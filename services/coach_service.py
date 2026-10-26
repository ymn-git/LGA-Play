from repositories.repository_instances import coaches_repo
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