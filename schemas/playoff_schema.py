from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class PlayoffMatchCreate(BaseModel):
    season: int
    phase: Literal["cuartos", "semis", "final", "finalisima"]
    bracket_group: int
    leg: Literal[1, 2] = 1

    team_a_id: int
    team_b_id: int

    full_date: datetime

