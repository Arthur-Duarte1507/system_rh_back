from sqlalchemy.orm import Session

from modelos import RegistroPonto


def registrar_ponto(
    banco: Session,
    funcionario_id: int,
    tipo: str
):

    registro = RegistroPonto(
        funcionario_id=funcionario_id,
        tipo=tipo
    )

    banco.add(registro)

    banco.commit()

    banco.refresh(registro)

    return registro


def listar_pontos_funcionario(
    banco: Session,
    funcionario_id: int
):

    return banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == funcionario_id
    ).all()

def buscar_ultimo_ponto(
    banco: Session,
    funcionario_id: int
):

    return banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == funcionario_id
    ).order_by(
        RegistroPonto.data_hora.desc()
    ).first()