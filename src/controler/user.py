from bson.json_util import dumps
import logging
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
    country: str


class usersController:
    model = None
    logger = None

    def getUserById(self, id: int):
        try:
            result = self.model.getUserById(id)
            if result == None:
                return '{"user":"null"}'
            return dumps(result)
        except ValueError:
            self.logger.error(ValueError)
            return '{"user":"null"}'

    def postUser(self, User):
        return self.model.postUser(User.name, User.email, User.country, User.age)

    def putUser(self, id, User):
        if not hasattr(User, 'name'):
            User.name = None
        if not hasattr(User, 'email'):
            User.email = None
        if not hasattr(User, 'country'):
            User.country = None
        if not hasattr(User, 'age'):
            User.age = None
        return self.model.putUser(id, User.name, User.email, User.country, User.age)

    def findUserByField(self, field: str, value):
        try:
            result = self.model.findUserByField(field, value)
            if result == None:
                return None
            for element in result:
                print(element)
                element = dumps(element)
            return dumps(result)
        except ValueError:
            self.logger.error(ValueError)
            return None

    def __init__(self, modelUsers):
        self.model = modelUsers
        self.logger = logging.getLogger("userController")
