from sqlmodel import Session, select

from app.models.group import Group
from app.schemas.group import GroupCreate


def create_group(session: Session, group_data: GroupCreate) -> Group:
    group = Group(**group_data.model_dump())

    session.add(group)
    session.commit()
    session.refresh(group)

    return group


def get_group_by_id(session: Session, group_id: int) -> Group | None:
    return session.get(Group, group_id)


def get_groups(session: Session) -> list[Group]:
    statement = select(Group)
    return list(session.exec(statement).all())


def delete_group(session: Session, group: Group) -> None:
    session.delete(group)
    session.commit()
