from fastapi import APIRouter, HTTPException
from datetime import date
from services import match_service

router = APIRouter(prefix="/matchs")

@router.get("/")
def get_matches():
    return match_service.get_matches()

@router.get("/{id_match}")
def get_match_result(id_match: int):
    try:
        return match_service.get_match_result(id_match)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/matchday/{season}/{matchday}")
def get_matches_by_matchday(season: int, matchday: int):
    try:
        return match_service.get_matches_by_matchday(season, matchday)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/date/{season}/{match_date}")
def get_matches_by_date(season: int, match_date: date):
    try:
        return match_service.get_matches_by_date(season, match_date)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{id_match}/result")
def update_match_result(id_match: int, payload: dict):
    try:
        return match_service.update_match_result(id_match, payload)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/standings/{season}")
def get_standings(season: int):
    return match_service.get_standings(season)