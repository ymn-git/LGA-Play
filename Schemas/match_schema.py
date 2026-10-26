# schemas/match_schema.py

from pydantic import BaseModel

class GoalInput(BaseModel):
    player_id: int
    team_id: int
    own_goal: bool

class MatchResultUpdate(BaseModel):
    scorers: list[GoalInput]
    yellow_cards: list[int]
    red_cards: list[int]