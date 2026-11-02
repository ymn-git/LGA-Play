from repositories.repository_instances import players_repo
from repositories.repository_instances import teams_repo
from repositories.repository_instances import player_x_team_repo
from entities.player import Player

def get_players():
    return players_repo.get_all()

def get_player_by_id(id_player: int):
    return players_repo.get_by_id(id_player)

def create_player(player: dict):
    if "id" not in player or "name" not in player or "position" not in player:
        raise ValueError("Missing required fields")
    new_player = Player(id_person=player["id"],name=player["name"],position=player["position"])
    return players_repo.create(new_player)

def put_player(id_player: int,updated_player: dict):
    if "name" not in updated_player or "position" not in updated_player:
        raise ValueError("Missing required fields")
    player = Player(id_person=id_player,name=updated_player["name"],position=updated_player["position"])

    return players_repo.update_full(id_player,player)

def patch_player(id_player: int,name=None,position=None):
    return players_repo.update_partial(id_player,name,position)

def delete_player(id_player: int):
    return players_repo.delete(id_player)

def transfer_player(player_id: int,new_team_id: int):
    current_team = (player_x_team_repo.get_active_team(player_id))
    if not current_team:
        raise ValueError("Player has no active team")
    player_x_team_repo.deactivate_relation(player_id)
    return player_x_team_repo.assign_player(player_id,new_team_id)

def get_current_team_of_player(player_id: int):
    relation = (player_x_team_repo.get_active_team(player_id))
    if relation is None:
        return None
    return teams_repo.get_team_by_id(relation["team_id"])