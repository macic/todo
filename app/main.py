from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.handlers.command import CommandHandler
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

    command = CommandHandler(command)
    command.handle(rest, full_command)
    return command.response()
