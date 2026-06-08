from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from repositorios.funcionario_repositorio import (
    buscar_funcionario_por_id,
    listar_funcionarios,
    criar_funcionario,
    alterar_funcionario,
    deletar_funcionario,
    formatar_funcionario
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

    return [
        formatar_funcionario(
            banco,
            funcionario
        )
        for funcionario in funcionarios
    ]


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

    return formatar_funcionario(
        banco,
        funcionario
    )


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
        dados.aniversario,
        dados.estado_trabalho,
        dados.data_admissao
    )

    return {
        "mensagem": "Funcionário criado com sucesso",
        "funcionario": formatar_funcionario(
            banco,
            funcionario
        )
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
        dados.estado_trabalho,
        dados.data_admissao
    )

    return {
        "mensagem": "Funcionário atualizado",
        "funcionario": formatar_funcionario(
            banco,
            funcionario_atualizado
        )
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
