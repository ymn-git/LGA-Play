from entities.match import Match

from repositories.repository_instances import (
    teams_repo,
    matches_repo
)

def get_match_by_id(match_id):
    return matches_repo.get_match_by_id(match_id)

def get_matches_by_matchday(matchday: int):
    return matches_repo.get_matches_by_matchday(matchday)

def get_match_result(id_match: int):
    return matches_repo.get_match_by_id(id_match)

def get_top_scorers(season_id: int):
    matches = matches_repo.get_played_matches_by_season(season_id)
    contador = {}

    for match in matches:
        for goal in match.scorers:
            if goal["own_goal"]:
                continue
            player_id = goal["player_id"]
            contador[player_id] = (contador.get(player_id, 0) + 1)
    return sorted(contador.items(),key=lambda x: x[1],reverse=True)

def mark_match_as_played(match_id):
    return matches_repo.mark_match_as_played(match_id)

def update_points_to_winner(points, team_id: int):
    return teams_repo.update_points_to_winner(points, team_id)

def update_points_to_both(points, teamA_id: int, teamB_id: int):
    return teams_repo.update_points_to_both_teams(points,teamA_id,teamB_id)

def update_positive_goal_difference(goal_difference,team_id: int):
    return teams_repo.update_positive_goal_difference(goal_difference,team_id)

def update_negative_goal_difference(goal_difference,team_id: int):
    return teams_repo.update_negative_goal_difference(goal_difference,team_id)

def calculate_score(match: Match):
    goalsA = 0
    goalsB = 0
    for goal in match.scorers:
        # gol normal
        if not goal["own_goal"]:
            if goal["team_id"] == match.teamA_id:
                goalsA += 1
            elif goal["team_id"] == match.teamB_id:
                goalsB += 1
        # autogol
        else:
            if goal["team_id"] == match.teamA_id:
                goalsB += 1
            elif goal["team_id"] == match.teamB_id:
                goalsA += 1
    return goalsA, goalsB

def update_match_result(id_match: int, payload: dict):
    match = matches_repo.get_match_by_id(id_match)
    match.scorers = payload["scorers"]
    match.yellow_cards = payload["yellow_cards"]
    match.red_cards = payload["red_cards"]
    goalsA, goalsB = calculate_score(match)
    match.goalsA = goalsA
    match.goalsB = goalsB
    match.jugado = True
    updated_match = match_result(match)
    matches_repo.update_match(updated_match)
    return updated_match

def match_result(match: Match):
    result = match.result
    if result is None:
        teams_repo.add_draw(match.teamA_id)
        teams_repo.add_draw(match.teamB_id)
        update_points_to_both(1,match.teamA_id,match.teamB_id)
        return match

    winner, loser = result
    goal_difference = match.goal_difference
    teams_repo.add_win(winner)
    update_points_to_winner(3,winner)
    update_positive_goal_difference(goal_difference,winner)
    teams_repo.add_loss(loser)
    update_negative_goal_difference(goal_difference,loser)
    return match