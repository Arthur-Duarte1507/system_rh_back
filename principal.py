from fastapi import FastAPI

from banco import Base, engine

from rotas.autenticacao_rotas import router as autenticacao_router
from rotas.dashboard_rotas import router as dashboard_router
from rotas.funcionario_rotas import router as funcionario_router
from rotas.ponto_rotas import router as ponto_router
from rotas.ferias_rotas import router as ferias_router
from rotas.chat_rotas import router as chat_router
from rotas.notificacao_rotas import router as notificacao_router

from rotas.ajuste_ponto_rotas import router as ajuste_ponto_router
from rotas.banco_horas_rotas import router as banco_horas_router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API RH",
    description="Sistema de RH para aplicativo Flutter",
    version="1.0"
)


app.include_router(autenticacao_router)
app.include_router(dashboard_router)
app.include_router(funcionario_router)
app.include_router(ponto_router)
app.include_router(ferias_router)
app.include_router(chat_router)
app.include_router(notificacao_router)
app.include_router(ajuste_ponto_router)
app.include_router(banco_horas_router)


@app.get("/")
def inicio():

    return {
        "mensagem": "API RH funcionando"
    }