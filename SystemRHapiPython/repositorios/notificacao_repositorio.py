from sqlalchemy.orm import Session

from modelos import Notificacao, NotificacaoDestinatario


def _normalizar_funcionario_id(funcionario_id: int | None):
    if funcionario_id == 0:
        return None

    return funcionario_id


def _destinatario_principal(notificacao: Notificacao):
    if not notificacao.destinatarios:
        return None

    return notificacao.destinatarios[0]


def formatar_notificacao(notificacao: Notificacao):
    destinatario = _destinatario_principal(notificacao)

    funcionario_id = None
    lida = False

    if destinatario is not None:
        funcionario_id = destinatario.funcionario_id
        lida = destinatario.lida

    return {
        "id": notificacao.id,
        "funcionario_id": funcionario_id if funcionario_id is not None else 0,
        "titulo": notificacao.titulo,
        "mensagem": notificacao.mensagem,
        "data": notificacao.data,
        "lida": lida
    }


def criar_notificacao(
    banco: Session,
    funcionario_id: int,
    titulo: str,
    mensagem: str,
    data: str
):
    notificacao = Notificacao(
        titulo=titulo,
        mensagem=mensagem,
        data=data
    )

    banco.add(notificacao)
    banco.flush()

    destinatario = NotificacaoDestinatario(
        notificacao_id=notificacao.id,
        funcionario_id=_normalizar_funcionario_id(funcionario_id),
        lida=False
    )

    banco.add(destinatario)
    banco.commit()
    banco.refresh(notificacao)

    return notificacao


def listar_notificacoes(
    banco: Session
):
    return banco.query(Notificacao).all()


def listar_notificacoes_funcionario(
    banco: Session,
    funcionario_id: int
):
    return banco.query(Notificacao).join(
        NotificacaoDestinatario
    ).filter(
        (
            NotificacaoDestinatario.funcionario_id == funcionario_id
        ) | (
            NotificacaoDestinatario.funcionario_id.is_(None)
        )
    ).distinct().all()


def buscar_notificacao_por_id(
    banco: Session,
    notificacao_id: int
):
    return banco.query(Notificacao).filter(
        Notificacao.id == notificacao_id
    ).first()


def deletar_notificacao(
    banco: Session,
    notificacao: Notificacao
):
    banco.delete(notificacao)
    banco.commit()

    return True


def atualizar_notificacao(
    banco: Session,
    notificacao: Notificacao,
    funcionario_id: int,
    titulo: str,
    mensagem: str,
    data
):
    notificacao.titulo = titulo
    notificacao.mensagem = mensagem
    notificacao.data = data

    destinatario = _destinatario_principal(notificacao)

    if destinatario is None:
        destinatario = NotificacaoDestinatario(
            notificacao_id=notificacao.id
        )
        banco.add(destinatario)

    destinatario.funcionario_id = _normalizar_funcionario_id(funcionario_id)

    banco.commit()
    banco.refresh(notificacao)

    return notificacao
