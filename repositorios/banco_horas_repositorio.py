from sqlalchemy.orm import Session

from modelos import RegistroPonto


def calcular_banco_horas(
    banco: Session,
    funcionario_id: int
):

    registros = banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == funcionario_id
    ).all()

    total_registros = len(registros)

    horas = total_registros * 4

    return {
        "saldo": f"{horas}:00"
    }


def listar_extrato(
    banco: Session,
    funcionario_id: int
):

    registros = banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == funcionario_id
    ).all()

    lista = []

    for registro in registros:

        lista.append({
            "tipo": registro.tipo,
            "data_hora": registro.data_hora
        })

    return lista