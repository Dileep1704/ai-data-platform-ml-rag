from fastapi import APIRouter
from backend.database import SessionLocal
from backend.models import UserData
from pymongo import MongoClient

router = APIRouter()

# MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ai_db"]

@router.post("/")
def ingest_data(record: dict):
    db = SessionLocal()

    # PostgreSQL
    user = UserData(name=record["name"], age=record["age"])
    db.add(user)
    db.commit()

    # MongoDB
    mongo_db.records.insert_one(record)

    return {"message": "Saved in PostgreSQL + MongoDB"}