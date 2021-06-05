from sqlalchemy import update, delete
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models.clientes import Cliente as clienteModel
from src.schemas.cliente_schema import Cliente as clienteSchema


class RepositoryCliente:
    """ Repositorio de Cliente """

    def __init__(self, session: Session):
        self.session = session

    def cadastrar(self, clienteSchema: clienteSchema):
        """  Cadastro de um cliente  """
        db_cliente = clienteModel(nome=clienteSchema.nome, email=clienteSchema.email)
        self.session.add(db_cliente)
        self.session.commit()
        self.session.refresh(db_cliente)
        return db_cliente

    def listar(self) -> clienteSchema:
        """  Listar todos os clientes cadastrados  """
        clientes = self.session.query(clienteModel).all()
        return clientes

    def atualizar(self, cliente_id: int, clienteSchema: clienteSchema):
        """  Atualizar um cliente por ID   """
        clienteUpdate = update(clienteModel).where(clienteModel.id == cliente_id).values(
            nome = clienteSchema.nome,
            email = clienteSchema.email
        )
        self.session.execute(clienteUpdate)
        self.session.commit()

    def deletar(self, cliente_id: int):
        """   Deletar um cliente por ID   """
        delete_stmt = delete(clienteModel).where(clienteModel.id == cliente_id)
        self.session.execute(delete_stmt)
        self.session.commit()
