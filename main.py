from fastapi import FastAPI
from controllers import player_controller, team_controller, match_controller

app = FastAPI()

app.include_router(player_controller.router)
app.include_router(team_controller.router)
app.include_router(match_controller.router)