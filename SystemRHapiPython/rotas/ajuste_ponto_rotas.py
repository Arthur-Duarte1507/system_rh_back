from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import AjustePontoRequisicao

from repositorios.ajuste_ponto_repositorio import (
    buscar_ajuste_por_id
)


router = APIRouter(
    prefix="/api/ajustes-ponto",
    tags=["Ajustes de Ponto"]
)

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