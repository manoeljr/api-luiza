from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.cliente_schema import Cliente
from src.infra.sqlalchemy.repository.cliente_repository import RepositoryCliente
from src.infra.sqlalchemy.config.database import get_db

from fastapi_pagination import Page, paginate


router = APIRouter()

@router.get('/api/clientes/', status_code=status.HTTP_200_OK, response_model=Page[Cliente])
def listar_clientes(session: Session = Depends(get_db)):
    clientes = RepositoryCliente(session).listar()
    return paginate(clientes)

@router.post('/api/clientes/', status_code=status.HTTP_201_CREATED, response_model=Cliente)
def cadastrar_cliente(cliente: Cliente, session: Session = Depends(get_db)):
    clienteCriado = RepositoryCliente(session).cadastrar(cliente)
    return clienteCriado

@router.delete("/api/clientes/{id}/", status_code=status.HTTP_200_OK)
def deletar_cliente(id: int, session: Session = Depends(get_db)):
    clienteDeletado = RepositoryCliente(session).deletar(id)
    return

@router.put("/api/clientes/{id}/", status_code=status.HTTP_200_OK)
def alterar_cliente(id: int, cliente: Cliente, session: Session = Depends(get_db)):
   clienteAlterado = RepositoryCliente(session).atualizar(id, cliente)
   return clienteAlterado

