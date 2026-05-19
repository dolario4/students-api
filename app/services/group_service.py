from fastapi import HTTPException, status
from sqlmodel import Session

from app.models.group import Group
from app.models.student import Student
from app.repositories import group_repository, student_repository
from app.schemas.group import GroupCreate


def create_group(session: Session, group_data: GroupCreate) -> Group:
    return group_repository.create_group(session, group_data)


def get_group_by_id(session: Session, group_id: int) -> Group:
    group = group_repository.get_group_by_id(session, group_id)

    if group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Group not found",
        )

    return group


def get_groups(session: Session) -> list[Group]:
    return group_repository.get_groups(session)


def delete_group(session: Session, group_id: int) -> None:
    group = get_group_by_id(session, group_id)

    group_repository.delete_group(session, group)


def add_student_to_group(
    session: Session,
    group_id: int,
    student_id: int,
) -> Student:
    group = get_group_by_id(session, group_id)

    student = student_repository.get_student_by_id(session, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    if student.group_id == group.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is already in this group",
        )

    student.group_id = group.id

    return student_repository.save_student(session, student)


def remove_student_from_group(
    session: Session,
    group_id: int,
    student_id: int,
) -> Student:
    group = get_group_by_id(session, group_id)

    student = student_repository.get_student_by_id(session, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    if student.group_id != group.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is not in this group",
        )

    student.group_id = None

    return student_repository.save_student(session, student)


def get_students_in_group(session: Session, group_id: int) -> list[Student]:
    get_group_by_id(session, group_id)

    return student_repository.get_students_by_group_id(session, group_id)
