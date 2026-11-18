from sqlalchemy.orm import Session

from entities.player_x_team import PlayerXTeam


class PlayerXTeamsRepository:

    def __init__(self, db: Session):
        self.db = db

    def assign_player(self, player_id: int, team_id: int):
        active_relation = self.get_active_team(player_id)
        if active_relation:
            raise ValueError("Player already has an active team")
        relation = PlayerXTeam(
            player_id=player_id,
            team_id=team_id,
            active=True
        )
        self.db.add(relation)
        self.db.commit()
        self.db.refresh(relation)
        return relation

    def get_active_team(self, player_id: int):
        return (
            self.db.query(PlayerXTeam)
            .filter(
                PlayerXTeam.player_id == player_id,
                PlayerXTeam.active.is_(True)
            )
            .first()
        )

    def deactivate_relation(self, player_id: int):
        relation = self.get_active_team(player_id)
        if relation is None:
            raise ValueError("Player has no active team")
        relation.active = False
        self.db.commit()
        self.db.refresh(relation)
        return relation

    def get_players_by_team(self, team_id: int):
        #devuelve relaciones es decir jugador y equipo
        return (
            self.db.query(PlayerXTeam)
            .filter(
                PlayerXTeam.team_id == team_id,
                PlayerXTeam.active.is_(True)
            )
            .all()
        )