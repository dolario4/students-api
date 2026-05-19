from typing import Optional
from sqlmodel import SQLModel

class StudentCreate(SQLModel):
    first_name: str
    last_name: str
    age: int
    email: str

class StudentRead(SQLModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str
    group_id: Optional[int] = None


class StudentTransfer(SQLModel):
    from_group_id: int
    to_group_id: int
