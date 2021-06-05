# Desafio Técnico - LuizaLabs

Esta documentação descreve a estrutura da API de produtos para desafios técnicos.

## Tecnologias

- `FastAPI`
- `Docker`
- `Postgres`
- `Alembic`
- `SQLAlchemy ORM`

## Clientes

Os endpoints de listagem e detalhe possuem clientes com a mesma estrutura, sendo que é composta por:

- `nome`: nome do cliente
- `email`: email do cliente

## Produtos

Os endpoints de listagem e detalhe possuem produtos com a mesma estrutura, sendo que esta é composta por:

- `preco`: preço do produto
- `imagem`: URL da imagem do produto
- `id`: id do produto
- `titulo`: nome do produto

### Listagem

`<PAGINA>` representa o número da página requisitada, iniciando em `1`.

URL: `http://localhost:8000/api/produtos/?page=<PAGINA>`

URL: `http://localhost:8000/api/clientes/?page=<PAGINA>`

### Detalhe

`<ID>` representa o `id` do produto, a ser coletado no endpoint de listagem.

URL: `http://localhost:8000/api/produtos/<ID>/`

URL: `http://localhost:8000/api/clientes/<ID>/`
