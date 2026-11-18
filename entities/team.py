from sqlalchemy import Column, Integer, String
from app.database import Base


class Team(Base):
    __tablename__ = "teams"

    id_team = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)