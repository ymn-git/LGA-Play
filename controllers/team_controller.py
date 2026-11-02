from fastapi import APIRouter, HTTPException
from services import team_service
router = APIRouter(prefix="/teams")

@router.get("")
def get_teams():
    return team_service.get_all_teams()

@router.get("/standings")
def get_standings():
    try:
        return team_service.get_standings()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{id_team}")
def get_team_by_id(id_team: int):
    try:
        return team_service.get_team_by_id(id_team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

#devuelve el plantel completo
@router.get("/{team_id}/players")
def get_team_players(team_id: int):
    return team_service.get_players_objects_by_team(team_id)

@router.get("/teams/{team_id}/coaches")
def get_team_coach(team_id: int):
    try:
        return team_service.get_coaches_objects_by_team(team_id)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.post("/{team_id}/players/{player_id}")
def assign_player_to_team(team_id: int,player_id: int):
    try:
        return team_service.assign_player_to_team(team_id,player_id)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.post("/teams/{team_id}/coaches/{coach_id}")
def assign_coach_to_team(team_id: int,coach_id: int):
    try:
        return team_service.assign_coach_to_team(coach_id,team_id)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.post("")
def create_team(team: dict):
    try:
        return team_service.create_team(team)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{id_team}")
def update_team_name(id_team: int, new_name: str):
    try:
        return team_service.update_team_name(id_team, new_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id_team}")
def delete_team(id_team: int):
    try:
        return team_service.delete_team(id_team)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
