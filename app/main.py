from fastapi import FastAPI

app = FastAPI(debug=True, redoc_url=None)

@app.get("/")
async def hello_world():
    return "hello"

@app.post("/task")
async def add_task(msg: str):
    print(msg)
    return msg