from fastapi import FastAPI
from src.model.user import modelUsers
from src.controler.user import usersController
import json

app = FastAPI()
modelUser = modelUsers()
usersController = usersController(modelUser)

@app.get("/user/{user_id}")
async def getUser(user_id: int):
    try:
        user = usersController.getUserById(user_id)
        response = json.loads(user)
        return response
    except ValueError:
        return {"user": None}

@app.get("/user/{field}/{value}")
async def search(field,value):
    try:
        if field == "age":
            value = int(value)
        users = usersController.findUserByField(field,value)
        if users == None:
            return {"users": None}
        response = json.loads(users)
        return {"users": response}
    except ValueError:
        return {"users": None}