from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"], responses={404: {"message": "No encontrado"}})


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


@router.get("/usersjson")
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


@router.get("/users")
async def users():
    return users_list


# Path
@router.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error: no existe usuario"}


# Query
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)


@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(204, detail="Error: Ya existe ese usuario.")
    else:
        users_list.append(user)
        return user


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error: no existe usuario"}


@router.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"Error: no se ha actualizado el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return "Eliminado"
    if not found:
        return {"Error: no se ha borrado el usuario"}
