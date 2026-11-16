# Importar entidades para que SQLAlchemy registre las tablas
from entities.team import Team
from entities.player import Player
from entities.coach import Coach
from entities.match import Match
from entities.goal import Goal
from entities.card import Card
from entities.player_x_team import PlayerXTeam
from entities.coach_x_team import CoachXTeam
from entities.playoff import Playoff
from models.user import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from controllers import (
    player_controller,
    team_controller,
    match_controller,
    coach_controller,
    user_controller,
)

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://lga-play-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player_controller.router)
app.include_router(team_controller.router)
app.include_router(match_controller.router)
app.include_router(coach_controller.router)
app.include_router(user_controller.router)