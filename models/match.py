from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    teamA_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    teamB_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    season = Column(Integer, nullable=False, default=2026)
    match_date = Column(DateTime, default=datetime.utcnow)

    goalsA = Column(Integer, default=0)
    goalsB = Column(Integer, default=0)
    jugado = Column(Boolean, default=False)

    scorers = Column(JSON, default=list)
    yellow_cards = Column(JSON, default=list)
    red_cards = Column(JSON, default=list)

    # Relaciones
    teamA = relationship("Team", foreign_keys=[teamA_id])
    teamB = relationship("Team", foreign_keys=[teamB_id])
    fase_info = relationship("MatchXFase", back_populates="match", uselist=False, cascade="all, delete-orphan")
