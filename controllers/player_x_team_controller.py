from fastapi import APIRouter, HTTPException
from services import player_x_teams_service

router = APIRouter(prefix="/player-teams",tags=["Player Teams"])

@router.post("/teams/{team_id}/players/{player_id}")
def assign_player_to_team(team_id: int,player_id: int):
    """
    Asigna un jugador a un equipo por primera vez.
    """
    try:
        return player_x_teams_service.assign_player_to_team(player_id,team_id)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.patch("/players/{player_id}/teams/{new_team_id}")
def transfer_player(player_id: int,new_team_id: int):
    """
    Transfiere un jugador a otro equipo.
    """
    try:
        return player_x_teams_service.transfer_player(player_id,new_team_id)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))

@router.get("/teams/{team_id}/players")
def get_team_players(team_id: int):
    """
    Devuelve todos los jugadores de un equipo.
    """
    try:
        return player_x_teams_service.get_players_objects_by_team(team_id)

    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))

@router.get("/players/{player_id}/team")
def get_current_team_of_player(player_id: int):
    """
    Devuelve el equipo actual de un jugador.
    """
    try:
        team = player_x_teams_service.get_current_team_of_player(player_id)
        if team is None:
            raise HTTPException(status_code=404,detail="Player has no active team")
        return team
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))