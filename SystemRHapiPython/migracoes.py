from sqlalchemy import text

from banco import engine


def _coluna_existe(conexao, tabela: str, coluna: str) -> bool:
    resultado = conexao.execute(
        text(
            """
            SELECT 1
            FROM information_schema.columns
            WHERE table_schema = current_schema()
              AND table_name = :tabela
              AND column_name = :coluna
            """
        ),
        {
            "tabela": tabela,
            "coluna": coluna
        }
    ).first()

    return resultado is not None


def _migrar_funcionarios(conexao):
    conexao.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS cargos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR NOT NULL UNIQUE
            )
            """
        )
    )

    conexao.execute(
        text(
            """
            ALTER TABLE funcionarios
            ADD COLUMN IF NOT EXISTS cargo_id INTEGER
            """
        )
    )

    conexao.execute(
        text(
            """
            ALTER TABLE funcionarios
            ADD COLUMN IF NOT EXISTS data_admissao DATE
            """
        )
    )

    if _coluna_existe(conexao, "funcionarios", "cargo"):
        conexao.execute(
            text(
                """
                INSERT INTO cargos (nome)
                SELECT DISTINCT NULLIF(TRIM(cargo), '')
                FROM funcionarios
                WHERE NULLIF(TRIM(cargo), '') IS NOT NULL
                ON CONFLICT (nome) DO NOTHING
                """
            )
        )

        conexao.execute(
            text(
                """
                UPDATE funcionarios AS f
                SET cargo_id = c.id
                FROM cargos AS c
                WHERE f.cargo_id IS NULL
                  AND c.nome = f.cargo
                """
            )
        )

    conexao.execute(
        text(
            """
            INSERT INTO cargos (nome)
            VALUES ('Funcionario')
            ON CONFLICT (nome) DO NOTHING
            """
        )
    )

    conexao.execute(
        text(
            """
            UPDATE funcionarios
            SET cargo_id = (
                SELECT id
                FROM cargos
                WHERE nome = 'Funcionario'
                LIMIT 1
            )
            WHERE cargo_id IS NULL
            """
        )
    )

    if _coluna_existe(conexao, "funcionarios", "tempo_casa"):
        conexao.execute(
            text(
                """
                UPDATE funcionarios
                SET data_admissao = to_date(tempo_casa, 'YYYY-MM-DD')
                WHERE data_admissao IS NULL
                  AND tempo_casa ~ '^\\d{4}-\\d{2}-\\d{2}$'
                """
            )
        )

        conexao.execute(
            text(
                """
                UPDATE funcionarios
                SET data_admissao = to_date(tempo_casa, 'DD/MM/YYYY')
                WHERE data_admissao IS NULL
                  AND tempo_casa ~ '^\\d{2}/\\d{2}/\\d{4}$'
                """
            )
        )

    conexao.execute(
        text(
            """
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT 1
                    FROM pg_constraint
                    WHERE conname = 'fk_funcionarios_cargo'
                ) THEN
                    ALTER TABLE funcionarios
                    ADD CONSTRAINT fk_funcionarios_cargo
                    FOREIGN KEY (cargo_id) REFERENCES cargos(id);
                END IF;
            END $$;
            """
        )
    )

    conexao.execute(
        text(
            """
            ALTER TABLE funcionarios
            ALTER COLUMN cargo_id SET NOT NULL
            """
        )
    )

    conexao.execute(text("ALTER TABLE funcionarios DROP COLUMN IF EXISTS cargo"))
    conexao.execute(text("ALTER TABLE funcionarios DROP COLUMN IF EXISTS tempo_casa"))
    conexao.execute(text("ALTER TABLE funcionarios DROP COLUMN IF EXISTS estado_trabalho"))


def _migrar_ajustes_ponto(conexao):
    conexao.execute(
        text(
            """
            ALTER TABLE ajustes_ponto
            ADD COLUMN IF NOT EXISTS data_ajustada TIMESTAMP
            """
        )
    )

    conexao.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS ajustes_ponto_horarios (
                id SERIAL PRIMARY KEY,
                ajuste_ponto_id INTEGER NOT NULL
                    REFERENCES ajustes_ponto(id) ON DELETE CASCADE,
                tipo VARCHAR NOT NULL,
                horario VARCHAR NOT NULL,
                ordem INTEGER NOT NULL,
                UNIQUE (ajuste_ponto_id, ordem)
            )
            """
        )
    )

    colunas_horario = [
        ("hora_inicial", "hora_inicial", 1),
        ("intervalo_inicial", "intervalo_inicial", 2),
        ("intervalo_final", "intervalo_final", 3),
        ("hora_final", "hora_final", 4),
    ]

    for coluna, tipo, ordem in colunas_horario:
        if not _coluna_existe(conexao, "ajustes_ponto", coluna):
            continue

        conexao.execute(
            text(
                f"""
                INSERT INTO ajustes_ponto_horarios (
                    ajuste_ponto_id,
                    tipo,
                    horario,
                    ordem
                )
                SELECT id, :tipo, {coluna}, :ordem
                FROM ajustes_ponto AS a
                WHERE {coluna} IS NOT NULL
                  AND NULLIF(TRIM({coluna}), '') IS NOT NULL
                  AND NOT EXISTS (
                      SELECT 1
                      FROM ajustes_ponto_horarios AS h
                      WHERE h.ajuste_ponto_id = a.id
                        AND h.tipo = :tipo
                  )
                """
            ),
            {
                "tipo": tipo,
                "ordem": ordem
            }
        )

    conexao.execute(text("ALTER TABLE ajustes_ponto DROP COLUMN IF EXISTS hora_inicial"))
    conexao.execute(text("ALTER TABLE ajustes_ponto DROP COLUMN IF EXISTS intervalo_inicial"))
    conexao.execute(text("ALTER TABLE ajustes_ponto DROP COLUMN IF EXISTS intervalo_final"))
    conexao.execute(text("ALTER TABLE ajustes_ponto DROP COLUMN IF EXISTS hora_final"))


