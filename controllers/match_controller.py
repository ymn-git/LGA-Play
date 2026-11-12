from fastapi import APIRouter, HTTPException
from services import match_service
from Schemas.match_schema import MatchResultUpdate

router = APIRouter(prefix="/matches")

@router.get("/matchday/{matchday}")
def get_matches_by_matchday(matchday: int, season: int):
    return match_service.get_matches_by_matchday(matchday,season)

@router.get("/season/{season_id}/top-scorers")
def get_top_scorers(season_id: int):
    return match_service.get_top_scorers(season_id)

@router.patch("/{id_match}/result")
def update_match_result(id_match: int, payload: MatchResultUpdate):
    try:
        return match_service.update_match_result(id_match, payload)
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

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