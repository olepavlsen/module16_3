from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/user")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
                      , age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = username, age
    return f"User {current_user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: Annotated[
    str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
                      , age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    users[user_id] = username, age
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(description="Enter user_id")]) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"

# uvicorn module_16_3:app
