from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/user")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user: str) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = user
    return f"User {current_user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, user: str) -> str:
    users[user_id] = user
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"



# uvicorn module_16_3:app
