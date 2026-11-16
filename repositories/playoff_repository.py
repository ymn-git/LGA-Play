from sqlalchemy.orm import Session

from entities.playoff import Playoff


class PlayoffRepository:

    def __init__(self, db: Session):
        self.db = db

    def add(
        self,
        match_id: int,
        season: int,
        phase: str,
        bracket_group: int,
        leg: int
    ):

        playoff = Playoff(
            match_id=match_id,
            season=season,
            phase=phase,
            bracket_group=bracket_group,
            leg=leg
        )

        self.db.add(playoff)

        # genera el id sin hacer commit todavía
        self.db.flush()

        return playoff

    def leg_exists(
        self,
        season: int,
        phase: str,
        bracket_group: int,
        leg: int
    ) -> bool:

        return (
            self.db.query(Playoff.id)
            .filter(
                Playoff.season == season,
                Playoff.phase == phase,
                Playoff.bracket_group == bracket_group,
                Playoff.leg == leg
            )
            .first()
            is not None
        )

    def get_by_bracket(
        self,
        season: int,
        phase: str,
        bracket_group: int
    ):

        return (
            self.db.query(Playoff)
            .filter(
                Playoff.season == season,
                Playoff.phase == phase,
                Playoff.bracket_group == bracket_group
            )
            .order_by(Playoff.leg)
            .all()
        )

    def get_by_match_id(self, match_id: int):

        return (
            self.db.query(Playoff)
            .filter(
                Playoff.match_id == match_id
            )
            .first()
        )

    def delete(self, playoff_id: int):

        playoff = (
            self.db.query(Playoff)
            .filter(
                Playoff.id == playoff_id
            )
            .first()
        )

        if playoff is None:
            raise ValueError("Playoff not found")

        self.db.delete(playoff)
        self.db.commit()

        return playoff