from app.database import Base
from sqlalchemy import  Column, Integer, ForeignKey, Boolean

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)

    id_match = Column(Integer, ForeignKey("matches.id_match"))
    id_team = Column(Integer, ForeignKey("teams.id_team"))
    id_player = Column(Integer, ForeignKey("players.id_player"))

    own_goal = Column(Boolean, nullable=False, default=False)