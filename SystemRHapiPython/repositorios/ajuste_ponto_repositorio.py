from sqlalchemy.orm import Session

from modelos import AjustePonto

def buscar_ajuste_por_id(
    banco: Session,
    ajuste_id: int
):

    return banco.query(AjustePonto).filter(
        AjustePonto.id == ajuste_id
    ).first()