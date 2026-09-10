
from entities.team import Team
from typing import List

class Match:
    def __init__(self, id_match,
                 teamA_id:int,
                 teamB_id:int,
                 matchday: int,
                 scorer_list:List[int],
                 goalsA:int=0,
                 goalsB:int=0,
                 jugado:bool=False):
        self.id_match = id_match
        self.matchday = matchday
        self.teamA_id = teamA_id
        self.teamB_id = teamB_id
        self.goalsA = goalsA
        self.goalsB = goalsB
        self.scorers_list = scorer_list
        self.jugado = jugado


    @property
    def result(self):
        if self.goalsA > self.goalsB:
            winner = self.teamA_id
            looser = self.teamB_id
            return winner, looser
        elif self.goalsB > self.goalsA:
            winner = self.teamB_id
            looser = self.teamA_id
            return winner, looser
        else:
            return None

    @property
    def goal_difference(self):
        if self.goalsA > self.goalsB:
            return self.goalsA - self.goalsB
        if self.goalsB > self.goalsA:
            return self.goalsB - self.goalsA
        return 0

    def add_scorers(self, scorer_ids: list[int]):
        # agregar los ids a la lista de goleadores del partido
        for player_id in scorer_ids:
            self.scorers_list.append(player_id)

        # contar cuántos goles hizo cada jugador
        goles_por_jugador = {}
        for pid in self.scorers_list:
            if pid not in goles_por_jugador:
                goles_por_jugador[pid] = 0
            goles_por_jugador[pid] += 1

        return goles_por_jugador


