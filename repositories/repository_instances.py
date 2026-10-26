
from repositories.players_repository import PlayersRepository
from repositories.teams_repository import TeamsRepository
from repositories.player_x_team_repository import PlayerXTeamsRepository
from repositories.matches_repository import MatchesRepository
from repositories.coaches_repository import CoachesRepository
from repositories.coach_x_team_repository import CoachXTeamsRepository

matches_repo = MatchesRepository()

players_repo = PlayersRepository()

teams_repo = TeamsRepository()

player_x_team_repo = PlayerXTeamsRepository()

coaches_repo = CoachesRepository()

coach_x_team_repo = CoachXTeamsRepository()