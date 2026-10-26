from fastapi import APIRouter, HTTPException
from services import coach_x_teams_service

router = APIRouter(
    prefix="/coach-teams",
    tags=["Coach Teams"]
)


@router.post("/teams/{team_id}/coaches/{coach_id}")
def assign_coach_to_team(
    team_id: int,
    coach_id: int
):
    """
    Asigna un entrenador a un equipo por primera vez.
    """
    try:
        return coach_x_teams_service.assign_coach_to_team(
            coach_id,
            team_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.patch("/coaches/{coach_id}/teams/{new_team_id}")
def transfer_coach(
    coach_id: int,
    new_team_id: int
):
    """
    Transfiere un entrenador a otro equipo.
    """
    try:
        return coach_x_teams_service.transfer_coach(
            coach_id,
            new_team_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get("/teams/{team_id}/coaches")
def get_team_coaches(team_id: int):
    """
    Devuelve todos los entrenadores de un equipo.
    """
    try:
        return coach_x_teams_service.get_coaches_objects_by_team(
            team_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/coaches/{coach_id}/team")
def get_current_team_of_coach(coach_id: int):
    """
    Devuelve el equipo actual de un entrenador.
    """
    try:
        team = coach_x_teams_service.get_current_team_of_coach(
            coach_id
        )

        if team is None:
            raise HTTPException(
                status_code=404,
                detail="Coach has no active team"
            )

        return team

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )