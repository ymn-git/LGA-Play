from repositories.teams_repository import TeamsRepository
from entities.match import Match
from  repositories.matches_repository import MatchesRepository
teams_repo = TeamsRepository()
matches_repo = MatchesRepository()

def get_match_by_id(match_id):
    return matches_repo.get_match_by_id(match_id)

def update_match_goals(match_id, goalsA, goalsB):
    return matches_repo.update_match_goals(match_id,goalsA,goalsB)

def mark_match_as_played(match_id):
    return matches_repo.mark_match_as_played(match_id)

def add_scorer(match_id, player_id):
    return matches_repo.add_scorer(match_id, player_id)

def update_points_to_winner(points, team_id: int):
    return teams_repo.update_points_to_winner(points, team_id)

def update_points_to_both(points, teamA_id: int, teamB_id: int):
    return teams_repo.update_points_to_both_teams(points, teamA_id, teamB_id)

def update_positive_goal_difference(goal_difference, team_id: int):
    return teams_repo.update_positive_goal_difference(goal_difference, team_id)

def update_negative_goal_difference(goal_difference, team_id: int):
    return teams_repo.update_negative_goal_difference(goal_difference, team_id)

def match_result(match:Match):
    # 1 Marco el partido como jugado
    matches_repo.mark_match_as_played(match.id_match)
    # 2 Guardo el resultado del partido
    update_match_goals(match.id_match, match.goalsA, match.goalsB)
    # 3 Obtengo el resultado del partido con su propiedad pública
    result = match.result

    # EMPATE
    if result is None:
        teams_repo.add_draw(match.teamA_id)
        teams_repo.add_draw(match.teamB_id)
        update_points_to_both(1, match.teamA_id, match.teamB_id)
        update_match_goals(match.id_match, match.goalsA, match.goalsB)
        return match

    # VICTORIA
    winner, looser = result
    goal_difference = match.goal_difference

    teams_repo.add_win(winner)
    update_points_to_winner(3, winner)
    update_positive_goal_difference(goal_difference, winner)

    teams_repo.add_loss(looser)
    update_negative_goal_difference(goal_difference, looser)

    return match

def add_win(winner_team_id):
    return teams_repo.update_wins_to_winner(winner_team_id)

def add_loss(looser_team_id):
    return teams_repo.update_losses_to_looser(looser_team_id)

def add_tie(teamA_id, teamB_id):
    return teams_repo.update_draw_to_both(teamA_id,teamB_id)

