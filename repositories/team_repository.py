from entities.team import Team
from repositories.matchday_repository import fixture

class TeamsRepository:
    def __init__(self):
        self.Defensores = Team("Defensores")
        self.Juventud_Unida = Team("Juventud Unida")
        self.Amigos_Unidos = Team("Amigos Unidos")
        self.Quilmes = Team("Quilmes")
        self.Polvorin = Team("Polvorin")
        self.Los_Santos = Team("Los Santos")
        self.San_Martin = Team("San Martin")
        self.Once_Unidos = Team("Once Unidos")
        self.Huracanes = Team("Huracanes")
        self.Defensores_DS = Team("Defensores DS")
        self.Sudamerica = Team("Sudamerica")
        self.Atletico = Team("Atletico")

        # lista para recorrer todos juntos
        self.team_list = [
            self.Defensores,
            self.Juventud_Unida,
            self.Amigos_Unidos,
            self.Quilmes,
            self.Polvorin,
            self.Los_Santos,
            self.San_Martin,
            self.Once_Unidos,
            self.Huracanes,
            self.Defensores_DS,
            self.Sudamerica,
            self.Atletico
        ]

    def update_points_to_winner (self, points, team_name):
        for team in self.team_list:
            if team.name == team_name:
                team.points += points

    def update_points_to_both(self, points, team_a_name, team_b_name):
        for teamA in self.team_list:
            if teamA.name == team_a_name:
                teamA.points = points
        for teamB in self.team_list:
            if teamB.name == team_b_name:
                teamB.points += points

    def update_goal_difference (self, difference, team_name):
        for team in self.team_list:
            if team.name == team_name:
                team.goalDifference += difference

    def add_win (self, team_name):
        for team in self.team_list:
            if team.name == team_name:
                team.wins += 1

    def add_loss (self, team_name):
        for team in self.team_list:
            if team.name == team_name:
                team.losses += 1

    def add_draw (self, team_name):
        for team in self.team_list:
            if team.name == team_name:
                team.draws += 1




