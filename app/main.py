from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from .schemas.slack import Command, BasicMessage, ErrorMessage
from .crud import item
from .utils import parse_command, log

app = FastAPI(debug=True, redoc_url=None)


@app.get("/")
async def hello_world():
    return "hello"


@app.post("/task/")
async def task_handler(request: Request):
    form = await request.form()
    full_command = Command(**form)
    command, rest = parse_command(full_command)
    if not command:
        return JSONResponse({"text": rest})

    # dummy way to check postgres fast
    if command == 'add':
        from app.db.session import db_session
        from app.schemas.item import ItemCreate
        obj = item.create(db_session=db_session,
                          obj_in=ItemCreate(title=rest, user_id=full_command.user_id, user_name=full_command.user_name))
        log.info("item created")
    return JSONResponse({"text": "Added fine."})
