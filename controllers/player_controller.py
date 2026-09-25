from fastapi import APIRouter
from fastapi import HTTPException
from typing import Optional
from services import player_service

router = APIRouter(
    prefix="/players"
)

@router.get("")
def get_players():
    return player_service.get_players()


@router.get("/{id_player}")
def get_player_by_id(id_player: int):
    try:
        return player_service.get_player_by_id(id_player)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

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
def patch_player(id_player: int,
                 name: Optional[str] = None,
                 position: Optional[str] = None,
                 active: Optional[bool] = None):
    try:
        return player_service.patch_player(id_player, name, position, active)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id_player}")
def delete_player(id_player:int):
    try:
        return player_service.delete_player(id_player)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))