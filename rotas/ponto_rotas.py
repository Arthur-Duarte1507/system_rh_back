from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import (
    BaterPontoRequisicao
)

from repositorios.ponto_repositorio import (
    registrar_ponto,
    listar_pontos_funcionario,
    buscar_ultimo_ponto
)


router = APIRouter(
    prefix="/api/ponto",
    tags=["Ponto"]
)


@router.post("/bater")
def bater_ponto(
    dados: BaterPontoRequisicao,
    banco: Session = Depends(pegar_banco)
):

    registro = registrar_ponto(
        banco,
        dados.funcionario_id,
        dados.tipo
    )

    return {
        "mensagem": "Ponto registrado",
        "registro": {
            "id": registro.id,
            "funcionario_id": registro.funcionario_id,
            "tipo": registro.tipo,
            "data_hora": registro.data_hora
        }
    }


@router.get("/historico/{funcionario_id}")
def historico_ponto(
    funcionario_id: int,
    banco: Session = Depends(pegar_banco)
):

    registros = listar_pontos_funcionario(
        banco,
        funcionario_id
    )

    lista = []

    for registro in registros:

        lista.append({
            "id": registro.id,
            "tipo": registro.tipo,
            "data_hora": registro.data_hora
        })

    return lista


@router.get("/status/{funcionario_id}")
def status_ponto(
    funcionario_id: int,
    banco: Session = Depends(pegar_banco)
):

    ultimo_ponto = buscar_ultimo_ponto(
        banco,
        funcionario_id
    )

    if ultimo_ponto is None:

        return {
            "estado": "nao_comecou"
        }

    if ultimo_ponto.tipo == "entrada":

        return {
            "estado": "trabalhando"
        }

    if ultimo_ponto.tipo == "saida":

        return {
            "estado": "saida"
        }

    if ultimo_ponto.tipo == "falta":

        return {
            "estado": "falta"
        }

    if ultimo_ponto.tipo == "ferias":

        return {
            "estado": "ferias"
        }

    return {
        "estado": ultimo_ponto.tipo
    }


@router.get("/hoje/{funcionario_id}")
def ponto_hoje(
    funcionario_id: int,
    banco: Session = Depends(pegar_banco)
):

    registros = listar_pontos_funcionario(
        banco,
        funcionario_id
    )

    lista = []

    for registro in registros:

        lista.append({
            "tipo": registro.tipo,
            "data_hora": registro.data_hora
        })

    return lista