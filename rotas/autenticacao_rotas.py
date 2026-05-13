from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from banco import pegar_banco

from esquemas import LoginRequisicao

from repositorios.funcionario_repositorio import (
    buscar_funcionario_por_email
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

    return {
        "mensagem": "Login realizado com sucesso",

        "usuario": {
            "id": funcionario.id,
            "nome": funcionario.nome,
            "email": funcionario.email,
            "cargo": funcionario.cargo
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