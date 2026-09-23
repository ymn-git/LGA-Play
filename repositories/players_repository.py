
class PlayersRepository:
    def __init__(self):
        self.players = [
            {"id": 1, "name": "Juan", "position": "GK"},
            {"id": 2, "name": "Matias", "position": "DF"},
            {"id": 3, "name": "Pablo", "position": "MF"},
            {"id": 4, "name": "Pablo", "position": "FW"}
        ]

    def get_all(self):
        return self.players

    def get_by_id(self, id_player: int):
        for p in self.players:
            if p["id"] == id_player:
                return p
        raise ValueError("Player not found")

    def create(self, player: dict):
        self.players.append(player)
        return player

    def update_full(self, id_player: int, updated_player: dict):
        for p in self.players:
            if p["id"] == id_player:
                p["name"] = updated_player["name"]
                p["position"] = updated_player["position"]
                return p
        raise ValueError("Player not found")

    def update_partial(self, id_player: int, name=None, position=None, active=None):
        for p in self.players:
            if p["id"] == id_player:
                if name is not None:
                    p["name"] = name
                if position is not None:
                    p["position"] = position
                if active is not None:
                    p["active"] = active
                return p
        raise ValueError("Player not found")

    def delete(self, id_player: int):
        for p in self.players:
            if p["id"] == id_player:
                self.players.remove(p)
                return
        raise ValueError("Player not found")
