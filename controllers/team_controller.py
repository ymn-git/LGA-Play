from fastapi import APIRouter
from typing import Optional
from fastapi import HTTPException
from services import team_service

router = APIRouter(
    prefix="/teams"
)

@router.get("")
def get_teams():
    return team_service.get_all_teams()

@router.get("/{id_team}")
def get_team_by_id(id_team: int):
    try:
        return team_service.get_team_by_id(id_team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("")
def create_team(team:dict):
    try:
        return team_service.create_team(team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{id_team}")
def update_team_name(id_team:int, new_name:str):
    try:
        return team_service.update_team_name(id_team, new_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{id_team}")
def delete_team(id_team:int):
    try:
        return team_service.delete_team(id_team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))