from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: dict, db: Session = Depends(get_db)):
    return {"id": 1, **user}

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return [{"id": 1, "username": "testuser", "email": "test@example.com"}]
