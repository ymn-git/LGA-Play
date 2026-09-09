from repositories.teams_repository import TeamsRepository

teams_repo = TeamsRepository()

def get_all_teams():
    return teams_repo.team_list

def get_team_by_id(id_team: int):
    for team in teams_repo.team_list:
        if team.id == id_team:
            return team
    raise ValueError("Team not found")

def update_team_name(id_team: int, new_name: str):
    for team in teams_repo.team_list:
        if team.id == id_team:
            team.name = new_name
            return team
    raise ValueError("Team not found")

def add_points(team_id: int, points: int):
    return teams_repo.update_points_to_winner(points, team_id)

def add_win(team_id: int):
    return teams_repo.update_wins_to_winner(team_id)

def add_loss(team_id: int):
    return teams_repo.update_losses_to_looser(team_id)

def add_draw(teamA_id: int, teamB_id: int):
    return teams_repo.update_draw_to_both(teamA_id, teamB_id)
