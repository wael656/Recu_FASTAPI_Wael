from fastapi import Depends
from schemas.user_schema import UserRead
from sqlmodel import Session
from Recu_FASTAPI_Wael.main import get_db
from Recu_FASTAPI_Wael.models.users import User
from Recu_FASTAPI_Wael.services.user_route import router
from Recu_FASTAPI_Wael.services.user_service import get_user_by_id, update_user, delete_user


@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)

@router.put("/users/{user_id}")
def update(user_id: int, user: User, db: Session = Depends(get_db)):
    return update_user(user_id, user, db)

@router.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)