from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.produto_schema import Produto
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repository.produto_repository import RepositoryProduto

from fastapi_pagination import Page, paginate

router = APIRouter()

@router.get('/api/produtos/', status_code=status.HTTP_200_OK, response_model=Page[Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositoryProduto(session).listar()
    return  paginate(produtos)

@router.post('/api/produtos/', status_code=status.HTTP_201_CREATED, response_model=Produto)
def cadastrar_produto(produto: Produto, session: Session = Depends(get_db)):
    produtoCriado = RepositoryProduto(session).cadastrar(produto)
    return produtoCriado

@router.delete("/api/produtos/{id}/", status_code=status.HTTP_200_OK)
def deletar_produto(id: int, session: Session = Depends(get_db)):
    produtoDeletado = RepositoryProduto(session).deletar(id)
    return

@router.put("/api/produtos/{id}/", status_code=status.HTTP_200_OK)
def alterar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
   produtoAlterado = RepositoryProduto(session).atualizar(id, produto)
   return produtoAlterado