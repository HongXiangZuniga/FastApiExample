This project is an example of a simple API built with the FastAPI framework. It includes the following endpoints:

 ```
Endpoints:
```
GET /user/id/<idUser> <get user by id>
GET /user/field/:value <get users by field and value>
```

The struct of mongo data is:

```json
{
  "id":22,
  "name":"Hong Xiang",
  "email":"hongxiang17@gmail.com",
  "age":27,
  "entryDate":{"$date":"2018-06-25T21:46:44.000Z"},
  "country":"Chile"
}
 ```

Variables used in the .env file to configure the project
 ```
MONGO_URI=
MONGO_DB=u
MONGO_COLLECTIONS=
LOGGER_LEVEL=<"DEBUG","INFO","WARNING","ERROR","CRITICAL"> // Default="INFO"
 ```

command for run:
```
 make run
```

command for installer:
 ```
    make install
 ```