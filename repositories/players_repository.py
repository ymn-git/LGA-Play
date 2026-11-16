from sqlalchemy.orm import Session

from entities.player import Player


class PlayersRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):

        return (
            self.db.query(Player)
            .order_by(Player.id_player)
            .all()
        )

    def get_by_id(self, id_player: int):

        player = (
            self.db.query(Player)
            .filter(Player.id_player == id_player)
            .first()
        )

        if player is None:
            raise ValueError("Player not found")

        return player

    def create(self, player: Player):

        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)

        return player

    def update_full(self, id_player: int, updated_player: Player):

        player = self.get_by_id(id_player)

        player.name = updated_player.name
        player.position = updated_player.position

        self.db.commit()
        self.db.refresh(player)

        return player

    def update_partial(self, id_player: int, name=None, position=None):

        player = self.get_by_id(id_player)

        if name is not None:
            player.name = name

        if position is not None:
            player.position = position

        self.db.commit()
        self.db.refresh(player)

        return player

    def delete(self, id_player: int):

        player = self.get_by_id(id_player)

        self.db.delete(player)
        self.db.commit()

        return player