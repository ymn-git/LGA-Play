from repositories.players_repository import PlayersRepository

players_repo = PlayersRepository()

def get_players():
    return players_repo.get_all()

def get_player_by_id(id_player: int):
    return players_repo.get_by_id(id_player)

def create_player(player: dict):
    if "id" not in player or "name" not in player or "position" not in player:
        raise ValueError("Missing required fields")
    return players_repo.create(player)

def put_player(id_player: int, updated_player: dict):
    if "name" not in updated_player or "position" not in updated_player:
        raise ValueError("Missing required fields")
    return players_repo.update_full(id_player, updated_player)

def patch_player(id_player: int, name=None, position=None, active=None):
    return players_repo.update_partial(id_player, name, position, active)

def delete_player(id_player: int):
    return players_repo.delete(id_player)

