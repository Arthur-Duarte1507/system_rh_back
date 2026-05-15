# Sistema RH Backend

Backend de um sistema de RH desenvolvido com FastAPI + PostgreSQL para integração com aplicação Flutter.

## Tecnologias utilizadas

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/Arthur-Duarte1507/system_rh_back.git
```

---

## 2. Entrar na pasta

```bash
cd system_rh_back
```

---

## 3. Executar o iniciar.bat

No Windows:

```text
Clique duas vezes no arquivo iniciar.bat
```

OU execute:

```bash
iniciar.bat
```

O sistema irá:

- criar ambiente virtual
- instalar dependências
- iniciar a API automaticamente

---

# Swagger

Após iniciar:

```text
http://127.0.0.1:8000/docs
```

---

# Estrutura do projeto

```text
rotas/
repositorios/
modelos.py
esquemas.py
banco.py
principal.py
```

---

# Endpoints principais

## Autenticação

```text
/api/auth/login
/api/auth/logout
/api/auth/me
```

## Funcionários

```text
GET /api/funcionarios
POST /api/funcionarios
PUT /api/funcionarios/{id}
DELETE /api/funcionarios/{id}
```

## Ponto

```text
POST /api/ponto/bater
GET /api/ponto/historico/{funcionario_id}
GET /api/ponto/status/{funcionario_id}
GET /api/ponto/hoje/{funcionario_id}
```

## Ajustes

```text
POST /api/ajustes-ponto
GET /api/ajustes-ponto
GET /api/ajustes-ponto/{id}
```

## Férias

```text
GET /api/ferias
POST /api/ferias/solicitar
```

## Chat

```text
POST /api/chat/conversas
GET /api/chat/conversas
POST /api/chat/mensagem
GET /api/chat/conversas/{id}/mensagens
```

## Notificações

```text
POST /api/notificacoes
GET /api/notificacoes
PUT /api/notificacoes/{id}/lida
DELETE /api/notificacoes/{id}
```

## Banco de horas

```text
GET /api/banco-horas/resumo/{funcionario_id}
GET /api/banco-horas/extrato/{funcionario_id}
```

## Dashboard

```text
GET /api/dashboard/{funcionario_id}
```

---

# Integração com Flutter

A API retorna dados em JSON e pode ser consumida normalmente por aplicações Flutter através de requisições HTTP.

Exemplo:

```dart
final response = await http.get(
  Uri.parse("http://IP_DA_API:8000/api/funcionarios"),
);
```

---

# Observações

- Necessário possuir Python instalado
- Necessário possuir PostgreSQL instalado
- Banco configurado em `banco.py`
