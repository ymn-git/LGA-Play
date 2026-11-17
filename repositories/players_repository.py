from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from entities.player import Player
from entities.card import Card
from entities.goal import Goal
from entities.match import Match

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

    def get_stats(self, id_player: int, season: Optional[int] = None):
        self.get_by_id(id_player)

        goals_query = (
            self.db.query(func.count(Goal.id))
            .join(Match, Match.id_match == Goal.id_match)
            .filter(
                Goal.id_player == id_player,
                Goal.own_goal.is_(False),
                Match.jugado.is_(True)
            )
        )
        if season is not None:
            goals_query = goals_query.filter(Match.season == season)
        goals = goals_query.scalar()

        cards_query = (
            self.db.query(Card.type, func.count(Card.id))
            .join(Match, Match.id_match == Card.id_match)
            .filter(
                Card.id_player == id_player,
                Card.type.in_(("yellow", "red")),
                Match.jugado.is_(True)
            )
        )
        if season is not None:
            cards_query = cards_query.filter(Match.season == season)
        cards = cards_query.group_by(Card.type).all()
        card_counts = {card_type: count for card_type, count in cards}

        return {
            "player_id": id_player,
            "goals": goals or 0,
            "yellow_cards": card_counts.get("yellow", 0),
            "red_cards": card_counts.get("red", 0)
        }