from sqlmodel import Session, select

from app.models.student import Student
from app.schemas.student import StudentCreate


def create_student(session: Session, student_data: StudentCreate) -> Student:
    student = Student(**student_data.model_dump())

    session.add(student)
    session.commit()
    session.refresh(student)

    return student


def get_student_by_id(session: Session, student_id: int) -> Student | None:
    return session.get(Student, student_id)


def get_students(session: Session) -> list[Student]:
    statement = select(Student)
    return list(session.exec(statement).all())


def get_students_by_group_id(session: Session, group_id: int) -> list[Student]:
    statement = select(Student).where(Student.group_id == group_id)
    return list(session.exec(statement).all())


def save_student(session: Session, student: Student) -> Student:
    session.add(student)
    session.commit()
    session.refresh(student)

    return student


def delete_student(session: Session, student: Student) -> None:
    session.delete(student)
    session.commit()
