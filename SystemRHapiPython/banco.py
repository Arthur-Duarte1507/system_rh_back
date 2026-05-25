import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

URL_BANCO = os.getenv("URL_BANCO") or os.getenv("DATABASE_URL")
if not URL_BANCO:
    raise RuntimeError("Defina URL_BANCO (ou DATABASE_URL) no arquivo .env.")


engine = create_engine(URL_BANCO)


SessaoLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def pegar_banco():

    banco = SessaoLocal()

    try:
        yield banco

    finally:
        banco.close()
