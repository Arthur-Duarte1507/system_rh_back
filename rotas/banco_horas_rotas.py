from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from repositorios.banco_horas_repositorio import (
    calcular_banco_horas,
    listar_extrato
)


router = APIRouter(
    prefix="/api/banco-horas",
    tags=["Banco de Horas"]
)


@router.get("/resumo/{funcionario_id}")
def resumo_banco_horas(
    funcionario_id: int,
    banco: Session = Depends(pegar_banco)
):

    resumo = calcular_banco_horas(
        banco,
        funcionario_id
    )

    return resumo


@router.get("/extrato/{funcionario_id}")
def extrato_banco_horas(
    funcionario_id: int,
    banco: Session = Depends(pegar_banco)
):

    extrato = listar_extrato(
        banco,
        funcionario_id
    )

    return extrato