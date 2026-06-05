from msilib.schema import Property
from entities.team import Team
class Match:
    def __init__(self, teamA:Team, teamB:Team, goalsA:int=0, goalsB:int=0):
        self.teamA = teamA
        self.teamB = teamB
        self.goalsA = goalsA
        self.goalsB = goalsB

    @property
    def result(self):
        if self.goalsA > self.goalsB:
            return self.teamA
        elif self.goalsB > self.goalsA:
            return self.teamB
        else:
            return None
    @property
    def goal_difference(self):
        if self.goalsA > self.goalsB:
            return self.goalsA - self.goalsB
        elif self.goalsB > self.goalsA:
            return self.goalsB - self.goalsA
        else:
            return 0
