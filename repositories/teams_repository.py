from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from entities.team import Team


class TeamsRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_teams(self):
        return (
            self.db.query(Team)
            .order_by(Team.id_team)
            .all()
        )

    def get_team_by_id(self, id_team: int):
        team = self.db.get(Team,id_team)
        if team is None:
            raise ValueError("Team not found")
        return team

    def create_team(self, name: str):
        name = name.strip()
        if not name:
            raise ValueError("Team name cannot be empty")
        team = Team(name=name)
        try:
            self.db.add(team)
            self.db.commit()
            self.db.refresh(team)
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"Team '{name}' already exists")
        return team

    def update_team_name(self,id_team: int,new_name: str):
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Name cannot be empty")
        team = self.get_team_by_id(id_team)
        team.name = new_name
        try:
            self.db.commit()
            self.db.refresh(team)
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"Team '{new_name}' already exists")
        return team

    def delete_team(self, id_team: int):
        team = self.get_team_by_id(id_team)
        try:
            self.db.delete(team)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise ValueError("No se puede borrar: el equipo tiene partidos o jugadores")
        return team
