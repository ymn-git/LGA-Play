from sqlalchemy import Column, Integer, String
from app.database import Base


class Coach(Base):
    __tablename__ = "coaches"

    id_coach = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
