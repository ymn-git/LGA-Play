from sqlalchemy.orm import Session

from entities.player import Player

from schemas.player_schema import (
    PlayerCreate,
    PlayerUpdate
)

from repositories.players_repository import PlayersRepository
from repositories.teams_repository import TeamsRepository
from repositories.player_x_team_repository import PlayerXTeamsRepository

def get_players(db: Session):
    players_repo = PlayersRepository(db)
    return players_repo.get_all()

def get_player_by_id(id_player: int,db: Session):
    players_repo = PlayersRepository(db)
    return players_repo.get_by_id(id_player)

def create_player(player: PlayerCreate,db: Session):
    players_repo = PlayersRepository(db)
    new_player = Player(id_player=player.dni,name=player.name,position=player.position)
    return players_repo.create(new_player)

def put_player(
    id_player: int,
    updated_player: PlayerUpdate,
    db: Session
):
    players_repo = PlayersRepository(db)
    player = Player(id_player=id_player,name=updated_player.name,position=updated_player.position)
    return players_repo.update_full(id_player,player)

def patch_player(
    id_player: int,
    name=None,
    position=None,
    db: Session = None
):
    players_repo = PlayersRepository(db)
    return players_repo.update_partial(id_player,name,position)

def delete_player(id_player: int,db: Session):
    players_repo = PlayersRepository(db)
    return players_repo.delete(id_player)

def transfer_player(player_id: int,new_team_id: int,db: Session):
    player_x_team_repo = PlayerXTeamsRepository(db)
    current_team = (player_x_team_repo.get_active_team(player_id))
    if not current_team:
        raise ValueError("Player has no active team")
    player_x_team_repo.deactivate_relation(player_id)
    return player_x_team_repo.assign_player(player_id,new_team_id)

def get_current_team_of_player(player_id: int,db: Session):
    player_x_team_repo = PlayerXTeamsRepository(db)
    teams_repo = TeamsRepository(db)
    relation = (player_x_team_repo.get_active_team(player_id))
    if relation is None:
        return None
    return teams_repo.get_team_by_id(relation.team_id)

def get_player_stats(id_player: int,db: Session,season=None):
    players_repo = PlayersRepository(db)
    return players_repo.get_stats(id_player,season)