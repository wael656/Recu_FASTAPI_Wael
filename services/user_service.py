from sqlmodel import Session
from models.user import User

def create_user(user: User, db: Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user