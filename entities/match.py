from datetime import datetime

from entities.goal import Goal


class Match:
    def __init__(self,
                 id_match: int,
                 teamA_id: int,
                 teamB_id: int,
                 matchday: int,
                 match_date_time: datetime,
                 season: int,
                 goals: list[Goal] | None = None,
                 yellow_cards: list[int] = None,
                 red_cards: list[int] = None,
                 jugado: bool = False,
                 phase: str = "regular"):

        self.id_match = id_match
        self.teamA_id = teamA_id
        self.teamB_id = teamB_id
        self.matchday = matchday
        self.match_date_time = match_date_time
        self.season = season
        # internos
        self._jugado = jugado
        self._phase = phase
        self.goals = list(goals) if goals else []
        self._yellow_cards = list(yellow_cards) if yellow_cards else []
        self._red_cards = list(red_cards) if red_cards else []

    @property
    def phase(self) -> str:
        return self._phase

    @property
    def goalsA(self) -> list[int]:
        return [
            goal.id_player
            for goal in self.goals
            if goal.id_team == self.teamA_id
        ]

    @goalsA.setter
    def goalsA(self, player_ids: list[int]):
        self.goals = [
            goal for goal in self.goals if goal.id_team != self.teamA_id
        ]
        self.goals.extend(
            Goal(id_team=self.teamA_id, id_player=player_id)
            for player_id in player_ids
        )

    @property
    def goalsB(self) -> list[int]:
        return [
            goal.id_player
            for goal in self.goals
            if goal.id_team == self.teamB_id
        ]

    @goalsB.setter
    def goalsB(self, player_ids: list[int]):
        self.goals = [
            goal for goal in self.goals if goal.id_team != self.teamB_id
        ]
        self.goals.extend(
            Goal(id_team=self.teamB_id, id_player=player_id)
            for player_id in player_ids
        )

    @property
    def jugado(self) -> bool:
        return self._jugado

    @jugado.setter
    def jugado(self, value: bool):
        self._jugado = value

    @property
    def yellow_cards(self) -> list[int]:
        return list(self._yellow_cards)

    @yellow_cards.setter
    def yellow_cards(self, value: list[int]):
        self._yellow_cards = list(value)

    @property
    def red_cards(self) -> list[int]:
        return list(self._red_cards)

    @red_cards.setter
    def red_cards(self, value: list[int]):
        self._red_cards = list(value)

    @property
    def result(self):
        a, b = len(self.goalsA), len(self.goalsB)
        if a == b:
            return None
        return (self.teamA_id, self.teamB_id) if a > b else (self.teamB_id, self.teamA_id)

    @property
    def goal_difference(self) -> int:
        return abs(len(self.goalsA) - len(self.goalsB))
