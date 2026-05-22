from sqlalchemy.orm import Session

from modelos import Funcionario


def buscar_funcionario_por_id(
    banco: Session,
    funcionario_id: int
):

    return banco.query(Funcionario).filter(
        Funcionario.id == funcionario_id
    ).first()


def listar_funcionarios(
    banco: Session
):

    return banco.query(Funcionario).all()


def criar_funcionario(
    banco: Session,
    nome: str,
    email: str,
    senha: str,
    cargo: str,
    tempo_casa: str,
    aniversario: str,
    estado_trabalho: str
):

    funcionario = Funcionario(
        nome=nome,
        email=email,
        senha=senha,
        cargo=cargo,
        tempo_casa=tempo_casa,
        aniversario=aniversario,

        # usa o valor enviado pelo Flutter
        estado_trabalho=estado_trabalho or "nao_comecou"
    )

    banco.add(funcionario)
    banco.commit()
    banco.refresh(funcionario)

    return funcionario


def buscar_funcionario_por_email(
    banco: Session,
    email: str
):

    return banco.query(Funcionario).filter(
        Funcionario.email == email
    ).first()


def alterar_funcionario(
    banco: Session,
    funcionario: Funcionario,
    nome: str,
    email: str,
    cargo: str,
    tempo_casa: str | None,
    aniversario: str | None,
    estado_trabalho: str
):

    funcionario.nome = nome
    funcionario.email = email
    funcionario.cargo = cargo
    funcionario.tempo_casa = tempo_casa
    funcionario.aniversario = aniversario
    funcionario.estado_trabalho = estado_trabalho

    banco.commit()
    banco.refresh(funcionario)

    return funcionario


def deletar_funcionario(
    banco: Session,
    funcionario: Funcionario
):

    banco.delete(funcionario)
    banco.commit()

    return True


def alterar_funcionario(
    banco: Session,
    funcionario: Funcionario,
    nome: str,
    email: str,
    cargo: str,
    tempo_casa: str | None,
    aniversario: str | None,
    estado_trabalho: str
):

    funcionario.nome = nome
    funcionario.email = email
    funcionario.cargo = cargo
    funcionario.tempo_casa = tempo_casa
    funcionario.aniversario = aniversario
    funcionario.estado_trabalho = estado_trabalho

    banco.commit()
    banco.refresh(funcionario)

    return funcionario


def deletar_funcionario(
    banco: Session,
    funcionario: Funcionario
):

    banco.delete(funcionario)
    banco.commit()

    return True
