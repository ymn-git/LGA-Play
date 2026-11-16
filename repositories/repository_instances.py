from app.database import SessionLocal
from repositories.coaches_repository import CoachesRepository
from repositories.coach_x_team_repository import CoachXTeamsRepository
from repositories.players_repository import PlayersRepository
from repositories.player_x_team_repository import PlayerXTeamsRepository
from repositories.teams_repository import TeamsRepository
from repositories.matches_repository import MatchesRepository
from repositories.users_repository import UserRepository
from repositories.playoff_repository import PlayoffRepository

db = SessionLocal()

teams_repo = TeamsRepository(db)
players_repo = PlayersRepository(db)
coaches_repo = CoachesRepository(db)

matches_repo = MatchesRepository(db)

player_x_team_repo = PlayerXTeamsRepository(db)
coach_x_team_repo = CoachXTeamsRepository(db)

users_repo = UserRepository(db)
playoff_repo = PlayoffRepository(db)

