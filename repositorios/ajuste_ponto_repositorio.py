from sqlalchemy.orm import Session

from modelos import AjustePonto


def criar_ajuste(
    banco: Session,
    funcionario_id: int,
    motivo: str
):

    ajuste = AjustePonto(
        funcionario_id=funcionario_id,
        motivo=motivo
    )

    banco.add(ajuste)

    banco.commit()

    banco.refresh(ajuste)

    return ajuste


def listar_ajustes(
    banco: Session
):

    return banco.query(AjustePonto).all()


def buscar_ajuste_por_id(
    banco: Session,
    ajuste_id: int
):

    return banco.query(AjustePonto).filter(
        AjustePonto.id == ajuste_id
    ).first()