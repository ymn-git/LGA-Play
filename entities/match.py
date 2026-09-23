from typing import List

class Match:
    def __init__(self,
                 id_match: int,
                 teamA_id: int,
                 teamB_id: int,
                 matchday: int,
                 season: int,
                 scorers: List[int] = None,
                 yellow_cards: List[int] = None,
                 red_cards: List[int] = None,
                 goalsA: int = 0,
                 goalsB: int = 0,
                 jugado: bool = False):

        self.id_match = id_match
        self.matchday = matchday
        self.teamA_id = teamA_id
        self.teamB_id = teamB_id
        self.season = season

        # listas de eventos del partido
        self.scorers = scorers if scorers is not None else []
        self.yellow_cards = yellow_cards if yellow_cards is not None else []
        self.red_cards = red_cards if red_cards is not None else []

        self.goalsA = goalsA
        self.goalsB = goalsB
        self.jugado = jugado

    @property
    def result(self):
        if self.goalsA > self.goalsB:
            return self.teamA_id, self.teamB_id
        elif self.goalsB > self.goalsA:
            return self.teamB_id, self.teamA_id
        return None

    @property
    def goal_difference(self):
        return abs(self.goalsA - self.goalsB)

    def add_scorers(self, scorer_ids: List[int]):
        for player_id in scorer_ids:
            self.scorers.append(player_id)

        goles_por_jugador = {}
        for pid in self.scorers:
            goles_por_jugador[pid] = goles_por_jugador.get(pid, 0) + 1

        return goles_por_jugador
