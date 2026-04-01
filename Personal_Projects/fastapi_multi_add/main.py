import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    app_name = os.getenv("APP_Name", "FastAPI")
    return {
        "service": app_name,
        "sum": a + b
    }