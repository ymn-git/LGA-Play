from entities.player import Player


class PlayersRepository:
    def __init__(self):
        self.players = [
            Player(1, "Juan", "GK"),
            Player(2, "Matias", "DF"),
            Player(3, "Pablo", "MF"),
            Player(4, "Pablo", "FW")
        ]

    def get_all(self):
        return self.players

    def get_by_id(self, id_player: int):
        for player in self.players:

            if player.id_person == id_player:
                return player

        raise ValueError("Player not found")

    def create(self, player: Player):
        self.players.append(player)
        return player

    def update_full(
        self,
        id_player: int,
        updated_player: Player
    ):
        player = self.get_by_id(id_player)

        player.name = updated_player.name
        player.position = updated_player.position

        return player

    def update_partial(
        self,
        id_player: int,
        name=None,
        position=None
    ):
        player = self.get_by_id(id_player)

        if name is not None:
            player.name = name

        if position is not None:
            player.position = position

        return player

    def delete(self, id_player: int):
        player = self.get_by_id(id_player)

        self.players.remove(player)