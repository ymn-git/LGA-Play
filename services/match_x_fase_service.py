from typing import Optional, List
from sqlalchemy.orm import Session
from repositories.match_x_fase_repository import MatchXFaseRepository
from models.match import Match

def get_regular_matches_by_matchday(db: Session, matchday: int, season: int = 2026):
    repo = MatchXFaseRepository(db)
    matches = repo.get_regular_matches_by_matchday(matchday, season)
    return [format_match(m) for m in matches]

def get_all_regular_matches(db: Session, season: int = 2026):
    repo = MatchXFaseRepository(db)
    matches = repo.get_all_regular_matches(season)
    return [format_match(m) for m in matches]

def get_playoff_matches(db: Session, season: int = 2026):
    repo = MatchXFaseRepository(db)
    matches = repo.get_playoff_matches_by_season(season)
    return [format_match(m) for m in matches]

def create_regular_match(db: Session, data: dict):
    repo = MatchXFaseRepository(db)
    match = repo.create_regular_match(
        teamA_id=data["teamA_id"],
        teamB_id=data["teamB_id"],
        matchday=data["matchday"],
        season=data.get("season", 2026),
        match_date=data.get("match_date")
    )
    return format_match(match)

def create_playoff_match(db: Session, data: dict):
    repo = MatchXFaseRepository(db)
    match = repo.create_playoff_match(
        teamA_id=data["teamA_id"],
        teamB_id=data["teamB_id"],
        round_name=data["round_name"],
        bracket_order=data["bracket_order"],
        season=data.get("season", 2026),
        match_date=data.get("match_date")
    )
    return format_match(match)

def update_playoff_result(db: Session, match_id: int, data: dict):
    repo = MatchXFaseRepository(db)
    match = repo.update_playoff_result(
        match_id=match_id,
        goalsA=data["goalsA"],
        goalsB=data["goalsB"],
        winner_id=data["winner_id"],
        penaltiesA=data.get("penaltiesA"),
        penaltiesB=data.get("penaltiesB"),
        scorers=data.get("scorers"),
        yellow_cards=data.get("yellow_cards"),
        red_cards=data.get("red_cards")
    )
    return format_match(match)

def format_match(match: Match) -> dict:
    fase_info = match.fase_info
    return {
        "id_match": match.id,
        "teamA_id": match.teamA_id,
        "teamB_id": match.teamB_id,
        "teamAName": match.teamA.name if match.teamA else f"Equipo {match.teamA_id}",
        "teamBName": match.teamB.name if match.teamB else f"Equipo {match.teamB_id}",
        "season": match.season,
        "match_date": match.match_date,
        "goalsA": match.goalsA,
        "goalsB": match.goalsB,
        "jugado": match.jugado,
        "scorers": match.scorers or [],
        "yellow_cards": match.yellow_cards or [],
        "red_cards": match.red_cards or [],
        # Datos de la tabla intermedia
        "tipo_fase": fase_info.tipo_fase if fase_info else "REGULAR",
        "matchday": fase_info.matchday if fase_info else None,
        "round_name": fase_info.round_name if fase_info else None,
        "bracket_order": fase_info.bracket_order if fase_info else None,
        "penaltiesA": fase_info.penaltiesA if fase_info else None,
        "penaltiesB": fase_info.penaltiesB if fase_info else None,
        "winner_id": fase_info.winner_id if fase_info else None,
    }
