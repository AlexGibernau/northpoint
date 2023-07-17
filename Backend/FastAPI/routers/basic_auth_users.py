from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "alex": {
        "username": "North",
        "full_name": "Alex Gibernau",
        "email": "alex@gmail.com",
        "disabled": False,
        "password": "123456",
    },
    "alex2": {
        "username": "North2",
        "full_name": "Alex Gibernau2",
        "email": "alex2@gmail.com",
        "disabled": True,
        "password": "654321",
    },
}


def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="No autorizado mi siela"
        )


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = form.username
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no se ha encontrado",
        )

    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Valiste con la contraseña.")

    return {"acces_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
