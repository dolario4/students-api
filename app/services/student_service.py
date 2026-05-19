from fastapi import HTTPException, status
from sqlmodel import Session

from app.models.student import Student
from app.repositories import group_repository, student_repository
from app.schemas.student import StudentCreate, StudentTransfer


def create_student(session: Session, student_data: StudentCreate) -> Student:
    return student_repository.create_student(session, student_data)


def get_student_by_id(session: Session, student_id: int) -> Student:
    student = student_repository.get_student_by_id(session, student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return student


def get_students(session: Session) -> list[Student]:
    return student_repository.get_students(session)


def delete_student(session: Session, student_id: int) -> None:
    student = get_student_by_id(session, student_id)

    student_repository.delete_student(session, student)


def transfer_student(
    session: Session,
    student_id: int,
    transfer_data: StudentTransfer,
) -> Student:
    student = get_student_by_id(session, student_id)

    from_group = group_repository.get_group_by_id(
        session,
        transfer_data.from_group_id,
    )

    if from_group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Source group not found",
        )

    to_group = group_repository.get_group_by_id(
        session,
        transfer_data.to_group_id,
    )

    if to_group is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Target group not found",
        )

    if transfer_data.from_group_id == transfer_data.to_group_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Source and target groups must be different",
        )

    if student.group_id != transfer_data.from_group_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is not in the source group",
        )

    student.group_id = transfer_data.to_group_id

    return student_repository.save_student(session, student)
