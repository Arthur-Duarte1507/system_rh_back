from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import (
    MensagemRequisicao,
    ConversaRequisicao
)

from repositorios.chat_repositorio import (
    criar_conversa,
    listar_conversas,
    enviar_mensagem,
    listar_mensagens_da_conversa
)


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)


@router.post("/conversas")
def nova_conversa(
    dados: ConversaRequisicao,
    banco: Session = Depends(pegar_banco)
):

    conversa = criar_conversa(
        banco,
        dados.titulo
    )

    return {
        "mensagem": "Conversa criada",
        "conversa": {
            "id": conversa.id,
            "titulo": conversa.titulo
        }
    }


@router.get("/conversas")
def buscar_conversas(
    banco: Session = Depends(pegar_banco)
):

    conversas = listar_conversas(
        banco
    )

    lista = []

    for conversa in conversas:

        lista.append({
            "id": conversa.id,
            "titulo": conversa.titulo
        })

    return lista


@router.post("/mensagem")
def nova_mensagem(
    dados: MensagemRequisicao,
    banco: Session = Depends(pegar_banco)
):

    mensagem = enviar_mensagem(
        banco,
        dados.conversa_id,
        dados.funcionario_id,
        dados.texto
    )

    return {
        "mensagem": "Mensagem enviada",
        "dados": {
            "id": mensagem.id,
            "conversa_id": mensagem.conversa_id,
            "funcionario_id": mensagem.funcionario_id,
            "texto": mensagem.texto,
            "data_hora": mensagem.data_hora
        }
    }


@router.get("/conversas/{id}/mensagens")
def buscar_mensagens(
    id: int,
    banco: Session = Depends(pegar_banco)
):

    mensagens = listar_mensagens_da_conversa(
        banco,
        id
    )

    lista = []

    for mensagem in mensagens:

        lista.append({
            "id": mensagem.id,
            "conversa_id": mensagem.conversa_id,
            "funcionario_id": mensagem.funcionario_id,
            "texto": mensagem.texto,
            "data_hora": mensagem.data_hora
        })

    return lista