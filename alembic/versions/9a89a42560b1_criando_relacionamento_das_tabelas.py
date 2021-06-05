"""Criando relacionamento das tabelas

Revision ID: 9a89a42560b1
Revises: 
Create Date: 2021-06-05 15:41:26.478656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a89a42560b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_clientes_id'), 'clientes', ['id'], unique=False)
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('imagem', sa.String(), nullable=True),
    sa.Column('nome_produto', sa.String(), nullable=False),
    sa.Column('titulo', sa.String(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome_produto')
    )
    op.create_index(op.f('ix_produtos_id'), 'produtos', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_produtos_id'), table_name='produtos')
    op.drop_table('produtos')
    op.drop_index(op.f('ix_clientes_id'), table_name='clientes')
    op.drop_table('clientes')
    # ### end Alembic commands ###
