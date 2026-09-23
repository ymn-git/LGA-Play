from repositories.teams_repository import TeamsRepository

teams_repo = TeamsRepository()

def get_all_teams():
    return teams_repo.team_list

def get_standings():
    return teams_repo.get_standings()

def get_team_by_id(id_team: int):
    return teams_repo.get_team_by_id(id_team)

def create_team(team: dict):
    return teams_repo.create_team(team)

def update_team_name(id_team: int, new_name: str):
    return teams_repo.update_team_name(id_team, new_name)

def delete_team(id_team: int):
    return teams_repo.delete_team(id_team)

def add_points(team_id: int, points: int):
    return teams_repo.update_points_to_winner(points, team_id)

def add_win(team_id: int):
    return teams_repo.update_wins_to_winner(team_id)

def add_loss(team_id: int):
    return teams_repo.update_losses_to_looser(team_id)

def add_draw(teamA_id: int, teamB_id: int):
    return teams_repo.update_draw_to_both(teamA_id, teamB_id)
