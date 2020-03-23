import logging
import sys

from fastapi import FastAPI
from .schemas.slack import Command
from starlette.requests import Request

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)
app = FastAPI(debug=True, redoc_url=None)


@app.get("/")
async def hello_world():
    return "hello"

@app.post("/task/")
async def add_task(request: Request):
    form = await request.form()
    command = Command(**form)
    log.info(command)

    return command