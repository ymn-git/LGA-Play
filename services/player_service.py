from repositories.repository_instances import players_repo
from entities.player import Player
def get_players():
    return players_repo.get_all()

def get_player_by_id(id_player: int):
    return players_repo.get_by_id(id_player)

def create_player(player: dict):
    if "id" not in player or "name" not in player or "position" not in player:
        raise ValueError("Missing required fields")
    new_player = Player(
        id_person=player["id"],
        name=player["name"],
        position=player["position"]
    )
    return players_repo.create(new_player)

def put_player(id_player: int,updated_player: dict):
    if "name" not in updated_player or "position" not in updated_player:
        raise ValueError("Missing required fields")
    player = Player(
        id_person=id_player,
        name=updated_player["name"],
        position=updated_player["position"]
    )

    return players_repo.update_full(id_player,player)

def patch_player(id_player: int,name=None,position=None):
    return players_repo.update_partial(
        id_player,
        name,
        position
    )

def delete_player(id_player: int):
    return players_repo.delete(id_player)

