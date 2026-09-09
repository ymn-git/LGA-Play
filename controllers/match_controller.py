from services import match_service
from repositories.matches_repository import Match, MatchesRepository
from entities.match import *
from fastapi import APIRouter
from fastapi import HTTPException

matches_repo = MatchesRepository()

router = APIRouter(
    prefix="/matchs"
)

@router.get("/{id_match}")
def get_match_result(id_match: int):
    match = matches_repo.get_match_by_id(id_match) # buscar el partido en la BD
    return match_service.match_result(match)
