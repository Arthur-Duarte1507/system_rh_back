from pydantic import BaseModel


class LoginRequisicao(BaseModel):
    email: str
    senha: str


class FuncionarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    tempo_casa: str | None
    aniversario: str | None
    estado_trabalho: str


class BaterPontoRequisicao(BaseModel):
    funcionario_id: int
    tipo: str


class AjustePontoRequisicao(BaseModel):
    funcionario_id: int
    motivo: str


class FeriasRequisicao(BaseModel):
    funcionario_id: int
    data_inicio: str
    data_fim: str


class MensagemRequisicao(BaseModel):
    conversa_id: int
    funcionario_id: int
    texto: str


class RespostaMensagem(BaseModel):
    mensagem: str


class CriarFuncionarioRequisicao(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: str
    tempo_casa: str
    aniversario: str
    estado_trabalho: str | None = None


class AlterarFuncionarioRequisicao(BaseModel):
    nome: str
    email: str
    cargo: str
    tempo_casa: str | None = None
    aniversario: str | None = None
    estado_trabalho: str


class ConversaRequisicao(BaseModel):
    titulo: str


class NotificacaoRequisicao(BaseModel):
    funcionario_id: int
    titulo: str
    mensagem: str
