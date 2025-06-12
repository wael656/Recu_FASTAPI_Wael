from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    cognom: str
    correu: str
    edat: int
    Dni: str
    telefon: str