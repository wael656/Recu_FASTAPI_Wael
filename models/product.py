from sqlmodel import SQLModel, Field

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    categoria: str
    preu: float
    stock: int
    descripcio: str
    valoracio: str