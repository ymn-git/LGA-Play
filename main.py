from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import player_controller, team_controller, match_controller, season_stats_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://lga-play-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player_controller.router)
app.include_router(team_controller.router)
app.include_router(match_controller.router)
app.include_router(season_stats_controller.router)
