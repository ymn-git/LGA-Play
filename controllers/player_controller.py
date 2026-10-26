from fastapi import APIRouter
from fastapi import HTTPException
from typing import Optional
from services import player_service
from services import player_x_teams_service

router = APIRouter(prefix="/players")

@router.get("")
def get_players():
    return player_service.get_players()

@router.get("/{player_id}/team")
def get_current_team_of_player(player_id: int):
    return player_x_teams_service.get_current_team_of_player(player_id)

@router.post("")
def create_player(player:dict):
    try:
        return player_service.create_player(player)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{id_player}")
def put_player(id_player:int, new_player:dict):
    try:
        return player_service.put_player(id_player, new_player)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id_player}")
def patch_player(id_player: int,name: Optional[str] = None,position: Optional[str] = None):
    try:
        return player_service.patch_player(id_player,name,position)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id_player}")
def delete_player(id_player:int):
    try:
        return player_service.delete_player(id_player)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/players/{player_id}/team")
def get_current_team_of_player(player_id: int):
    return (player_x_teams_service.get_current_team_of_player(player_id))