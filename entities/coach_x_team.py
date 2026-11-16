from sqlalchemy import Boolean, Column, ForeignKey, Integer
from app.database import Base


class CoachXTeam(Base):
    __tablename__ = "coach_x_team"

    id = Column(Integer, primary_key=True, index=True)

    coach_id = Column(
        Integer,
        ForeignKey("coaches.id_coach"),
        nullable=False
    )

    team_id = Column(
        Integer,
        ForeignKey("teams.id_team"),
        nullable=False
    )

    active = Column(Boolean, nullable=False, default=True)