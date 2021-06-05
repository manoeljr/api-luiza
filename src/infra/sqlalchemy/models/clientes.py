from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Cliente(Base):
    """ Representacao do Cliente na base de dados """
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    produtos = relationship('Produto', back_populates='cliente')

    def __repr__(self):
        return f"Cliente [nome={self.nome}]"
