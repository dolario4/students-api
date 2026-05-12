from typing import Optional

from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    __tablename__ = "students"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int
    email: str = Field(index=True)
    group_id: Optional[int] = Field(default=None, foreign_key="groups.id")
