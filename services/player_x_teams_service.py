from repositories.repository_instances import (
    player_x_team_repo,
    players_repo,
    teams_repo
)

def assign_player_to_team(player_id: int,team_id: int):
    existing_team = (player_x_team_repo.get_active_team(player_id))
    if existing_team:
        raise ValueError("Player already belongs to a team")
    return player_x_team_repo.assign_player(player_id,team_id)

def transfer_player(player_id: int,new_team_id: int):
    current_team = (player_x_team_repo.get_active_team(player_id))
    if not current_team:
        raise ValueError("Player has no active team")
    player_x_team_repo.deactivate_relation(player_id)
    return player_x_team_repo.assign_player(player_id,new_team_id)

def get_team_players(team_id: int):
    return player_x_team_repo.get_players_by_team(team_id)

def get_players_objects_by_team(team_id: int):
    relations = (player_x_team_repo.get_players_by_team(team_id))
    players = []
    for relation in relations:
        player = (players_repo.get_by_id(relation.player_id))
        players.append(player)
    return players

def get_current_team_of_player(player_id: int):
    relation = (player_x_team_repo.get_active_team(player_id))
    if relation is None:
        return None
    return teams_repo.get_team_by_id(relation.team_id)