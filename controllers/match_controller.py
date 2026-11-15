from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from services import match_service, match_x_fase_service
from schemas.match_schema import MatchResultUpdate
from schemas.match_x_fase_schema import (
    RegularMatchCreate,
    PlayoffMatchCreate,
    PlayoffResultUpdate
)
from security.jwt_service import get_current_user
from models.user import User

router = APIRouter(prefix="/matches")

# 1. Obtener todos los partidos
@router.get("")
def get_matches(season: int = 2026, db: Session = Depends(get_db)):
    matches_db = match_x_fase_service.get_all_regular_matches(db, season)
    if matches_db:
        return matches_db
    try:
        return match_service.get_matches_by_matchday(1, season)
    except Exception:
        return []

# 2. Obtener partidos de Playoffs por temporada
@router.get("/playoffs")
def get_playoff_matches(season: int = 2026, db: Session = Depends(get_db)):
    return match_x_fase_service.get_playoff_matches(db, season)

# 3. Crear partido de Fase Regular (tabla intermedia match_x_fase)
@router.post("/regular")
def create_regular_match(payload: RegularMatchCreate, db: Session = Depends(get_db)):
    try:
        return match_x_fase_service.create_regular_match(db, payload.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# 4. Crear partido de Playoffs (tabla intermedia match_x_fase)
@router.post("/playoffs")
def create_playoff_match(payload: PlayoffMatchCreate, db: Session = Depends(get_db)):
    try:
        return match_x_fase_service.create_playoff_match(db, payload.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# 5. Actualizar resultado de partido de Playoff (penales + clasificado)
@router.patch("/playoffs/{id_match}/result")
def update_playoff_result(
    id_match: int,
    payload: PlayoffResultUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return match_x_fase_service.update_playoff_result(db, id_match, payload.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# 6. Partidos por fecha
@router.get("/matchday/{matchday}")
def get_matches_by_matchday(matchday: int, season: int = 2026, db: Session = Depends(get_db)):
    matches_db = match_x_fase_service.get_regular_matches_by_matchday(db, matchday, season)
    if matches_db:
        return matches_db
    return match_service.get_matches_by_matchday(matchday, season)

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

@router.get("/{id_match}")
def get_match_result(id_match: int):
    try:
        return match_service.get_match_result(id_match)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
