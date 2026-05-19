from sqlmodel import SQLModel, create_engine, Session

from app.config import DATABASE_URL
from app.models.group import Group
from app.models.student import Student


engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
