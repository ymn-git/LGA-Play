from services import season_stats_service
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/season_stats")

@router.get("/season/{season_id}/top-scorers")
def get_top_scorers(season_id: int):
    try:
        return season_stats_service.get_top_scorers(season_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
