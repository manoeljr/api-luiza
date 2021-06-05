from pydantic import BaseModel
from typing import Optional


class Produto(BaseModel):
    """ Classes Produto de Schemas na base de dados """
    id: Optional[str]
    preco: float
    imagem: str
    nome_produto: str
    titulo: str
    cliente_id: str

    class Config:
        orm_mode = True
