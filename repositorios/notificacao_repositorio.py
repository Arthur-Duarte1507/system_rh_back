from sqlalchemy.orm import Session

from modelos import Notificacao


def criar_notificacao(
    banco: Session,
    funcionario_id: int,
    titulo: str,
    mensagem: str
):

    notificacao = Notificacao(
        funcionario_id=funcionario_id,
        titulo=titulo,
        mensagem=mensagem
    )

    banco.add(notificacao)

    banco.commit()

    banco.refresh(notificacao)

    return notificacao


def listar_notificacoes(
    banco: Session
):

    return banco.query(Notificacao).all()


def buscar_notificacao_por_id(
    banco: Session,
    notificacao_id: int
):

    return banco.query(Notificacao).filter(
        Notificacao.id == notificacao_id
    ).first()


def marcar_como_lida(
    banco: Session,
    notificacao: Notificacao
):

    notificacao.lida = True

    banco.commit()

    banco.refresh(notificacao)

    return notificacao

def deletar_notificacao(
    banco: Session,
    notificacao: Notificacao
):

    banco.delete(notificacao)

    banco.commit()

    return True