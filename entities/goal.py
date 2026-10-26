from dataclasses import dataclass


@dataclass
class Goal:
    id_team: int
    id_player: int
    own_goal: bool = False