def _migrar_notificacoes(conexao):
    conexao.execute(
        text(
            """
            ALTER TABLE notificacoes
            ADD COLUMN IF NOT EXISTS data TEXT
            """
        )
    )

    conexao.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS notificacao_destinatarios (
                id SERIAL PRIMARY KEY,
                notificacao_id INTEGER NOT NULL
                    REFERENCES notificacoes(id) ON DELETE CASCADE,
                funcionario_id INTEGER NULL
                    REFERENCES funcionarios(id),
                lida BOOLEAN NOT NULL DEFAULT FALSE
            )
            """
        )
    )

    conexao.execute(
        text(
            """
            CREATE INDEX IF NOT EXISTS idx_notificacao_destinatarios_notificacao
            ON notificacao_destinatarios (notificacao_id)
            """
        )
    )

    conexao.execute(
        text(
            """
            CREATE INDEX IF NOT EXISTS idx_notificacao_destinatarios_funcionario
            ON notificacao_destinatarios (funcionario_id)
            """
        )
    )

    if _coluna_existe(conexao, "notificacoes", "funcionario_id"):
        lida_sql = "COALESCE(n.lida, FALSE)" if _coluna_existe(
            conexao,
            "notificacoes",
            "lida"
        ) else "FALSE"

        conexao.execute(
            text(
                f"""
                INSERT INTO notificacao_destinatarios (
                    notificacao_id,
                    funcionario_id,
                    lida
                )
                SELECT
                    n.id,
                    CASE
                        WHEN n.funcionario_id = 0 THEN NULL
                        ELSE n.funcionario_id
                    END,
                    {lida_sql}
                FROM notificacoes AS n
                WHERE (
                    n.funcionario_id IS NULL
                    OR n.funcionario_id = 0
                    OR EXISTS (
                        SELECT 1
                        FROM funcionarios AS f
                        WHERE f.id = n.funcionario_id
                    )
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM notificacao_destinatarios AS d
                    WHERE d.notificacao_id = n.id
                      AND d.funcionario_id IS NOT DISTINCT FROM
                          CASE
                              WHEN n.funcionario_id = 0 THEN NULL
                              ELSE n.funcionario_id
                          END
                )
                """
            )
        )

    conexao.execute(text("ALTER TABLE notificacoes DROP COLUMN IF EXISTS funcionario_id"))
    conexao.execute(text("ALTER TABLE notificacoes DROP COLUMN IF EXISTS lida"))


def aplicar_migracoes():
    with engine.begin() as conexao:
        _migrar_funcionarios(conexao)
        _migrar_ajustes_ponto(conexao)
        _migrar_notificacoes(conexao)
