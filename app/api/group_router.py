from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.database import get_session
from app.schemas.group import GroupCreate, GroupRead
from app.schemas.student import StudentRead
from app.services import group_service


router = APIRouter(
    prefix="/groups",
    tags=["Groups"],
)


@router.post(
    "",
    response_model=GroupRead,
    status_code=status.HTTP_201_CREATED,
)
def create_group(
    group_data: GroupCreate,
    session: Session = Depends(get_session),
):
    return group_service.create_group(session, group_data)


@router.get(
    "",
    response_model=list[GroupRead],
)
def get_groups(
    session: Session = Depends(get_session),
):
    return group_service.get_groups(session)


@router.get(
    "/{group_id}",
    response_model=GroupRead,
)
def get_group_by_id(
    group_id: int,
    session: Session = Depends(get_session),
):
    return group_service.get_group_by_id(session, group_id)


@router.delete(
    "/{group_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_group(
    group_id: int,
    session: Session = Depends(get_session),
):
    group_service.delete_group(session, group_id)


@router.post(
    "/{group_id}/students/{student_id}",
    response_model=StudentRead,
)
def add_student_to_group(
    group_id: int,
    student_id: int,
    session: Session = Depends(get_session),
):
    return group_service.add_student_to_group(
        session,
        group_id,
        student_id,
    )


@router.delete(
    "/{group_id}/students/{student_id}",
    response_model=StudentRead,
)
def remove_student_from_group(
    group_id: int,
    student_id: int,
    session: Session = Depends(get_session),
):
    return group_service.remove_student_from_group(
        session,
        group_id,
        student_id,
    )


@router.get(
    "/{group_id}/students",
    response_model=list[StudentRead],
)
def get_students_in_group(
    group_id: int,
    session: Session = Depends(get_session),
):
    return group_service.get_students_in_group(session, group_id)
