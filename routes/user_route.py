from fastapi import Depends
from schemas.user_schema import UserRead
from sqlmodel import Session
from Recu_FASTAPI_Wael.main import get_db
from Recu_FASTAPI_Wael.services.user_route import router
from Recu_FASTAPI_Wael.services.user_service import get_user_by_id


@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)