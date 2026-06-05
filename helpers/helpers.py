# helpers/team_helpers.py
from entities.team import Team
from repositories.team_repository import teams

def get_team_by_name(name: str) -> Team:
    for team in teams:
        if team.name == name:
            return team
    raise ValueError(f"Equipo '{name}' no encontrado")
