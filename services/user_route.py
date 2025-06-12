from fastapi import APIRouter, Depends
from sqlmodel import Session
from models.user import User
from services.user_service import create_user
from main import get_db

router = APIRouter()

@router.post("/users/")
def create(user: User, db: Session = Depends(get_db)):
    return create_user(user, db)
