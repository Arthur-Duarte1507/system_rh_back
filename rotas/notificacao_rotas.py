from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import NotificacaoRequisicao

from repositorios.notificacao_repositorio import (
    criar_notificacao,
    listar_notificacoes,
    buscar_notificacao_por_id,
    marcar_como_lida,
    deletar_notificacao
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
        dados.mensagem
    )

    return {
        "mensagem": "Notificação criada",
        "notificacao": {
            "id": notificacao.id,
            "titulo": notificacao.titulo,
            "mensagem": notificacao.mensagem,
            "lida": notificacao.lida
        }
    }


@router.get("")
def buscar_notificacoes(
    banco: Session = Depends(pegar_banco)
):

    notificacoes = listar_notificacoes(
        banco
    )

    lista = []

    for notificacao in notificacoes:

        lista.append({
            "id": notificacao.id,
            "funcionario_id": notificacao.funcionario_id,
            "titulo": notificacao.titulo,
            "mensagem": notificacao.mensagem,
            "lida": notificacao.lida
        })

    return lista


@router.put("/{id}/lida")
def ler_notificacao(
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

    notificacao = marcar_como_lida(
        banco,
        notificacao
    )

    return {
        "mensagem": "Notificação marcada como lida",
        "notificacao": {
            "id": notificacao.id,
            "lida": notificacao.lida
        }
    }


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