import os

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

DB_ENGINE = os.environ["DB_ENGINE"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


def get_connection(
    engine: str = DB_ENGINE,
    username: str = DB_USERNAME,
    password: str = DB_PASSWORD,
    host: str = DB_HOST,
    port: str = DB_PORT,
    database: str = DB_NAME,
) -> Engine:
    return create_engine(
        url=f"{engine}://{username}:{password}@{host}:{port}/{database}"
    )


engine = get_connection()
Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """This function is a generator of a db session."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
