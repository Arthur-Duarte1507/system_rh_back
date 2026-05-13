from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import AjustePontoRequisicao

from repositorios.ajuste_ponto_repositorio import (
    criar_ajuste,
    listar_ajustes,
    buscar_ajuste_por_id
)


router = APIRouter(
    prefix="/api/ajustes-ponto",
    tags=["Ajustes de Ponto"]
)


@router.post("")
def novo_ajuste(
    dados: AjustePontoRequisicao,
    banco: Session = Depends(pegar_banco)
):

    ajuste = criar_ajuste(
        banco,
        dados.funcionario_id,
        dados.motivo
    )

    return {
        "mensagem": "Ajuste criado",
        "ajuste": {
            "id": ajuste.id,
            "funcionario_id": ajuste.funcionario_id,
            "motivo": ajuste.motivo,
            "status": ajuste.status
        }
    }


@router.get("")
def buscar_ajustes(
    banco: Session = Depends(pegar_banco)
):

    ajustes = listar_ajustes(banco)

    lista = []

    for ajuste in ajustes:

        lista.append({
            "id": ajuste.id,
            "funcionario_id": ajuste.funcionario_id,
            "motivo": ajuste.motivo,
            "status": ajuste.status
        })

    return lista


@router.get("/{id}")
def buscar_ajuste(
    id: int,
    banco: Session = Depends(pegar_banco)
):

    ajuste = buscar_ajuste_por_id(
        banco,
        id
    )

    if ajuste is None:

        return {
            "erro": "Ajuste não encontrado"
        }

    return {
        "id": ajuste.id,
        "funcionario_id": ajuste.funcionario_id,
        "motivo": ajuste.motivo,
        "status": ajuste.status
    }