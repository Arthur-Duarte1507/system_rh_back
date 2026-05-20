from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


URL_BANCO = "postgresql://postgres:1234@localhost:5432/rh_api"


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
