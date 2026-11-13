from entities.match import Match
from Schemas.match_schema import MatchResultUpdate
from repositories.repository_instances import (
    teams_repo,
    matches_repo
)

def get_match_by_id(match_id):
    return _with_score(matches_repo.get_match_by_id(match_id))

def get_matches_by_matchday(matchday: int, season: int):
    return [
        _with_score(m)
        for m in matches_repo.get_matches_by_matchday(matchday, season)
    ]

def get_match_result(id_match: int):
    return get_match_by_id(id_match)

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

def update_match_result(id_match: int, payload: MatchResultUpdate):
    match = matches_repo.get_match_by_id(id_match)

    for g in payload.scorers:
        if g.team_id not in (match.teamA_id, match.teamB_id):
            raise ValueError(f"Team {g.team_id} no juega este partido")

    match.scorers = [g.model_dump() for g in payload.scorers] #.model_dump desempaqueta en clave/valor
    match.yellow_cards = payload.yellow_cards
    match.red_cards = payload.red_cards
    match.goalsA, match.goalsB = calculate_score(match)
    match.jugado = True
    return matches_repo.update_match(match)

def get_standings(season_id: int):
    table = {
        t.id_team: {
            "id_team": t.id_team, "name": t.name, "played": 0, "wins": 0,
            "draws": 0, "losses": 0, "gf": 0, "ga": 0, "points": 0,
        }
        for t in teams_repo.get_all_teams()
    }

    for match in matches_repo.get_played_matches_by_season(season_id):
        goalsA, goalsB = calculate_score(match)
        for team_id, gf, ga in (
            (match.teamA_id, goalsA, goalsB),
            (match.teamB_id, goalsB, goalsA),
        ):
            row = table[team_id]
            row["played"] += 1
            row["gf"] += gf
            row["ga"] += ga
            if gf > ga:
                row["wins"] += 1
                row["points"] += 3
            elif gf == ga:
                row["draws"] += 1
                row["points"] += 1
            else:
                row["losses"] += 1

    for row in table.values():
        row["goal_difference"] = row["gf"] - row["ga"]

    rows = sorted(
        table.values(),
        key=lambda r: (r["points"], r["goal_difference"], r["gf"]),
        reverse=True,
    )
    for pos, row in enumerate(rows, start=1):
        row["position"] = pos
    return rows

def get_next_matches(season_id: int):
    matchday = matches_repo.get_next_matchday(season_id)
    if matchday is None:
        raise ValueError("La temporada ya terminó")
    return matches_repo.get_matches_by_matchday(matchday, season_id)

def get_qualified(season_id: int):
    return get_standings(season_id)[:8] #devuelve los primeros 8

def _with_score(match: Match):
    match.goalsA, match.goalsB = calculate_score(match)
    return match
