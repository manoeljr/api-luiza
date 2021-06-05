from sqlalchemy import delete, update
from sqlalchemy.orm import Session

from src.schemas.produto_schema import Produto as produtoSchema
from src.infra.sqlalchemy.models.produtos import Produto as produtoModel


class RepositoryProduto:
    """ Repositorio de Produto """

    def __init__(self, session: Session):
        self.session = session

    def cadastrar(self, produtoSchema: produtoSchema):
        """  Cadastro de um produto  """
        produto = produtoModel(
            cliente_id=produtoSchema.cliente_id,
            preco=produtoSchema.preco,
            imagem=produtoSchema.imagem,
            nome_produto=produtoSchema.nome_produto,
            titulo=produtoSchema.titulo
        )
        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto

    def listar(self):
        """  Listar todos os clientes cadastrados  """
        produtos = self.session.query(produtoModel).all()
        return produtos

    def atualizar(self, produto_id: int, produtoSchema: produtoSchema):
        """  Atualizar um produto por ID  """
        updateProduto = update(produtoModel).where(produtoModel.id == produto_id).values(
            preco=produtoSchema.preco,
            imagem=produtoSchema.imagem,
            nome_produto=produtoSchema.nome_produto,
            titulo=produtoSchema.titulo
        )
        self.session.execute(updateProduto)
        self.session.commit()

    def deletar(self, produto_id: int):
        """  Deletar um produto por ID  """
        deleteProduto = delete(produtoModel).where(produtoModel.id == produto_id)
        self.session.execute(deleteProduto)
        self.session.commit()
