from fastapi import APIRouter, HTTPException
from services import match_service

router = APIRouter(prefix="/matchs")

@router.get("/{id_match}")
def get_match_result(id_match: int):
    try:
        return match_service.get_match_result(id_match)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/matchday/{matchday}")
def get_matches_by_matchday(matchday: int):
    return match_service.get_matches_by_matchday(matchday)

@router.patch("/{id_match}/result")
def update_match_result(id_match: int, payload: dict):
    try:
        return match_service.update_match_result(id_match, payload)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


