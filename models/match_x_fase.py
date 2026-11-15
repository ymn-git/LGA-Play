from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class MatchXFase(Base):
    """
    Tabla intermedia única para vincular un partido (Match) con su fase (Fase).
    Permite almacenar tanto partidos de Fase Regular como de Playoffs,
    resolviendo las particularidades de cada uno.
    """
    __tablename__ = "match_x_fase"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"), nullable=False, unique=True)
    fase_id = Column(Integer, ForeignKey("fases.id"), nullable=False)
    tipo_fase = Column(String, nullable=False)  # 'REGULAR' o 'PLAYOFF'

    # Campos específicos para FASE REGULAR
    matchday = Column(Integer, nullable=True)   # Número de jornada/fecha (1..22)

    # Campos específicos para PLAYOFFS
    round_name = Column(String, nullable=True)     # 'PRIMERA_RONDA', 'CUARTOS', 'SEMIFINAL', 'FINAL'
    bracket_order = Column(Integer, nullable=True) # Posición/llave dentro de la ronda (1, 2, 3...)
    penaltiesA = Column(Integer, nullable=True)    # Goles en tanda de penales equipo A
    penaltiesB = Column(Integer, nullable=True)    # Goles en tanda de penales equipo B
    winner_id = Column(Integer, ForeignKey("teams.id"), nullable=True) # Clasificado/ganador de la serie

    # Relaciones ORM
    match = relationship("Match", back_populates="fase_info")
    fase = relationship("Fase", back_populates="partidos_fase")
    winner = relationship("Team", foreign_keys=[winner_id])
