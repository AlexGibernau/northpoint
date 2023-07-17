from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def root():
    return{"url del curso":"https://alexgibernau.com"}