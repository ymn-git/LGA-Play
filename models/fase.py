from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Fase(Base):
    __tablename__ = "fases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)          # ej: "Fase Regular", "Playoffs"
    tipo = Column(String, nullable=False)          # 'REGULAR' o 'PLAYOFF'
    season = Column(Integer, nullable=False, default=2026)

    # Relación con la tabla intermedia
    partidos_fase = relationship("MatchXFase", back_populates="fase", cascade="all, delete-orphan")
