from repositories.repository_instances import (
    coach_x_team_repo,
    coaches_repo,
    teams_repo
)


def assign_coach_to_team(coach_id: int,team_id: int):
    existing_team = (coach_x_team_repo.get_active_team(coach_id))
    if existing_team:
        raise ValueError("Coach already belongs to a team")

    return coach_x_team_repo.assign_coach(coach_id,team_id)

def transfer_coach(coach_id: int,new_team_id: int):
    current_team = (coach_x_team_repo.get_active_team(coach_id))
    if not current_team:
        raise ValueError("Coach has no active team")
    coach_x_team_repo.deactivate_relation(coach_id)

    return coach_x_team_repo.assign_coach(coach_id,new_team_id)

def get_team_coaches(team_id: int):
    return coach_x_team_repo.get_coaches_by_team(team_id)

def get_coaches_objects_by_team(team_id: int):
    relations = (coach_x_team_repo.get_coaches_by_team(team_id))
    coaches = []
    for relation in relations:
        coach = coaches_repo.get_by_id(relation.coach_id)
        coaches.append(coach)
    return coaches

def get_current_team_of_coach(coach_id: int):
    relation = (coach_x_team_repo.get_active_team(coach_id))
    if relation is None:
        return None
    return teams_repo.get_team_by_id(relation.team_id)