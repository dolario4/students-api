from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.database import get_session
from app.schemas.student import StudentCreate, StudentRead, StudentTransfer
from app.services import student_service


router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "",
    response_model=StudentRead,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student_data: StudentCreate,
    session: Session = Depends(get_session),
):
    return student_service.create_student(session, student_data)


@router.get(
    "",
    response_model=list[StudentRead],
)
def get_students(
    session: Session = Depends(get_session),
):
    return student_service.get_students(session)


@router.get(
    "/{student_id}",
    response_model=StudentRead,
)
def get_student_by_id(
    student_id: int,
    session: Session = Depends(get_session),
):
    return student_service.get_student_by_id(session, student_id)


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(
    student_id: int,
    session: Session = Depends(get_session),
):
    student_service.delete_student(session, student_id)


@router.post(
    "/{student_id}/transfer",
    response_model=StudentRead,
)
def transfer_student(
    student_id: int,
    transfer_data: StudentTransfer,
    session: Session = Depends(get_session),
):
    return student_service.transfer_student(
        session,
        student_id,
        transfer_data,
    )
