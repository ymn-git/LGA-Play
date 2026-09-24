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

    def _get_id(self, team):
        # soporta team.id o team.id_team
        return getattr(team, 'id', getattr(team, 'id_team', None))

    def get_standings(self):
        return sorted(
            self.team_list,
            key=lambda t: (t.points, t.goal_difference, t.goals_for),
            reverse=True
        )

    def create_team(self, team_data: dict):
        if "id" not in team_data or "name" not in team_data:
            raise ValueError("Team must include 'id' and 'name' fields")
        for team in self.team_list:
            if self._get_id(team) == team_data["id"]:
                raise ValueError(f"Team with id {team_data['id']} already exists")
        new_team = Team(team_data["id"], team_data["name"])
        self.team_list.append(new_team)
        return new_team

    def delete_team(self, id_team: int):
        for team in self.team_list:
            if self._get_id(team) == id_team:
                self.team_list.remove(team)
                return team
        raise ValueError(f"Team with id {id_team} not found")

    def get_team_by_id(self, id_team):
        for team in self.team_list:
            if self._get_id(team) == id_team:
                return team
        raise ValueError(f"Team with id {id_team} not found")

    def update_points_to_winner(self, points, winner_id):
        for team in self.team_list:
            if self._get_id(team) == winner_id:
                team.points += points
                return team
        raise ValueError(f"Winner team with id {winner_id} not found")

    def update_wins_to_winner(self, winner_id):
        for team in self.team_list:
            if self._get_id(team) == winner_id:
                team.wins += 1
                return team
        raise ValueError(f"Winner team with id {winner_id} not found")

    def update_losses_to_looser(self, looser_id):
        for team in self.team_list:
            if self._get_id(team) == looser_id:
                team.losses += 1
                return team
        raise ValueError(f"Looser team with id {looser_id} not found")

    def update_draw_to_both(self, teamA_id, teamB_id):
        found_a = False
        for teamA in self.team_list:
            if self._get_id(teamA) == teamA_id:
                teamA.draws += 1
                found_a = True
                break
        if not found_a:
            raise ValueError(f"Team A with id {teamA_id} not found")

        found_b = False
        for teamB in self.team_list:
            if self._get_id(teamB) == teamB_id:
                teamB.draws += 1
                found_b = True
                break
        if not found_b:
            raise ValueError(f"Team B with id {teamB_id} not found")

    def update_points_to_both_teams(self, points, teamA_id, teamB_id):
        found_a = False
        for teamA in self.team_list:
            if self._get_id(teamA) == teamA_id:
                teamA.points += points
                found_a = True
                break
        if not found_a:
            raise ValueError(f"Team A with id {teamA_id} not found")

        found_b = False
        for teamB in self.team_list:
            if self._get_id(teamB) == teamB_id:
                teamB.points += points
                found_b = True
                break
        if not found_b:
            raise ValueError(f"Team B with id {teamB_id} not found")

    def update_positive_goal_difference(self, difference, team_id):
        for team in self.team_list:
            if self._get_id(team) == team_id:
                team.goal_difference += difference
                return team
        raise ValueError(f"Team with id {team_id} not found")

    def update_negative_goal_difference(self, difference, team_id):
        for team in self.team_list:
            if self._get_id(team) == team_id:
                team.goal_difference -= difference
                return team
        raise ValueError(f"Team with id {team_id} not found")

    def update_team_name(self, id_team: int, new_name: str):
        for team in self.team_list:
            if self._get_id(team) == id_team:
                team.name = new_name
                return team
        raise ValueError(f"Team with id {id_team} not found")

    def add_win(self, team_id):
        for team in self.team_list:
            if self._get_id(team) == team_id:
                team.wins += 1
                return team
        raise ValueError(f"Team with id {team_id} not found")

    def add_loss(self, team_id):
        for team in self.team_list:
            if self._get_id(team) == team_id:
                team.losses += 1
                return team
        raise ValueError(f"Team with id {team_id} not found")

    def add_draw(self, team_id):
        for team in self.team_list:
            if self._get_id(team) == team_id:
                team.draws += 1
                return team
        raise ValueError(f"Team with id {team_id} not found")