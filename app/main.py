from fastapi import FastAPI
from starlette.requests import Request
from .schemas.slack import Command, BasicMessage
from .crud import item
from .utils import parse_command, log

app = FastAPI(debug=True, redoc_url=None)


@app.get("/")
async def hello_world():
    return "hello"


@app.post("/task/")
async def task_handler(request: Request, response_model: BasicMessage):
    form = await request.form()

    log.info("form")
    log.info(form)
    log.info("content-type")
    log.info(request.headers['content-type'])

    command = Command(**form)
    log.info(command)

    command, rest = parse_command(command)
    if not command:
        return {"text": rest}

    # dummy way to check postgres fast
    if command == 'add':
        from app.db.session import db_session
        from app.schemas.item import ItemCreate
        obj = item.create(db_session=db_session, obj_in=ItemCreate(title=rest))
        log.info("item created")
    return BasicMessage(**{
        "response_type": "in_channel",
        "text": "Added fine."
    })

