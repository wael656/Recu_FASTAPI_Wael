from pydantic import BaseModel

class UserRead(BaseModel):
    id: int
    nom: str
    cognom: str
    correu: str
    edat: int
    dni: str
    telefon: str

    class Config:
        orm_mode = True