from fastapi import APIRouter, HTTPException
from services import match_service
from schemas.match_schema import MatchResultUpdate, MatchCreate
from fastapi import Depends
from security.jwt_service import get_current_user
from models.user import User
from sqlalchemy.orm import Session
from schemas.playoff_schema import PlayoffMatchCreate, PenaltyResultUpdate


from app.database import get_db

router = APIRouter(prefix="/matches")
@router.post("", status_code=201)
def create_match(data: MatchCreate,current_user: User = Depends(get_current_user)):
    try:
        return match_service.create_match(
            data.season,
            data.matchday,
            data.team_a_id,
            data.team_b_id,
            data.full_date
        )
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.post("/playoffs", status_code=201)
def create_playoff(data: PlayoffMatchCreate, db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    try:
        match = match_service.create_playoff_match(
            db, data.season, data.phase, data.bracket_group, data.leg,
            data.team_a_id, data.team_b_id, data.full_date,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return match_service.with_score(match)

@router.patch("/playoffs/{match_id}/penalties")
def update_playoff_penalties(match_id: int,payload: PenaltyResultUpdate,
                             current_user: User = Depends(get_current_user)):
    try:
        return match_service.update_playoff_penalties(
            match_id,
            payload.penaltiesA,
            payload.penaltiesB
        )
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.get("/playoffs/{season}/{phase}/{bracket_group}")
def get_bracket(season: int, phase: str, bracket_group: int):
    matches = match_service.get_playoff_bracket(season,phase,bracket_group)
    if not matches:
        raise HTTPException(status_code=404, detail="Llave no encontrada")
    return [match_service.with_score(m) for m in matches]


@router.get("/matchday/{matchday}")
def get_matches_by_matchday(matchday: int, season: int):
    try:
        return match_service.get_matches_by_matchday(matchday, season)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/season/{season_id}/top-scorers")
def get_top_scorers(season_id: int):
    return match_service.get_top_scorers(season_id)

@router.patch("/{id_match}/result")
def update_match_result(id_match: int, payload: MatchResultUpdate, current_user: User = Depends(get_current_user)):
    try:
        return match_service.update_match_result(id_match, payload)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/standings/{season}")
def standings(season: int):
    return match_service.get_standings(season)

@router.get("/next")
def next_matches(season: int):
    try:
        return match_service.get_next_matches(season)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/qualified/{season}")
def qualified(season: int):
    return match_service.get_qualified(season)


@router.get("/{id_match}") #/{id} declarado a lo ultimo porque FastApi toma el orden en cascada
def get_match_result(id_match: int):
    try:
        return match_service.get_match_result(id_match)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


