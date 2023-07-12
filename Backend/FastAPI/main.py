from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola gente!"

@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}