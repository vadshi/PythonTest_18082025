from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    Request
)

# library for validation, serialiazation and deserialization
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Item, SessionLocal

app = FastAPI()


@app.get("/home")
def get_home():
    return {"message": "Hello, world!"}