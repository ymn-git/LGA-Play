
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer

from app.database import Base


class Match(Base):
    __tablename__ = "matches"

    id_match = Column(Integer, primary_key=True, index=True)

    teamA_id = Column(
        Integer,
        ForeignKey("teams.id_team"),
        nullable=False
    )

    teamB_id = Column(
        Integer,
        ForeignKey("teams.id_team"),
        nullable=False
    )

    matchday = Column(Integer, nullable=False)

    season = Column(Integer, nullable=False)

    full_date = Column(DateTime, nullable=False)

    goalsA = Column(Integer, nullable=False, default=0)
    goalsB = Column(Integer, nullable=False, default=0)

    jugado = Column(Boolean, nullable=False, default=False)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.scorers = []
        self.yellow_cards = []
        self.red_cards = []
    @property
    def result(self):
        if self.goalsA == self.goalsB:
            return None

        return (
            (self.teamA_id, self.teamB_id)
            if self.goalsA > self.goalsB
            else (self.teamB_id, self.teamA_id)
        )

    @property
    def goal_difference(self):
        return abs(self.goalsA - self.goalsB)