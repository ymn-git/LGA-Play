from sqlalchemy import Column, Integer, String
from app.database import Base


class Player(Base):
    __tablename__ = "players"

    id_player = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    position = Column(String(20), nullable=True)