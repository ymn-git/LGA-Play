import sqlite3
from entities.team import Team


class TeamsRepository:
    def __init__(self, conn):
        self.conn = conn

    def _to_team(self, row):
        return Team(row["id_team"], row["name"])

    def get_all_teams(self):
        rows = self.conn.execute(
            "SELECT id_team, name FROM teams ORDER BY id_team"
        ).fetchall()
        return [self._to_team(r) for r in rows]

    def get_team_by_id(self, id_team: int):
        row = self.conn.execute(
            "SELECT id_team, name FROM teams WHERE id_team = ?", (id_team,)
        ).fetchone()
        if not row:
            raise ValueError(f"Team with id {id_team} not found")
        return self._to_team(row)

    def create_team(self, team_data: dict):
        name = (team_data.get("name") or "").strip()
        if not name:
            raise ValueError("Team must include a 'name'")
        try:
            with self.conn:
                cursor = self.conn.execute(
                    "INSERT INTO teams (name) VALUES (?)", (name,)
                )
        except sqlite3.IntegrityError:
            raise ValueError(f"Team '{name}' already exists")
        return Team(cursor.lastrowid, name)

    def update_team_name(self, id_team: int, new_name: str):
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Name cannot be empty")
        self.get_team_by_id(id_team)  # ValueError si no existe
        try:
            with self.conn:
                self.conn.execute(
                    "UPDATE teams SET name = ? WHERE id_team = ?",
                    (new_name, id_team),
                )
        except sqlite3.IntegrityError:
            raise ValueError(f"Team '{new_name}' already exists")
        return Team(id_team, new_name)

    def delete_team(self, id_team: int):
        team = self.get_team_by_id(id_team)
        try:
            with self.conn:
                self.conn.execute("DELETE FROM teams WHERE id_team = ?", (id_team,))
        except sqlite3.IntegrityError:
            raise ValueError("No se puede borrar: el equipo tiene partidos o jugadores")
        return team






