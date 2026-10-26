from fastapi import APIRouter, HTTPException
from services import team_service
from services import player_x_teams_service
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
@router.get("/teams/{team_id}/players")
def get_team_players(team_id: int):

    return (
        player_x_teams_service
        .get_players_objects_by_team(team_id)
    )

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
