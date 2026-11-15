
from repositories.players_repository import PlayersRepository
from repositories.teams_repository import TeamsRepository
from repositories.player_x_team_repository import PlayerXTeamsRepository
from repositories.matches_repository import MatchesRepository
from repositories.coaches_repository import CoachesRepository
from repositories.coach_x_team_repository import CoachXTeamsRepository

import sqlite3

conn = sqlite3.connect("nombre_base_datos.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
conn.execute("PRAGMA foreign_keys = ON")#evita borrar algo que tenga FK

matches_repo = MatchesRepository(conn)
players_repo = PlayersRepository()

teams_repo = TeamsRepository(conn)

player_x_team_repo = PlayerXTeamsRepository()

coaches_repo = CoachesRepository()

coach_x_team_repo = CoachXTeamsRepository()

