from sqlalchemy.orm import Session

from modelos import Conversa, Mensagem


def criar_conversa(
    banco: Session,
    titulo: str
):

    conversa = Conversa(
        titulo=titulo
    )

    banco.add(conversa)
    banco.commit()
    banco.refresh(conversa)

    return conversa


def listar_conversas(
    banco: Session
):

    return banco.query(Conversa).all()


def buscar_conversa_por_id(
    banco: Session,
    conversa_id: int
):

    return banco.query(Conversa).filter(
        Conversa.id == conversa_id
    ).first()


def enviar_mensagem(
    banco: Session,
    conversa_id: int,
    funcionario_id: int,
    texto: str
):

    mensagem = Mensagem(
        conversa_id=conversa_id,
        funcionario_id=funcionario_id,
        texto=texto
    )

    banco.add(mensagem)
    banco.commit()
    banco.refresh(mensagem)

    return mensagem


def listar_mensagens_da_conversa(
    banco: Session,
    conversa_id: int
):

    return banco.query(Mensagem).filter(
        Mensagem.conversa_id == conversa_id
    ).all()