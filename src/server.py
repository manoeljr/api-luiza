from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import cliente_router, produto_router
from fastapi_pagination import add_pagination


app = FastAPI()

origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def page_home():
    return {'message': 'Página de Desafio LuizaLabs'}

app.include_router(cliente_router.router)
app.include_router(produto_router.router)

add_pagination(app)

