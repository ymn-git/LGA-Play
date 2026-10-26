from fastapi import APIRouter, HTTPException
from services import match_service
from Schemas.match_schema import MatchResultUpdate

router = APIRouter(prefix="/matches")

@router.get("/{id_match}")
def get_match_result(id_match: int):
    try:
        return match_service.get_match_result(id_match)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/matchday/{matchday}")
def get_matches_by_matchday(matchday: int):
    return match_service.get_matches_by_matchday(matchday)

@router.get("/season/{season_id}/top-scorers")
def get_top_scorers(season_id: int):
    return match_service.get_top_scorers(season_id)

@router.patch("/{id_match}/result")
def update_match_result(id_match: int,payload: MatchResultUpdate):
    try:
        return match_service.update_match_result(id_match,payload.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))


