from datetime import date, datetime

from sqlalchemy.orm import Session

from modelos import Cargo, Funcionario, RegistroPonto


def _normalizar_data(valor: str | None):
    if not valor:
        return None

    valor = valor.strip()

    for formato in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(valor, formato).date()
        except ValueError:
            pass

    return None


def _buscar_ou_criar_cargo(
    banco: Session,
    nome: str
):
    nome_cargo = (nome or "Funcionario").strip() or "Funcionario"

    cargo = banco.query(Cargo).filter(
        Cargo.nome == nome_cargo
    ).first()

    if cargo is not None:
        return cargo

    cargo = Cargo(nome=nome_cargo)
    banco.add(cargo)
    banco.flush()

    return cargo


def _calcular_tempo_casa(data_admissao):
    if data_admissao is None:
        return None

    hoje = date.today()

    if data_admissao > hoje:
        return "0 dias"

    anos = hoje.year - data_admissao.year
    meses = hoje.month - data_admissao.month
    dias = hoje.day - data_admissao.day

    if dias < 0:
        meses -= 1

    if meses < 0:
        anos -= 1
        meses += 12

    if anos > 0:
        return f"{anos} ano" if anos == 1 else f"{anos} anos"

    if meses > 0:
        return f"{meses} mes" if meses == 1 else f"{meses} meses"

    diferenca_dias = (hoje - data_admissao).days

    return f"{diferenca_dias} dia" if diferenca_dias == 1 else f"{diferenca_dias} dias"


def obter_estado_trabalho(
    banco: Session,
    funcionario_id: int
):
    ultimo_ponto = banco.query(RegistroPonto).filter(
        RegistroPonto.funcionario_id == funcionario_id
    ).order_by(
        RegistroPonto.data_hora.desc()
    ).first()

    if ultimo_ponto is None:
        return "nao_comecou"

    tipo = (ultimo_ponto.tipo or "").lower()

    if tipo == "entrada":
        return "Trabalhando"

    if tipo == "saida":
        return "Ausente"

    if tipo == "falta":
        return "Falta"

    if tipo == "ferias":
        return "Ferias"

    return ultimo_ponto.tipo


def formatar_funcionario(
    banco: Session,
    funcionario: Funcionario
):
    cargo_nome = funcionario.cargo.nome if funcionario.cargo is not None else None
    data_admissao = (
        funcionario.data_admissao.isoformat()
        if funcionario.data_admissao is not None
        else None
    )

    return {
        "id": funcionario.id,
        "nome": funcionario.nome,
        "email": funcionario.email,
        "cargo": cargo_nome,
        "data_admissao": data_admissao,
        "tempo_casa": _calcular_tempo_casa(funcionario.data_admissao),
        "aniversario": funcionario.aniversario,
        "estado_trabalho": obter_estado_trabalho(
            banco,
            funcionario.id
        )
    }


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
    tempo_casa: str | None,
    aniversario: str,
    estado_trabalho: str | None = None,
    data_admissao: str | None = None
):
    cargo_entidade = _buscar_ou_criar_cargo(
        banco,
        cargo
    )

    funcionario = Funcionario(
        nome=nome,
        email=email,
        senha=senha,
        cargo_id=cargo_entidade.id,
        data_admissao=_normalizar_data(data_admissao or tempo_casa),
        aniversario=aniversario
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
    estado_trabalho: str | None = None,
    data_admissao: str | None = None
):
    cargo_entidade = _buscar_ou_criar_cargo(
        banco,
        cargo
    )

    funcionario.nome = nome
    funcionario.email = email
    funcionario.cargo_id = cargo_entidade.id
    funcionario.data_admissao = _normalizar_data(data_admissao or tempo_casa)
    funcionario.aniversario = aniversario

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
