from datetime import date

from entities.goal import Goal
from repositories.matches_repository import MatchesRepository
from repositories.teams_repository import TeamsRepository
from services import player_service


teams_repo = TeamsRepository()
matches_repo = MatchesRepository()


def get_match_by_id(match_id: int):
    return matches_repo.get_match_by_id(match_id)


def get_matches():
    return matches_repo.get_all()


def _get_played_matches(season: int):
    return matches_repo.get_played_matches_by_season(season)


def get_matches_by_matchday(season: int, matchday: int):
    return matches_repo.get_matches_by_matchday(season, matchday)


def get_matches_by_date(season: int, match_date: date):
    return matches_repo.get_matches_by_date(season, match_date)


def get_match_result(match_id: int):
    return matches_repo.get_match_by_id(match_id)


def update_match_result(match_id: int, payload: dict):
    match = matches_repo.get_match_by_id(match_id)

    if "goals" in payload:
        match.goals = [Goal(**goal) for goal in payload["goals"]]
    else:
        match.goalsA = payload["goalsA"]
        match.goalsB = payload["goalsB"]

    match.yellow_cards = payload["yellow_cards"]
    match.red_cards = payload["red_cards"]
    match.jugado = payload["jugado"]

    return matches_repo.update_match(match)


def get_match_stats(match_id: int) -> dict:
    match = matches_repo.get_match_by_id(match_id)
    team_a = teams_repo.get_team_by_id(match.teamA_id)
    team_b = teams_repo.get_team_by_id(match.teamB_id)

    return {
        "id_match": match.id_match,
        "jornada": match.matchday,
        "fecha_hora": match.match_date_time,
        "phase": match.phase,
        "teamA": team_a.name,
        "teamB": team_b.name,
        "jugado": match.jugado,
        "goalsA": len(match.goalsA) if match.jugado else None,
        "scorersA": get_player_names_by_ids(match.goalsA),
        "goalsB": len(match.goalsB) if match.jugado else None,
        "scorersB": get_player_names_by_ids(match.goalsB),
        "yellow_cards": get_player_names_by_ids(match.yellow_cards),
        "red_cards": get_player_names_by_ids(match.red_cards),
    }


def get_standings(season: int) -> list[dict]:
    standings = {
        team.id_team: {
            "points": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "goalDifference": 0,
        }
        for team in teams_repo.team_list
    }

    for match in _get_played_matches(season):
        team_a = standings[match.teamA_id]
        team_b = standings[match.teamB_id]
        goals_a = len(match.goalsA)
        goals_b = len(match.goalsB)
        goal_difference = abs(goals_a - goals_b)

        if goals_a == goals_b:
            team_a["draws"] += 1
            team_a["points"] += 1
            team_b["draws"] += 1
            team_b["points"] += 1
        elif goals_a > goals_b:
            team_a["wins"] += 1
            team_a["points"] += 3
            team_a["goalDifference"] += goal_difference
            team_b["losses"] += 1
            team_b["goalDifference"] -= goal_difference
        else:
            team_b["wins"] += 1
            team_b["points"] += 3
            team_b["goalDifference"] += goal_difference
            team_a["losses"] += 1
            team_a["goalDifference"] -= goal_difference

    result = [
        {
            "team_id": team.id_team,
            "name": team.name,
            **standings[team.id_team],
        }
        for team in teams_repo.team_list
    ]

    result.sort(
        key=lambda team: (-team["points"], -team["goalDifference"])
    )
    return result


def get_player_names_by_ids(player_ids: list[int]) -> list[str]:
    return [
        player_service.get_player_by_id(player_id)["name"]
        for player_id in player_ids
    ]
