from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Text
from datetime import datetime

from banco import Base
from sqlalchemy.orm import relationship


class Cargo(Base):
    __tablename__ = "cargos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    aniversario = Column(String, nullable=True)
    cargo_id = Column(Integer, ForeignKey("cargos.id"), nullable=False)
    data_admissao = Column(Date, nullable=True)

    cargo = relationship("Cargo")


class RegistroPonto(Base):
    __tablename__ = "registros_ponto"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    data_hora = Column(DateTime, default=datetime.now)
    tipo = Column(String, nullable=False)


class AjustePonto(Base):
    __tablename__ = "ajustes_ponto"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    motivo = Column(Text, nullable=False)
    status = Column(String, default="pendente")
    data_ajustada = Column(DateTime, nullable=True)

    horarios = relationship(
        "AjustePontoHorario",
        cascade="all, delete-orphan",
        back_populates="ajuste"
    )


class AjustePontoHorario(Base):
    __tablename__ = "ajustes_ponto_horarios"

    id = Column(Integer, primary_key=True, index=True)
    ajuste_ponto_id = Column(Integer, ForeignKey("ajustes_ponto.id"))
    tipo = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    ordem = Column(Integer, nullable=False)

    ajuste = relationship(
        "AjustePonto",
        back_populates="horarios"
    )


class SolicitacaoFerias(Base):
    __tablename__ = "solicitacoes_ferias"

    id = Column(Integer, primary_key=True, index=True)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    data_inicio = Column(String, nullable=False)
    data_fim = Column(String, nullable=False)
    status = Column(String, default="pendente")


class Conversa(Base):
    __tablename__ = "conversas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)


class Mensagem(Base):
    __tablename__ = "mensagens"

    id = Column(Integer, primary_key=True, index=True)
    conversa_id = Column(Integer, ForeignKey("conversas.id"))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    texto = Column(Text, nullable=False)
    data_hora = Column(DateTime, default=datetime.now)


class Notificacao(Base):
    __tablename__ = "notificacoes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    mensagem = Column(Text, nullable=False)
    data = Column(Text, nullable=True)

    destinatarios = relationship(
        "NotificacaoDestinatario",
        cascade="all, delete-orphan",
        back_populates="notificacao"
    )


class NotificacaoDestinatario(Base):
    __tablename__ = "notificacao_destinatarios"

    id = Column(Integer, primary_key=True, index=True)
    notificacao_id = Column(Integer, ForeignKey("notificacoes.id"))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"), nullable=True)
    lida = Column(Boolean, default=False, nullable=False)

    notificacao = relationship(
        "Notificacao",
        back_populates="destinatarios"
    )
