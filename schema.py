import sqlite3


def create_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS teams (
            id_team INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS persons (
            id_person INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            role TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS players (
            id_person INTEGER PRIMARY KEY
                REFERENCES persons (id_person),
            position TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS player_teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER NOT NULL
                REFERENCES players (id_person),
            id_team INTEGER NOT NULL
                REFERENCES teams (id_team),
            start_date TEXT NOT NULL,
            end_date TEXT
        );

        CREATE TABLE IF NOT EXISTS matches (
            id_match INTEGER PRIMARY KEY,
            team_a_id INTEGER NOT NULL REFERENCES teams (id_team),
            team_b_id INTEGER NOT NULL REFERENCES teams (id_team),
            matchday INTEGER NOT NULL,
            match_date_time TEXT NOT NULL,
            season INTEGER NOT NULL,
            played INTEGER NOT NULL DEFAULT 0,
            phase TEXT NOT NULL DEFAULT 'regular'
        );

        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_match INTEGER NOT NULL REFERENCES matches (id_match),
            id_team INTEGER NOT NULL REFERENCES teams (id_team),
            id_player INTEGER NOT NULL REFERENCES players (id_person),
            own_goal INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_match INTEGER NOT NULL REFERENCES matches (id_match),
            id_player INTEGER NOT NULL REFERENCES players (id_person),
            type TEXT NOT NULL
        );
        """
    )
