from entities.team import Team

class TeamsRepository:
    def __init__(self):
        self.Defensores = Team(1,"Defensores")
        self.Juventud_Unida = Team(2,"Juventud Unida")
        self.Amigos_Unidos = Team(3,"Amigos Unidos")
        self.Quilmes = Team(4,"Quilmes")
        self.Polvorin = Team(5,"Polvorin")
        self.Los_Santos = Team(6,"Los Santos")
        self.San_Martin = Team(7,"San Martin")
        self.Once_Unidos = Team(8,"Once Unidos")
        self.Huracanes = Team(9,"Huracanes")
        self.Defensores_DS = Team(10,"Defensores DS")
        self.Sudamerica = Team(11,"Sudamerica")
        self.Atletico = Team(12,"Atletico")

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

    def update_points_to_winner(self, points, winner_id):
        for team in self.team_list:
            if team.id_team == winner_id:
                team.points += points

    def update_wins_to_winner(self, winner_id):
        for team in self.team_list:
            if team.id_team == winner_id:
                team.wins +=1

    def update_losses_to_looser(self, looser_id):
        for team in self.team_list:
            if team.id_team == looser_id:
                team.losses +=1

    def update_draw_to_both(self, teamA_id, teamB_id):
        for teamA in self.team_list:
            if teamA.id_team == teamA_id:
                teamA.draws +=1
        for teamB in self.team_list:
            if teamB.id_team == teamB_id:
                teamB.draws +=1

    def update_points_to_both_teams(self, points, teamA_id, teamB_id):
        for teamA in self.team_list:
            if teamA.id_team == teamA_id:
                teamA.points += points
        for teamB in self.team_list:
            if teamB.id_team == teamB_id:
                teamB.points += points

    def update_positive_goal_difference (self, difference, team_id):
        for team in self.team_list:
            if team.id_team == team_id:
                team.goalDifference += difference

    def update_negative_goal_difference (self, difference, team_id):
        for team in self.team_list:
            if team.id_team == team_id:
                team.goalDifference -= difference

    def add_win (self, team_id):
        for team in self.team_list:
            if team.id_team == team_id:
                team.wins += 1

    def add_loss (self, team_id):
        for team in self.team_list:
            if team.id_team == team_id:
                team.losses += 1

    def add_draw (self, team_id):
        for team in self.team_list:
            if team.id_team == team_id:
                team.draws += 1






