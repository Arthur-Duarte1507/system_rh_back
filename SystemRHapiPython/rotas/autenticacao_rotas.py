from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import LoginRequisicao

from repositorios.funcionario_repositorio import (
    buscar_funcionario_por_email,
    formatar_funcionario
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Autenticação"]
)


@router.post("/login")
def login(
    dados: LoginRequisicao,
    banco: Session = Depends(pegar_banco)
):

    funcionario = buscar_funcionario_por_email(
        banco,
        dados.email
    )

    if funcionario is None:

        return {
            "erro": "Usuário não encontrado"
        }

    if funcionario.senha != dados.senha:

        return {
            "erro": "Senha inválida"
        }

    usuario = formatar_funcionario(
        banco,
        funcionario
    )

    return {
        "mensagem": "Login realizado com sucesso",

        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"],
            "cargo": usuario["cargo"]
        }
    }


@router.post("/logout")
def logout():

    return {
        "mensagem": "Logout realizado"
    }


@router.get("/me")
def usuario_logado():

    return {
        "nome": "Usuário logado",
        "cargo": "Funcionário"
    }
