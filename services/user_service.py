from sqlalchemy.sql.sqltypes import NULLTYPE
from sqlmodel import Session
from models.user import User

def create_user(user: User, db: Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(user_id: int, db: Session):
    return db.get(User, user_id)


def update_user(user_id: int, data: User, db: Session):
    db_user = db.get(User, user_id)
    if db_user:
        for key, value in data.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(user_id: int, db: Session):
    db_user = db.get(User, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"missatge": "Usuari eliminat correctament"}
    return {"error": "Usuari no trobat"}