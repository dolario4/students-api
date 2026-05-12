from typing import Optional

from sqlmodel import SQLModel


class GroupCreate(SQLModel):
    name: str
    description: Optional[str] = None


class GroupRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None
