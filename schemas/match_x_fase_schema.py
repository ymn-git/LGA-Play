from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class MatchXFaseBase(BaseModel):
    fase_id: int
    tipo_fase: str = Field(..., pattern="^(REGULAR|PLAYOFF)$")
    matchday: Optional[int] = None
    round_name: Optional[str] = None
    bracket_order: Optional[int] = None
    penaltiesA: Optional[int] = None
    penaltiesB: Optional[int] = None
    winner_id: Optional[int] = None

class RegularMatchCreate(BaseModel):
    teamA_id: int
    teamB_id: int
    season: int = 2026
    match_date: Optional[datetime] = None
    matchday: int

class PlayoffMatchCreate(BaseModel):
    teamA_id: int
    teamB_id: int
    season: int = 2026
    match_date: Optional[datetime] = None
    round_name: str  # 'PRIMERA_RONDA', 'CUARTOS', 'SEMIFINAL', 'FINAL'
    bracket_order: int  # 1, 2, 3, 4...

class PlayoffResultUpdate(BaseModel):
    goalsA: int
    goalsB: int
    penaltiesA: Optional[int] = None
    penaltiesB: Optional[int] = None
    winner_id: int
    scorers: List[dict] = []
    yellow_cards: List[int] = []
    red_cards: List[int] = []

class MatchResponse(BaseModel):
    id: int
    teamA_id: int
    teamB_id: int
    season: int
    match_date: Optional[datetime] = None
    goalsA: int
    goalsB: int
    jugado: bool
    tipo_fase: str
    matchday: Optional[int] = None
    round_name: Optional[str] = None
    bracket_order: Optional[int] = None
    penaltiesA: Optional[int] = None
    penaltiesB: Optional[int] = None
    winner_id: Optional[int] = None

    class Config:
        from_attributes = True
