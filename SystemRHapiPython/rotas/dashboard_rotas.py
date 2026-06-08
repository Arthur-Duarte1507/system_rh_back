from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from repositorios.funcionario_repositorio import (
    buscar_funcionario_por_id,
    formatar_funcionario
)

from repositorios.banco_horas_repositorio import calcular_banco_horas

from repositorios.notificacao_repositorio import (
    formatar_notificacao,
    listar_notificacoes_funcionario
)


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/{funcionario_id}")
def dashboard(
    funcionario_id: int,
    banco: Session = Depends(pegar_banco)
):

    funcionario = buscar_funcionario_por_id(
        banco,
        funcionario_id
    )

    if funcionario is None:

        return {
            "erro": "Funcionário não encontrado"
        }

    banco_horas = calcular_banco_horas(
        banco,
        funcionario_id
    )

    notificacoes = listar_notificacoes_funcionario(
        banco,
        funcionario_id
    )

    comunicados = [
        formatar_notificacao(notificacao)
        for notificacao in notificacoes
    ]

    return {
        "funcionario": formatar_funcionario(
            banco,
            funcionario
        ),

        "banco_horas": banco_horas,

        "comunicados": comunicados
    }
