import repositories.team_repository
from entities.team import Team
from repositories.team_repository import *

# aca instancie el repo dentro del service pero no es escalable preguntar al profe si mejor hago  lo siguiente:
# def __init__(self, repo: TeamsRepository):
#   self.repo = repo
# y asi desde el controller tengo que instanciar el repo y pasarselo al service por parametro para inyeccion:
# repo = TeamsRepository()
# service = MatchService(repo)

class MatchService:
    def __init__(self):
        self.repo = repositories.team_repository.TeamsRepository()
    def update_points_to_winner(self, points, team:Team):
        return self.repo.update_points_to_winner(points, team.name)
    def update_points_to_both(self, points, team_a:Team, team_b: Team):
        return self.repo.update_points_to_both(points, team_a, team_b)


