from services import match_service
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/matchs"
)


@router.get("")
def get_matches():
    return match_service.get_matches()


@router.get("/{id_match}")
def get_match_by_id(id_match: int):
    match = match_service.get_match_by_id(id_match)

    if match is None:
        raise HTTPException(
            status_code=404,
            detail="Match not found"
        )

    return match