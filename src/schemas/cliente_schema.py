from pydantic import BaseModel
from src.schemas.produto_schema import Produto
from typing import Optional, List


class Cliente(BaseModel):
    """ Classes Cliente de Schemas na base de dados """
    id: Optional[str]
    nome: str
    email: str
    produtos: List[Produto] = []

    class Config:
        orm_mode = True
