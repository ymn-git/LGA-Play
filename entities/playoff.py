from sqlalchemy import (Column,Integer,String,ForeignKey,UniqueConstraint)
from sqlalchemy.orm import relationship
from app.database import Base

class Playoff(Base):
    __tablename__ = "playoff_matches"

    __table_args__ = (
        UniqueConstraint(
            "season",
            "phase",
            "bracket_group",
            "leg",
            name="uq_playoff_leg"
        ),
    )

    id = Column(Integer, primary_key=True)

    match_id = Column(
        Integer,
        ForeignKey("matches.id_match"),
        unique=True,
        nullable=False
    )

    season = Column(Integer, nullable=False, index=True)

    phase = Column(
        String,
        nullable=False,
        index=True
    )

    bracket_group = Column(
        Integer,
        nullable=False
    )

    leg = Column(
        Integer,
        nullable=False,
        default=1
    )

    match = relationship("Match",lazy="joined")