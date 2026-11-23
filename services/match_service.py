from collections import Counter
from sqlalchemy.orm import Session

from entities.match import Match
from schemas.match_schema import MatchResultUpdate

from repositories.teams_repository import TeamsRepository
from repositories.matches_repository import MatchesRepository
from repositories.playoff_repository import PlayoffRepository


def get_repositories(db: Session):
    return (
        TeamsRepository(db),
        MatchesRepository(db),
        PlayoffRepository(db)
    )

def get_match_by_id(db: Session, match_id):
    _, matches_repo, _ = get_repositories(db)

    return with_score(
        matches_repo.get_match_by_id(match_id)
    )

def get_matches_by_matchday(
    db: Session,
    matchday: int,
    season: int
):
    _, matches_repo, _ = get_repositories(db)

    return [
        with_score(m)
        for m in matches_repo.get_matches_by_matchday(
            matchday,
            season
        )
    ]


def get_match_result(
    db: Session,
    id_match: int
):
    return get_match_by_id(
        db,
        id_match
    )

def get_top_scorers(
    db: Session,
    season_id: int
):
    _, matches_repo, _ = get_repositories(db)

    matches = matches_repo.get_played_matches_by_season(
        season_id
    )

    contador = {}

    for match in matches:
        for goal in match.scorers:

            if goal["own_goal"]:
                continue

            player_id = goal["player_id"]

            contador[player_id] = (
                contador.get(player_id, 0) + 1
            )

    return sorted(
        contador.items(),
        key=lambda x: x[1],
        reverse=True
    )

def mark_match_as_played(
    db: Session,
    match_id
):
    _, matches_repo, _ = get_repositories(db)

    return matches_repo.mark_match_as_played(
        match_id
    )


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

def update_match_result(
    db: Session,
    id_match: int,
    payload: MatchResultUpdate
):
    _, matches_repo, _ = get_repositories(db)

    try:
        match = matches_repo.get_match_by_id(id_match)
    except ValueError as exc:
        raise LookupError("Match not found") from exc
    for g in payload.scorers:
        if g.team_id not in (match.teamA_id, match.teamB_id):
            raise ValueError(f"Team {g.team_id} no juega este partido")

    match.scorers = [g.model_dump() for g in payload.scorers]  # .model_dump desempaqueta en clave/valor
    match.yellow_cards = payload.yellow_cards
    match.red_cards = payload.red_cards
    yellow_counts = Counter(match.yellow_cards)
    for player_id, count in yellow_counts.items():
        if count >= 2 and player_id not in match.red_cards:
            match.red_cards.append(player_id)
    match.goalsA, match.goalsB = calculate_score(match)
    match.jugado = True
    return matches_repo.update_match(match)

def get_standings(
    db: Session,
    season_id: int
):
    teams_repo, matches_repo, _ = get_repositories(db)

    table = {
        t.id_team: {
            "id_team": t.id_team,
            "name": t.name,
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "gf": 0,
            "ga": 0,
            "points": 0,
        }
        for t in teams_repo.get_all_teams()
    }

    for match in matches_repo.get_played_matches_by_season(season_id, include_playoffs=False):
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

def get_next_matches(
    db: Session,
    season_id: int
):
    _, matches_repo, _ = get_repositories(db)

    matchday = matches_repo.get_next_matchday(
        season_id
    )

    if matchday is None:
        raise ValueError(
            "La temporada ya terminó"
        )

    return matches_repo.get_matches_by_matchday(
        matchday,
        season_id
    )

def get_qualified(
    db: Session,
    season_id: int
):
    return get_standings(
        db,
        season_id
    )[:8]  # devuelve los primeros 8

def with_score(match: Match):
    match.goalsA, match.goalsB = calculate_score(match)
    return match

def get_playoff_bracket(
    db: Session,
    season,
    phase,
    bracket_group
):
    _, _, playoff_repo = get_repositories(db)

    playoffs = playoff_repo.get_by_bracket(
        season,
        phase,
        bracket_group
    )

    return [p.match for p in playoffs]

from sqlalchemy import and_, or_

def create_match(
    db: Session,
    season,
    matchday,
    team_a_id,
    team_b_id,
    full_date
):
    _, matches_repo, _ = get_repositories(db)

    if team_a_id == team_b_id:
        raise ValueError(
            "Un equipo no puede jugar contra sí mismo"
        )

    existing_match = (
        db.query(Match)
        .filter(
            Match.season == season,
            Match.matchday == matchday,
            or_(
                and_(
                    Match.teamA_id == team_a_id,
                    Match.teamB_id == team_b_id
                ),
                and_(
                    Match.teamA_id == team_b_id,
                    Match.teamB_id == team_a_id
                )
            )
        )
        .first()
    )

    if existing_match:
        raise ValueError(
            "Ya existe un partido entre esos equipos para esta fecha"
        )

    match = matches_repo.add(
        team_a_id,
        team_b_id,
        matchday,
        season,
        full_date
    )

    db.commit()

    return matches_repo.get_match_by_id(
        match.id_match
    )

SINGLE_LEG_PHASES = {"final", "finalisima"}

def create_playoff_match(
    db: Session,
    season,
    phase,
    bracket_group,
    leg,
    team_a_id,
    team_b_id,
    full_date,
    matchday=0
):

    _, matches_repo, playoff_repo = get_repositories(db)

    if leg not in (1, 2):
        raise ValueError(
            "leg debe ser 1 o 2"
        )

    if phase in SINGLE_LEG_PHASES and leg != 1:
        raise ValueError(
            f"{phase} es partido único (leg=1)"
        )

    if team_a_id == team_b_id:
        raise ValueError(
            "Un equipo no puede jugar contra sí mismo"
        )

    if playoff_repo.leg_exists(
        season,
        phase,
        bracket_group,
        leg
    ):
        raise ValueError(
            "Ya existe ese partido en la llave"
        )

    existing_matches = playoff_repo.get_by_bracket(
        season,
        phase,
        bracket_group
    )

    if leg == 2 and not existing_matches:
        raise ValueError(
            "No puede existir una vuelta sin ida previa"
        )

    if existing_matches:

        ida = next(
            (p for p in existing_matches if p.leg == 1),
            None
        )

        if leg == 2 and ida:

            if (
                ida.match.teamA_id != team_b_id
                or
                ida.match.teamB_id != team_a_id
            ):
                raise ValueError(
                    "La vuelta debe invertir las localías de la ida"
                )

        if ida:

            equipos_ida = {
                ida.match.teamA_id,
                ida.match.teamB_id
            }

            equipos_nuevos = {
                team_a_id,
                team_b_id
            }

            if equipos_ida != equipos_nuevos:
                raise ValueError(
                    "La vuelta debe involucrar los mismos equipos que la ida"
                )

    try:

        match = matches_repo.add(
            team_a_id,
            team_b_id,
            matchday,
            season,
            full_date
        )

        playoff_repo.add(
            match.id_match,
            season,
            phase,
            bracket_group,
            leg
        )

        db.commit()

    except Exception:

        db.rollback()
        raise

    return matches_repo.get_match_by_id(
        match.id_match
    )

def update_playoff_penalties(
    db: Session,
    match_id: int,
    penaltiesA: int,
    penaltiesB: int
):
    _, _, playoff_repo = get_repositories(db)

    if penaltiesA < 0 or penaltiesB < 0:
        raise ValueError(
            "Los penales no pueden ser negativos"
        )

    if penaltiesA == penaltiesB:
        raise ValueError(
            "Una definición por penales no puede terminar empatada"
        )

    return playoff_repo.update_penalties(
        match_id,
        penaltiesA,
        penaltiesB
    )
