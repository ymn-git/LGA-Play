from typing import Optional

players_list = [
    {"id": 1, "name": "Juan", "position": "GK"},
    {"id": 2, "name": "Matias", "position": "DF"},
    {"id": 3, "name": "Pablo", "position": "MF"},
    {"id": 4, "name": "Pablo", "position": "FW"}
]
def get_players():
    return players_list

def get_player_by_id(id_player: int):
    for p in players_list:
        if p["id"] == id_player:
            return p
    raise ValueError("Player not found")

def create_player(player: dict):
    if "name" not in player or "position" not in player:
        raise ValueError("Missing required fields")
    new_player = {
        "id": len(players_list) + 1,
        "name": player["name"],
        "position": player["position"]
    }
    players_list.append(new_player)
    return new_player

def put_player(id_player:int, updated_player:dict):
    if "name" not in updated_player or "position" not in updated_player:
        raise ValueError("Missing required fields")
    for p in players_list:
        if p["id"] == id_player:
            p["name"] = updated_player["name"]
            p["position"] = updated_player["position"]
            return updated_player

def patch_player(id_player: int,
                 name: Optional[str] = None,
                 position: Optional[str] = None,
                 active: Optional[bool] = None):
    for p in players_list:
        if p["id"] == id_player:
            if name is not None:
                p["name"] = name
            if position is not None:
                p["position"] = position
            if active is not None:
                p["active"] = active
            return p
    raise ValueError("Player nor found")

def delete_player(id_player:int):
    for p in players_list:
        if p["id"] == id_player:
            players_list.remove(p)
            return
    raise ValueError("Player nor found")
