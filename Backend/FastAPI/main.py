from fastapi import FastAPI
from routers import products, users

app = FastAPI()

# Routers
app.include_router(products.router)

app.include_router(users.router)


@app.get("/")
async def root():
    return "Hola FastAPI!"


@app.get("/url")
async def root():
    return {"url del curso": "https://alexgibernau.com"}
