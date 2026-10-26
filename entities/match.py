from typing import List

class Match:
    def __init__(self,
                 id_match: int,
                 teamA_id: int,
                 teamB_id: int,
                 matchday: int,
                 season: int,
                 scorers: List[dict] = None,
                 yellow_cards: List[int] = None,
                 red_cards: List[int] = None,
                 goalsA: int = 0,
                 goalsB: int = 0,
                 jugado: bool = False):

        self.id_match = id_match
        self.teamA_id = teamA_id
        self.teamB_id = teamB_id
        self.matchday = matchday
        self.season = season

        self._goalsA = goalsA
        self._goalsB = goalsB
        self._jugado = jugado

        self._scorers = scorers or []
        self._yellow_cards = yellow_cards or []
        self._red_cards = red_cards or []

    @property
    def goalsA(self) -> int:
        return self._goalsA

    @goalsA.setter
    def goalsA(self, value: int):
        self._goalsA = value

    @property
    def goalsB(self) -> int:
        return self._goalsB

    @goalsB.setter
    def goalsB(self, value: int):
        self._goalsB = value

    @property
    def jugado(self) -> bool:
        return self._jugado

    @jugado.setter
    def jugado(self, value: bool):
        self._jugado = value

    @property
    def scorers(self) -> List[dict]:
        return self._scorers

    @scorers.setter
    def scorers(self, value: List[dict]):
        self._scorers = value

    @property
    def yellow_cards(self) -> List[int]:
        return self._yellow_cards

    @yellow_cards.setter
    def yellow_cards(self, value: List[int]):
        self._yellow_cards = value

    @property
    def red_cards(self) -> List[int]:
        return self._red_cards

    @red_cards.setter
    def red_cards(self, value: List[int]):
        self._red_cards = value

    @property
    def result(self):
        if self._goalsA == self._goalsB:
            return None
        return (
            (self.teamA_id, self.teamB_id)
            if self._goalsA > self._goalsB
            else (self.teamB_id, self.teamA_id)
        )

    @property
    def goal_difference(self) -> int:
        return abs(self._goalsA - self._goalsB)