from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from datetime import datetime

from banco import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    cargo = Column(String, nullable=False)
    tempo_casa = Column(String, nullable=True)
    aniversario = Column(String, nullable=True)
    estado_trabalho = Column(String, default="nao_comecou")


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
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    titulo = Column(String, nullable=False)
    mensagem = Column(Text, nullable=False)
    lida = Column(Boolean, default=False)