from sqlmodel import Session
from models.user import User

def create_user(user: User, db: Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(user_id: int, db: Session):
    return db.get(User, user_id)
