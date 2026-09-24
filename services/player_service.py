from repositories.players_repository import PlayersRepository
from repositories.matches_repository import MatchesRepository
from collections import Counter

players_repo = PlayersRepository()
matches_repo = MatchesRepository()

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

def get_scorers():
    players = players_repo.get_all()
    matches = matches_repo.get_all()
    counter = Counter()

    for m in matches:
        if isinstance(m, dict):
            if m.get("jugado") is False:
                continue
            scorers = m.get("scorers_list", []) or m.get("scorers", [])
        else:
            if hasattr(m, 'jugado') and not m.jugado:
                continue
            scorers = getattr(m, 'scorers_list', []) or getattr(m, 'scorers', [])
        
        counter.update(scorers)

    result = []
    for p in players:
        if isinstance(p, dict):
            p_dict = p
            p_id = p.get("id")
        else:
            p_dict = p.toJSON() if hasattr(p, 'toJSON') else p.__dict__
            p_id = getattr(p, 'id', None) or p_dict.get("id")

        result.append({
            **p_dict,
            "goals": counter.get(p_id, 0)
        })

    result.sort(key=lambda x: x["goals"], reverse=True)
    return result