from pymongo import MongoClient
from dotenv import load_dotenv
import os

class modelUsers:
    client = None #Client to db
    db=None #database
    collection = None#collection

    def getUserById(self,id:int):
        result = self.collection.find_one({"id":id})
        if result !=None:
            result.pop('_id', None)
        return result
    
    def findUserByField(self,field:str,value):
        result = []
        mongoResult = self.collection.find({field:value})
        for element in mongoResult:
            element.pop('_id', None)
            result.append(element)
            mongoResult.next()
        if len(result)==0:
            return None
        return result

    def __init__(self):
        load_dotenv()
        mongouri =os.getenv('MONGO_URI')
        db =os.getenv('MONGO_DB')
        collections =os.getenv('MONGO_COLLECTIONS')
        self.client = MongoClient(mongouri) #Client to db
        self.db=self.client.get_database(db) #database
        self.collection = self.db.get_collection(collections) #collection