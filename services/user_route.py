from fastapi import APIRouter, Depends
from sqlmodel import Session
from models.user import User
from services.user_service import create_user
from main import get_db

from Recu_FASTAPI_Wael.services.user_service import get_user_by_id

router = APIRouter()

@router.post("/users/")
def create(user: User, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)