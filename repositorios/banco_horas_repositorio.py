from sqlalchemy.orm import Session

from modelos import RegistroPonto

from datetime import timedelta


def calcular_banco_horas(
    banco: Session,
    funcionario_id: int
):

    registros = banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == funcionario_id
    ).order_by(RegistroPonto.data_hora).all()

    total_tempo = timedelta()

    entrada = None

    for registro in registros:

        if registro.tipo == "Entrada":

            entrada = registro.data_hora

            print(f"Entrada: {entrada}")

        elif registro.tipo == "Saida" and entrada is not None:

            diferenca = registro.data_hora - entrada

            print(f"Saída: {registro.data_hora}")
            print(f"Diferença: {diferenca}")

            total_tempo += diferenca

            entrada = None

    total_segundos = int(total_tempo.total_seconds())

    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return {
        "saldo": f"{horas:02}:{minutos:02}:{segundos:02}"
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