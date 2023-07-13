from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int


users_list = [
    User(id=1, name="Alex", surname="Gibernau", email="alexgc808@gmail.com", age=26),
    User(id=2, name="Pol", surname="Agullo", email="eles@gmail.com", age=21),
    User(
        id=3,
        name="Adrian",
        surname="Rodriguez",
        email="adrianrodriguez@gmail.com",
        age=25,
    ),
]


@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Alex",
            "surname": "Gibernau",
            "email": "alexgc808@gmail.com",
            "age": 26,
        },
        {"name": "Pol", "surname": "Agullo", "email": "eles@gmail.com", "age": 21},
        {
            "name": "Adrian",
            "surname": "Rodriguez",
            "email": "adrianrodriguez@gmail.com",
            "age": 25,
        },
    ]


@app.get("/users")
async def users():
    return users_list


# Path
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error: no existe usuario"}


# Query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)



@app.post("/user/")
async def user(user: User):
        if type(search_user(user.id)) == User:
            return {"Error: Ya existe ese usuario."}
        else:    
            users_list.append(user)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error: no existe usuario"}