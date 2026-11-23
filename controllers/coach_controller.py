from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from services import coach_service

from security.jwt_service import get_current_user
from models.user import User

from schemas.coach_schema import (
    CoachCreate,
    CoachUpdate
)

router = APIRouter(
    prefix="/coaches"
)


@router.get("")
def get_coaches(
    db: Session = Depends(get_db)
):
    return coach_service.get_coaches(
        db
    )


@router.get("/{coach_id}/team")
def get_current_team_of_coach(
    coach_id: int,
    db: Session = Depends(get_db)
):
    try:

        return coach_service.get_current_team_of_coach(
            coach_id,
            db
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.post("")
def create_coach(
    coach: CoachCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        return coach_service.create_coach(
            coach,
            db
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.put("/{id_coach}")
def put_coach(
    id_coach: int,
    new_coach: CoachUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        return coach_service.put_coach(
            id_coach,
            new_coach,
            db
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.patch("/{id_coach}")
def patch_coach(
    id_coach: int,
    name: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        return coach_service.patch_coach(
            id_coach,
            name,
            db
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete("/{id_coach}")
def delete_coach(
    id_coach: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        return coach_service.delete_coach(
            id_coach,
            db
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.patch("/{coach_id}/teams/{new_team_id}")
def transfer_coach(
    coach_id: int,
    new_team_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        return coach_service.transfer_coach(
            coach_id,
            new_team_id,
            db
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )