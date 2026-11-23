from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from models.user import User
from schemas.team_schema import TeamCreate, TeamUpdate
from security.jwt_service import get_current_user
from services import team_service, match_service

router = APIRouter(prefix="/teams")

@router.get("")
def get_teams(db: Session = Depends(get_db)):
    return team_service.get_all_teams(db)

@router.get("/{id_team}")
def get_team_by_id(id_team: int,db: Session = Depends(get_db)):
    try:
        return team_service.get_team_by_id(id_team,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/{team_id}/players")
def get_team_players(team_id: int,db: Session = Depends(get_db)):
    try:
        return team_service.get_players_objects_by_team(team_id,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/{team_id}/coaches")
def get_team_coaches(team_id: int,db: Session = Depends(get_db)):
    try:
        return team_service.get_coaches_objects_by_team(team_id,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.post("")
def create_team(team: TeamCreate,current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    try:
        return team_service.create_team(team,db)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.patch("/{id_team}")
def update_team_name(id_team: int,updated_team: TeamUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    try:
        return team_service.update_team_name(id_team,updated_team,db)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.delete("/{id_team}")
def delete_team(id_team: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)):
    try:
        return team_service.delete_team(id_team,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/{team_id}/stats")
def get_team_stats(team_id: int,season: int, db: Session = Depends(get_db)):
    try:
        return team_service.get_team_stats(team_id,season,db)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/standings")
def get_standings(season: int, db: Session = Depends(get_db)):
    return match_service.get_standings(db, season)
