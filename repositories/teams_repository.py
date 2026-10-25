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

    def get_standings(self):
        return sorted(
            self.team_list,
            key=lambda t: (t.points, t.goal_difference, t.goals_for),
            reverse=True
        )

    def create_team(self, team_data: dict):
        # Validación mínima
        if "id" not in team_data or "name" not in team_data:
            raise ValueError("Team must include 'id' and 'name' fields")

        # Evitar duplicados
        for team in self.team_list:
            if team.id == team_data["id"]:
                raise ValueError(f"Team with id {team_data['id']} already exists")

        # Crear el objeto Team
        new_team = Team(team_data["id"], team_data["name"])
        self.team_list.append(new_team)
        return new_team

    def delete_team(self, id_team: int):
        for team in self.team_list:
            if team.id == id_team:
                self.team_list.remove(team)
                return team

        raise ValueError(f"Team with id {id_team} not found")

    def get_team_by_id(self, id_team):
        for team in self.team_list:
            if team.id == id_team:
                return team
        raise ValueError(f"Team with id {id_team} not found")

    def update_team_name(self, id_team: int, new_name: str):
        for team in self.team_list:
            if team.id == id_team:
                team.name = new_name
                return team
        raise ValueError(f"Team with id {id_team} not found")