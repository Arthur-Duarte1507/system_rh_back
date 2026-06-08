from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import NotificacaoRequisicao

from repositorios.notificacao_repositorio import (
    criar_notificacao,
    listar_notificacoes,
    buscar_notificacao_por_id,
    deletar_notificacao,
    atualizar_notificacao,
    formatar_notificacao
)


router = APIRouter(
    prefix="/api/notificacoes",
    tags=["Notificações"]
)


@router.post("")
def nova_notificacao(
    dados: NotificacaoRequisicao,
    banco: Session = Depends(pegar_banco)
):

    notificacao = criar_notificacao(
        banco,
        dados.funcionario_id,
        dados.titulo,
        dados.mensagem,
        dados.data,
    )

    return {
        "mensagem": "Notificação criada",
        "notificacao": formatar_notificacao(notificacao)
    }


@router.get("")
def buscar_notificacoes(
    banco: Session = Depends(pegar_banco)
):

    notificacoes = listar_notificacoes(
        banco
    )

    return [
        formatar_notificacao(notificacao)
        for notificacao in notificacoes
    ]


@router.delete("/{id}")
def remover_notificacao(
    id: int,
    banco: Session = Depends(pegar_banco)
):

    notificacao = buscar_notificacao_por_id(
        banco,
        id
    )

    if notificacao is None:

        return {
            "erro": "Notificação não encontrada"
        }

    deletar_notificacao(
        banco,
        notificacao
    )

    return {
        "mensagem": "Notificação removida"
    }

@router.put("/atualizar/{id}")
def atualizar_notificacao_endpoint(
    id: int,
    dados: NotificacaoRequisicao,
    banco: Session = Depends(pegar_banco)
):

    notificacao = buscar_notificacao_por_id(
        banco,
        id
    )

    if notificacao is None:

        return {
            "erro": "Notificação não encontrada"
        }

    notificacao_atualizada = atualizar_notificacao(
        banco,
        notificacao,
        dados.funcionario_id,
        dados.titulo,
        dados.mensagem,
        dados.data
    )

    return {
        "mensagem": "Notificação atualizada",
        "notificacao": formatar_notificacao(notificacao_atualizada)
    }
