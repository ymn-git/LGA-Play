from repositories.repository_instances import coaches_repo
from repositories.repository_instances import coach_x_team_repo
from repositories.repository_instances import teams_repo

from entities.coach import Coach

def get_coaches():
    return coaches_repo.get_all()

def get_coach_by_id(id_coach: int):
    return coaches_repo.get_by_id(id_coach)

def create_coach(coach: dict):
    if "id" not in coach or "name" not in coach:
        raise ValueError("Missing required fields")
    new_coach = Coach(id_person=coach["id"],name=coach["name"])
    return coaches_repo.create(new_coach)

def put_coach(id_coach: int,updated_coach: dict):
    if "name" not in updated_coach:
        raise ValueError("Missing required fields")
    coach = Coach(id_person=id_coach,name=updated_coach["name"])
    return coaches_repo.update_full(id_coach,coach)

def patch_coach(id_coach: int,name=None):
    return coaches_repo.update_partial(id_coach,name)

def delete_coach(id_coach: int):
    return coaches_repo.delete(id_coach)

def transfer_coach(coach_id: int,new_team_id: int):
    current_team = (coach_x_team_repo.get_active_team(coach_id))
    if not current_team:
        raise ValueError("Coach has no active team")
    coach_x_team_repo.deactivate_relation(coach_id)

    return coach_x_team_repo.assign_coach(coach_id,new_team_id)

def get_current_team_of_coach(coach_id: int):
    relation = (coach_x_team_repo.get_active_team(coach_id))
    if relation is None:
        return None
    return teams_repo.get_team_by_id(relation["team_id"])