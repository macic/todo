from fastapi import FastAPI
from .schemas.msg import Msg
app = FastAPI(debug=True, redoc_url=None)

@app.get("/")
async def hello_world():
    return "hello"

@app.post("/task/")
async def add_task(msg: Msg):
    print(msg)
    return msg