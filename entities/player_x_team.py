from sqlalchemy import Boolean, Column, ForeignKey, Integer
from app.database import Base


class PlayerXTeam(Base):
    __tablename__ = "player_x_team"

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(
        Integer,
        ForeignKey("players.id_player"),
        nullable=False
    )

    team_id = Column(
        Integer,
        ForeignKey("teams.id_team"),
        nullable=False
    )

    active = Column(Boolean, nullable=False, default=True)