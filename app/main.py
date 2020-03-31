from fastapi import FastAPI, Depends
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.constants import InternalException
from app.handlers.command import CommandHandler
from app.handlers.utils import get_db
from app.db.session import Session
from .schemas.slack import Command
from .utils import split_by_first_space

app = FastAPI(debug=True, redoc_url=None)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


@app.get("/")
async def hello_world():
    return "hello"


@app.post("/task/")
async def task_handler(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    try:
        full_command = Command(**form)
        command, rest = split_by_first_space(full_command.text)
        command = CommandHandler(command, db)
        command.parse_text(rest)
        command.handle(full_command)
        return command.response()
    except InternalException as exc:
        return exc.get_message()
