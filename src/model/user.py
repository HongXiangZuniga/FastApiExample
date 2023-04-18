from pymongo import MongoClient
from pymongo.errors import WriteError
from pymongo import DESCENDING

from dotenv import load_dotenv
import os
import logging
from datetime import datetime


class userModel:
    client = None  # Client to db
    db = None  # database
    collection = None  # collection
    logger = None

    def getUserById(self, id: int):
        try:
            result = self.collection.find_one({"id": id})
            if result != None:
                result.pop('_id', None)
            return result
        except ValueError:
            self.logger.error(ValueError)
            return None

    def postUser(self, name: str, email: str, country: str, age: int):
        try:
            lastUser = self.collection.find_one({}, sort=[("id", DESCENDING)])
            lastId = lastUser["id"]
            now = datetime.now()
            user = {"id": lastId+1, "name": name, "age": age,
                    "country": country, "entryDate": now}
            self.collection.insert_one(user)
            del user["_id"]
            return user
        except WriteError as e:
            logging.error("Error:", e)

    def putUser(self, id: int, name: str, email: str, country: str, age: int):
        try:
            update = {}
            if name is not None:
                update["name"] = name
            if email is not None:
                update["email"] = email
            if country is not None:
                update["country"] = country
            if age is not None:
                update["age"] = age
            self.collection.update_one({"id": id}, {"$set": update})
        except WriteError as e:
            logging.error("Error:", e)
    
    def deleteUser(self, id:int):
        return self.collection.delete_one({"id": id})
   

    def findUserByField(self, field: str, value):
        try:
            result = []
            mongoResult = self.collection.find({field: value})
            for element in mongoResult:
                element.pop('_id', None)
                result.append(element)
                mongoResult.next()
            if len(result) == 0:
                return None
            return result
        except ValueError:
            self.logger.error(ValueError)
            return None

    def __init__(self):
        load_dotenv()
        mongouri = os.getenv('MONGO_URI')
        db = os.getenv('MONGO_DB')
        collections = os.getenv('MONGO_COLLECTIONS')
        self.client = MongoClient(mongouri)  # Client to db
        self.db = self.client.get_database(db)  # database
        self.collection = self.db.get_collection(collections)  # collection
        self.logger = logging.getLogger("userModel")
