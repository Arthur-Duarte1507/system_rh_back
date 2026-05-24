from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")

print(f"postgresql://{DB_USER}:{DB_PASS}@localhost:{DB_PORT}/rh_api")
URL_BANCO = f"postgresql://{DB_USER}:{DB_PASS}@localhost:{DB_PORT}/rh_api"


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
