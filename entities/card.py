from app.database import Base
from sqlalchemy import  Column, Integer, ForeignKey, String

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)

    id_match = Column(Integer, ForeignKey("matches.id_match"))
    id_player = Column(Integer, ForeignKey("players.id_player"))

    type = Column(String(20), nullable=False)