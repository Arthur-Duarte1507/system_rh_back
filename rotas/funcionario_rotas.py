from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from repositorios.funcionario_repositorio import (
    buscar_funcionario_por_id,
    listar_funcionarios,
    criar_funcionario,
    alterar_funcionario,
    deletar_funcionario
)

from esquemas import (
    CriarFuncionarioRequisicao,
    AlterarFuncionarioRequisicao
)


router = APIRouter(
    prefix="/api/funcionarios",
    tags=["Funcionários"]
)


@router.get("")
def buscar_funcionarios(
    banco: Session = Depends(pegar_banco)
):

    funcionarios = listar_funcionarios(banco)

    lista = []

    for funcionario in funcionarios:

        lista.append({
            "id": funcionario.id,
            "nome": funcionario.nome,
            "email": funcionario.email,
            "cargo": funcionario.cargo,
            "tempo_casa": funcionario.tempo_casa,
            "aniversario": funcionario.aniversario,
            "estado_trabalho": funcionario.estado_trabalho
        })

    return lista


@router.get("/{id}")
def buscar_funcionario(
    id: int,
    banco: Session = Depends(pegar_banco)
):

    funcionario = buscar_funcionario_por_id(
        banco,
        id
    )

    if funcionario is None:

        return {
            "erro": "Funcionário não encontrado"
        }

    return {
        "id": funcionario.id,
        "nome": funcionario.nome,
        "email": funcionario.email,
        "cargo": funcionario.cargo,
        "tempo_casa": funcionario.tempo_casa,
        "aniversario": funcionario.aniversario,
        "estado_trabalho": funcionario.estado_trabalho
    }


@router.post("")
def cadastrar_funcionario(
    dados: CriarFuncionarioRequisicao,
    banco: Session = Depends(pegar_banco)
):

    funcionario = criar_funcionario(
        banco,
        dados.nome,
        dados.email,
        dados.senha,
        dados.cargo,
        dados.tempo_casa,
        dados.aniversario
    )

    return {
        "mensagem": "Funcionário criado com sucesso",
        "funcionario": {
            "id": funcionario.id,
            "nome": funcionario.nome,
            "email": funcionario.email,
            "cargo": funcionario.cargo,
            "estado_trabalho": funcionario.estado_trabalho,
            "tempo_casa": funcionario.tempo_casa,
            "aniversario": funcionario.aniversario
        }
    }


@router.put("/{id}")
def atualizar_funcionario(
    id: int,
    dados: AlterarFuncionarioRequisicao,
    banco: Session = Depends(pegar_banco)
):

    funcionario = buscar_funcionario_por_id(
        banco,
        id
    )

    if funcionario is None:

        return {
            "erro": "Funcionário não encontrado"
        }

    funcionario_atualizado = alterar_funcionario(
        banco,
        funcionario,
        dados.nome,
        dados.email,
        dados.cargo,
        dados.tempo_casa,
        dados.aniversario,
        dados.estado_trabalho
    )

    return {
        "mensagem": "Funcionário atualizado",
        "funcionario": {
            "id": funcionario_atualizado.id,
            "nome": funcionario_atualizado.nome,
            "email": funcionario_atualizado.email,
            "cargo": funcionario_atualizado.cargo,
            "tempo_casa": funcionario_atualizado.tempo_casa,
            "aniversario": funcionario_atualizado.aniversario,
            "estado_trabalho": funcionario_atualizado.estado_trabalho
        }
    }


@router.delete("/{id}")
def remover_funcionario(
    id: int,
    banco: Session = Depends(pegar_banco)
):

    funcionario = buscar_funcionario_por_id(
        banco,
        id
    )

    if funcionario is None:

        return {
            "erro": "Funcionário não encontrado"
        }

    deletar_funcionario(
        banco,
        funcionario
    )

    return {
        "mensagem": "Funcionário removido"
    }
