# System RH API Java

Guia rapido para subir a API Java em WSL/Linux, Windows e macOS.

## Requisitos

- Java 17 instalado
- PostgreSQL rodando
- Banco existente (exemplo: `rh_api`)

## Variaveis de ambiente usadas pela API

A aplicacao le essas variaveis:

- `DB_URL` (ex.: `jdbc:postgresql://localhost:5432/rh_api`)
- `DB_USER` (ex.: `postgres`)
- `DB_PASS` (ex.: `123456`)
- `SERVER_PORT` (opcional, padrao: `8080`)

## 1) WSL / Linux

No terminal, dentro da pasta `systemRhApiJava`:

```bash
cd /caminho/para/systemRhApiJava

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

export DB_URL='jdbc:postgresql://localhost:5432/rh_api'
export DB_USER='postgres'
export DB_PASS='123456'
export SERVER_PORT='8081'   # opcional

sh mvnw spring-boot:run
```

## 2) Windows (PowerShell)

No PowerShell, dentro da pasta `systemRhApiJava`:

```powershell
cd C:\caminho\para\systemRhApiJava

$env:DB_URL="jdbc:postgresql://localhost:5432/rh_api"
$env:DB_USER="postgres"
$env:DB_PASS="123456"
$env:SERVER_PORT="8081"   # opcional

.\mvnw.cmd spring-boot:run
```

## 3) Windows (CMD)

No Prompt de Comando (CMD), dentro da pasta `systemRhApiJava`:

```cmd
cd C:\caminho\para\systemRhApiJava

set DB_URL=jdbc:postgresql://localhost:5432/rh_api
set DB_USER=postgres
set DB_PASS=123456
set SERVER_PORT=8081

mvnw.cmd spring-boot:run
```

## 4) macOS

No terminal, dentro da pasta `systemRhApiJava`:

```bash
cd /caminho/para/systemRhApiJava

export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH=$JAVA_HOME/bin:$PATH

export DB_URL='jdbc:postgresql://localhost:5432/rh_api'
export DB_USER='postgres'
export DB_PASS='123456'
export SERVER_PORT='8081'   # opcional

./mvnw spring-boot:run
```

Se der `permission denied` no `./mvnw`:

```bash
chmod +x mvnw
./mvnw spring-boot:run
```

## Teste rapido

Com a API no ar:

- URL: `http://localhost:8081/api/teste` (ou porta que voce definiu)
- Resposta esperada: `FUNFANDO`

## Erros comuns

### 1) Porta em uso

Erro: `Port 8080 is already in use`.

Solucao: use outra porta, por exemplo:

- Linux/macOS: `export SERVER_PORT=8081`
- PowerShell: `$env:SERVER_PORT="8081"`
- CMD: `set SERVER_PORT=8081`

### 2) Java errado (Java 8)

Erro semelhante: `class file has wrong version 61.0, should be 52.0`.

Solucao: usar Java 17 no terminal atual (`JAVA_HOME` + `PATH`).

### 3) Variavel de banco ausente

Se `DB_URL`, `DB_USER` ou `DB_PASS` nao estiverem definidas, a API nao conecta no banco.

