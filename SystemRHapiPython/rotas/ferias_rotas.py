from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco
from esquemas import FeriasRequisicao

from repositorios.ferias_repositorio import (
    solicitar_ferias,
    listar_ferias
)


router = APIRouter(
    prefix="/api/ferias",
    tags=["Férias"]
)


@router.get("")
def buscar_ferias(
    banco: Session = Depends(pegar_banco)
):

    ferias = listar_ferias(banco)

    lista = []

    for item in ferias:

        lista.append({
            "id": item.id,
            "funcionario_id": item.funcionario_id,
            "data_inicio": item.data_inicio,
            "data_fim": item.data_fim,
            "status": item.status
        })

    return lista


@router.post("/solicitar")
def criar_solicitacao_ferias(
    dados: FeriasRequisicao,
    banco: Session = Depends(pegar_banco)
):

    ferias = solicitar_ferias(
        banco,
        dados.funcionario_id,
        dados.data_inicio,
        dados.data_fim
    )

    return {
        "mensagem": "Solicitação de férias enviada",
        "ferias": {
            "id": ferias.id,
            "funcionario_id": ferias.funcionario_id,
            "data_inicio": ferias.data_inicio,
            "data_fim": ferias.data_fim,
            "status": ferias.status
        }
    }