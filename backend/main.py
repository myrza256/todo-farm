from fastapi import FastAPI, HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

from database import *

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo{title}")
async def get_todo(title):
    response = await fetch_one_todo(title)
    if responses:
        return response
    raise HTTPException(404, f"not TODO with this title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "sssssssssssssssssss")

@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"Not found {title}")

@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Deleted ok"
    raise HTTPException(404, f"no TODO itme with this title{title}")





