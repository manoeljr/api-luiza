from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):
    """ Representacao do Produtos na base de dados """
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, index=True)
    preco = Column(Float, nullable=False)
    imagem = Column(String)
    nome_produto = Column(String, nullable=False, unique=True)
    titulo = Column(String)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship('Cliente', back_populates='produtos')

    def __repr__(self):
        return f"Produto: [nome={self.nome_produto}]"
