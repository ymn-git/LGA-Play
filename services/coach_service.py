from repositories.repository_instances import (
    coaches_repo,
    coach_x_team_repo,
    teams_repo
)
from schemas.coach_schema import CoachUpdate,CoachCreate
from entities.coach import Coach

def get_coaches():
    return coaches_repo.get_all()


def get_coach_by_id(id_coach: int):
    return coaches_repo.get_by_id(id_coach)


def create_coach(coach: CoachCreate):
    new_coach = Coach(id_coach=coach.dni,name=coach.name)
    return coaches_repo.create(new_coach)

def put_coach(id_coach: int, updated_coach: CoachUpdate):
    if "name" not in updated_coach:
        raise ValueError("Missing required fields")
    coach = Coach(id_coach=id_coach,name=updated_coach["name"])
    return coaches_repo.update_full(id_coach, coach)

def patch_coach(id_coach: int, name=None):
    return coaches_repo.update_partial(id_coach, name)

def delete_coach(id_coach: int):
    return coaches_repo.delete(id_coach)


def transfer_coach(coach_id: int, new_team_id: int):

    current_team = coach_x_team_repo.get_active_team(coach_id)

    if current_team is None:
        raise ValueError("Coach has no active team")

    coach_x_team_repo.deactivate_relation(coach_id)

    return coach_x_team_repo.assign_coach(
        coach_id,
        new_team_id
    )


def get_current_team_of_coach(coach_id: int):

    relation = coach_x_team_repo.get_active_team(coach_id)

    if relation is None:
        return None

    return teams_repo.get_team_by_id(
        relation.team_id
    )