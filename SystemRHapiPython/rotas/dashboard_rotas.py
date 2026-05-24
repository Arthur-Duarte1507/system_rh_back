from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from repositorios.funcionario_repositorio import buscar_funcionario_por_id

from repositorios.banco_horas_repositorio import calcular_banco_horas

from repositorios.notificacao_repositorio import listar_notificacoes


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

    notificacoes = listar_notificacoes(
        banco
    )

    comunicados = []

    for notificacao in notificacoes:

        if notificacao.funcionario_id == funcionario_id:

            comunicados.append({
                "id": notificacao.id,
                "titulo": notificacao.titulo,
                "mensagem": notificacao.mensagem,
                "data": notificacao.data
            })

        if notificacao.funcionario_id == 0:

            comunicados.append({
                "id": notificacao.id,
                "titulo": notificacao.titulo,
                "mensagem": notificacao.mensagem,
                "data": notificacao.data
            })

    return {
        "funcionario": {
            "id": funcionario.id,
            "nome": funcionario.nome,
            "email": funcionario.email,
            "cargo": funcionario.cargo,
            "tempo_casa": funcionario.tempo_casa,
            "aniversario": funcionario.aniversario,
            "estado_trabalho": funcionario.estado_trabalho
        },

        "banco_horas": banco_horas,

        "comunicados": comunicados
    }