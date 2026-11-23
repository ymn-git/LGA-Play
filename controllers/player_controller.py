from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from services import player_service
from security.jwt_service import get_current_user
from models.user import User
from schemas.player_schema import (
    PlayerCreate,
    PlayerUpdate
)

router = APIRouter(prefix="/players")

@router.get("")
def get_players(db: Session = Depends(get_db)):
    return player_service.get_players(db)

@router.get("/{player_id}/stats")
def get_player_stats(player_id: int,season: Optional[int] = None,db: Session = Depends(get_db)):
    try:
        return player_service.get_player_stats(player_id,db,season)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/{player_id}/team")
def get_current_team_of_player(
    player_id: int,
    db: Session = Depends(get_db)
):
    try:
        return player_service.get_current_team_of_player(player_id,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.post("")
def create_player(
    player: PlayerCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return player_service.create_player(player,db)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.put("/{id_player}")
def put_player(
    id_player: int,
    new_player: PlayerUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return player_service.put_player(id_player,new_player,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.patch("/{id_player}")
def patch_player(
    id_player: int,
    name: Optional[str] = None,
    position: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return player_service.patch_player(id_player,name,position,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.delete("/{id_player}")
def delete_player(
    id_player: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return player_service.delete_player(id_player,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.patch("/{player_id}/teams/{new_team_id}")
def transfer_player(
    player_id: int,
    new_team_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return player_service.transfer_player(player_id,new_team_id,db)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))