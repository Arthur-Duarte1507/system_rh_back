from sqlalchemy.orm import Session

from modelos import SolicitacaoFerias


def solicitar_ferias(
    banco: Session,
    funcionario_id: int,
    data_inicio: str,
    data_fim: str
):

    ferias = SolicitacaoFerias(
        funcionario_id=funcionario_id,
        data_inicio=data_inicio,
        data_fim=data_fim
    )

    banco.add(ferias)
    banco.commit()
    banco.refresh(ferias)

    return ferias


def listar_ferias(
    banco: Session
):

    return banco.query(SolicitacaoFerias).all()