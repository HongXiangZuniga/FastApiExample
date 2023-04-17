from bson.json_util import dumps
import logging

class usersController:
    model=None
    logger = None
    def getUserById(self,id:int):
        try:
            result = self.model.getUserById(id)
            if result == None:
                    return '{"user":"null"}'
            return dumps(result)
        except ValueError:
            self.logger.error(ValueError)
            return '{"user":"null"}'
    
    def findUserByField(self,field:str,value):
        try:
            result = self.model.findUserByField(field,value)
            if result == None:
                return None
            for element in result:
                print(element)
                element = dumps(element)
            return dumps(result)
        except ValueError:
            self.logger.error(ValueError)
            return None

    def __init__(self,modelUsers):
        self.model = modelUsers
        self.logger = logging.getLogger("userController")