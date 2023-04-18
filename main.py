from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from src.model.user import userModel
from src.controler.user import usersController
from src.controler.user import User
from dotenv import load_dotenv
import json
import logging
import os

level = 0
load_dotenv()
loggerLevel = os.getenv('LOGGER_LEVEL')
if loggerLevel == "DEBUG":
    level = logging.DEBUG
elif loggerLevel == "INFO":
    level = logging.INFO
elif loggerLevel == "WARNING":
    level = logging.WARNING
elif loggerLevel == "ERROR":
    level = logging.ERROR
elif loggerLevel == "CRITICAL":
    level = logging.CRITICAL
else:
    level = logging.INFO
logging.basicConfig(level=level)
logger = logging.getLogger("main")

logger.info("INIT FastAPI")
app = FastAPI()

logger.info("INIT User Model")
userModel = userModel()

logger.info("INIT User Controler")
usersController = usersController(userModel)


@app.get("/user/{user_id}")
async def getUser(user_id: int):
    user = usersController.getUserById(user_id)
    response = json.loads(user)
    return JSONResponse(content=response, status_code=200)


@app.get("/user/{field}/{value}")
async def search(field, value):
    if field == "age":
        value = int(value)
    users = usersController.findUserByField(field, value)
    if users == None:
        return {"users": None}
    response = json.loads(users)
    return JSONResponse(content={"users": response}, status_code=200)


@app.post("/user")
async def create_item(request: Request):
    body = await request.json()
    if not ("name" in body or "age" in body or "country" in body or "email" in body):
        return JSONResponse(content={"error": "Missing information, required fields are name, email, country and Age"}, status_code=404)
    User.age = body["age"]
    User.name = body["name"]
    User.country = body["country"]
    User.email = body["email"]
    result = usersController.postUser(User)
    return result


@app.put("/user/{user_id}")
async def create_item(user_id: int, request: Request, response: Response):
    body = await request.json()
    if ("name" in body):
        User.name = body["name"]
    if ("age" in body):
        User.age = body["age"]
    if ("country" in body):
        User.country = body["country"]
    if ("email" in body):
        User.email = body["email"]
    usersController.putUser(user_id, User)
    response.status_code = 204
