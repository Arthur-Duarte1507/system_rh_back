from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from banco import pegar_banco

from esquemas import (
    BaterPontoRequisicao
)

from repositorios import funcionario_repositorio

from modelos import (
    RegistroPonto,
    Funcionario
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

    tipo_ponto = "Entrada"

    quantidade_registros = banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == dados.funcionario_id,
        func.date(RegistroPonto.data_hora) == date.today()
    ).count()

    if quantidade_registros % 2 != 0:
        tipo_ponto = "Saida"

    print(quantidade_registros)

    registro = registrar_ponto(
        banco,
        dados.funcionario_id,
        tipo_ponto
    )

    vfuncionario=funcionario_repositorio.buscar_funcionario_por_id(
            banco=banco,
            funcionario_id=dados.funcionario_id
        )
    
    vestado_trabalho = "Trabalhando" if tipo_ponto == "Entrada" else "Ausente"
    
    funcionario_repositorio.alterar_funcionario(
        banco=banco,
        funcionario=vfuncionario,
        nome=vfuncionario.nome,
        email=vfuncionario.email,
        cargo=vfuncionario.cargo,
        tempo_casa=vfuncionario.tempo_casa,
        aniversario=vfuncionario.aniversario,
        estado_trabalho= vestado_trabalho
    )

    return {
        "mensagem": "Ponto registrado",
        "registro": {
            "id": registro.id,
            "funcionario_id": registro.funcionario_id,
            "data_hora": registro.data_hora,
            "tipo": tipo_ponto
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
            "estado": "nao comecou"
        }

    if ultimo_ponto.tipo == "entrada":

        return {
            "estado": "Trabalhando"
        }

    if ultimo_ponto.tipo == "saida":

        return {
            "estado": "Saida"
        }

    if ultimo_ponto.tipo == "falta":

        return {
            "estado": "Falta"
        }

    if ultimo_ponto.tipo == "ferias":

        return {
            "estado": "Ferias"
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
