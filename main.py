from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.model.user import userModel
from src.controler.user import usersController
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
    try:
        user = usersController.getUserById(user_id)
        response = json.loads(user)
        return JSONResponse(content=response,status_code=200)
    except ValueError:
        logger.error(ValueError)
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
        return  JSONResponse(content={"users": response},status_code=200)
    except ValueError:
        logger.error(ValueError)
        return {"users": None}