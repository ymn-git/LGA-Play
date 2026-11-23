from sqlalchemy.orm import Session
from repositories.teams_repository import TeamsRepository
from repositories.players_repository import PlayersRepository
from repositories.player_x_team_repository import PlayerXTeamsRepository
from repositories.coaches_repository import CoachesRepository
from repositories.coach_x_team_repository import CoachXTeamsRepository

from services import match_service
from schemas.team_schema import (
    TeamCreate,
    TeamUpdate
)

def get_all_teams(db: Session):
    teams_repo = TeamsRepository(db)
    return teams_repo.get_all_teams()

def get_team_by_id(id_team: int,db: Session):
    teams_repo = TeamsRepository(db)
    return teams_repo.get_team_by_id(id_team)

def create_team(team: TeamCreate,db: Session):
    teams_repo = TeamsRepository(db)
    return teams_repo.create_team(team.name)

def update_team_name(id_team: int,updated_team: TeamUpdate,db: Session):
    teams_repo = TeamsRepository(db)
    return teams_repo.update_team_name(id_team,updated_team.name)

def delete_team(id_team: int,db: Session):
    teams_repo = TeamsRepository(db)
    return teams_repo.delete_team(id_team)

def get_team_stats(team_id: int, season: int, db: Session):
    teams_repo = TeamsRepository(db)
    teams_repo.get_team_by_id(team_id)
    for row in match_service.get_standings(db,season):
        if row["id_team"] == team_id:
            return row
    raise ValueError("Team not found in standings")

def assign_player_to_team(team_id: int,player_id: int):
    teams_repo.get_team_by_id(team_id)
    players_repo.get_by_id(player_id)
    return player_x_team_repo.assign_player(player_id,team_id)

def assign_coach_to_team(coach_id: int,team_id: int):
    teams_repo.get_team_by_id(team_id)
    coaches_repo.get_by_id(coach_id)
    return coach_x_team_repo.assign_coach(coach_id,team_id)

def get_team_players(team_id: int):
    return player_x_team_repo.get_players_by_team(team_id)

def get_team_coach(team_id: int):
    return coach_x_team_repo.get_coaches_by_team(team_id)


def get_players_objects_by_team(
    team_id: int,
    db: Session
):
    teams_repo = TeamsRepository(db)
    players_repo = PlayersRepository(db)
    player_x_team_repo = PlayerXTeamsRepository(db)

    teams_repo.get_team_by_id(team_id)

    relations = player_x_team_repo.get_players_by_team(team_id)

    players = []

    for relation in relations:
        players.append(
            players_repo.get_by_id(
                relation.player_id
            )
        )

    return players

def get_coaches_objects_by_team(
    team_id: int,
    db: Session
):
    teams_repo = TeamsRepository(db)
    coaches_repo = CoachesRepository(db)
    coach_x_team_repo = CoachXTeamsRepository(db)

    teams_repo.get_team_by_id(team_id)

    relations = coach_x_team_repo.get_coaches_by_team(team_id)

    coaches = []

    for relation in relations:
        coaches.append(
            coaches_repo.get_by_id(
                relation.coach_id
            )
        )

    return coaches