from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.constants import InternalException
from app.handlers.command import CommandHandler
from .schemas.slack import Command
from .utils import split_by_first_space

app = FastAPI(debug=True, redoc_url=None)


@app.get("/")
async def hello_world():
    return "hello"


@app.post("/task/")
async def task_handler(request: Request):
    form = await request.form()
    try:
        full_command = Command(**form)
        command, rest = split_by_first_space(full_command.text)
        command = CommandHandler(command)
        command.parse_text(rest)
        command.handle(full_command)
        return command.response()
    except InternalException as exc:
        return exc.get_message()
