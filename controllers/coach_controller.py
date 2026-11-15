from fastapi import APIRouter, HTTPException
from services import coach_service
from typing import Optional
from security.jwt_service import get_current_user
from models.user import User
from fastapi import Depends


router = APIRouter(prefix="/coaches",)

@router.get("")
def get_coaches():
    return coach_service.get_coaches()

@router.get("/{coach_id}/team")
def get_current_team_of_coach(coach_id: int):
    try:
        return coach_service.get_current_team_of_coach(coach_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("")
def create_coach(coach: dict, current_user: User = Depends(get_current_user)):
    try:
        return coach_service.create_coach(coach)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{id_coach}")
def put_coach(id_coach: int, new_coach: dict, current_user: User = Depends(get_current_user)):
    try:
        return coach_service.put_coach(id_coach, new_coach)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id_coach}")
def patch_coach(
    id_coach: int,
    name: Optional[str] = None,
    current_user: User = Depends(get_current_user)
):
    try:
        return coach_service.patch_coach(id_coach, name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id_coach}")
def delete_coach(id_coach: int, current_user: User = Depends(get_current_user)):
    try:
        return coach_service.delete_coach(id_coach)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{coach_id}/teams/{new_team_id}")
def transfer_coach(coach_id: int, new_team_id: int, current_user: User = Depends(get_current_user)):
    try:
        return coach_service.transfer_coach(coach_id, new_team_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))