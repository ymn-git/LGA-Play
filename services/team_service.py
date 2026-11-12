from repositories.repository_instances import (
    teams_repo,
    coaches_repo,
    coach_x_team_repo,
    players_repo,
    player_x_team_repo,
)
from services import match_service

def get_all_teams():
    return teams_repo.get_all_teams()

def get_team_by_id(id_team: int):
    return teams_repo.get_team_by_id(id_team)

def create_team(team: dict):
    return teams_repo.create_team(team)

def update_team_name(id_team: int, new_name: str):
    return teams_repo.update_team_name(id_team, new_name)

def delete_team(id_team: int):
    return teams_repo.delete_team(id_team)

def get_team_stats(team_id: int, season: int):
    teams_repo.get_team_by_id(team_id)
    for row in match_service.get_standings(season):
        if row["id_team"] == team_id:
            return row
    raise ValueError("Team not found in standings")


def assign_player_to_team(team_id: int,player_id: int):
    team = teams_repo.get_team_by_id(team_id)
    player = players_repo.get_by_id(player_id)
    if not team:
        raise ValueError("Team not found")
    if not player:
        raise ValueError("Player not found")
    return player_x_team_repo.assign_player(
        player_id,
        team_id
    )

def assign_coach_to_team(coach_id: int,team_id: int):
    team = teams_repo.get_team_by_id(team_id)
    coach = coaches_repo.get_by_id(coach_id)
    if not team:
        raise ValueError("Team not found")
    if not coach:
        raise ValueError("Coach not found")
    return coach_x_team_repo.assign_coach(coach_id,team_id)

def get_team_players(team_id: int):
    return player_x_team_repo.get_players_by_team(team_id)

def get_team_coach(team_id: int):
    return coach_x_team_repo.get_coaches_by_team(team_id)

def get_players_objects_by_team(team_id: int):
    teams_repo.get_team_by_id(team_id)  # ValueError si no existe
    relations = (player_x_team_repo.get_players_by_team(team_id))
    players = []
    for relation in relations:
        player = (players_repo.get_by_id(relation["player_id"]))
        players.append(player)
    return players

def get_coaches_objects_by_team(team_id: int):
    relations = (coach_x_team_repo.get_coaches_by_team(team_id))
    coaches = []
    for relation in relations:
        coach = coaches_repo.get_by_id(relation["coach_id"])
        coaches.append(coach)
    return coaches