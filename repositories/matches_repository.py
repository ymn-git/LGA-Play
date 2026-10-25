import sqlite3
from datetime import date, datetime

from database import get_connection
from entities.goal import Goal
from entities.match import Match


class MatchesRepository:
    def get_match_by_id(self, match_id: int) -> Match:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        try:
            row = conn.execute(
                "SELECT * FROM matches WHERE id_match = ?",
                (match_id,),
            ).fetchone()
            if row is None:
                raise ValueError(f"Match {match_id} not found")
            return self._row_to_match(conn, row)
        finally:
            conn.close()

    def get_all(self) -> list[Match]:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                "SELECT * FROM matches ORDER BY id_match"
            ).fetchall()
            return [self._row_to_match(conn, row) for row in rows]
        finally:
            conn.close()

    def get_matches_by_matchday(
        self, season: int, matchday: int
    ) -> list[Match]:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                """
                SELECT * FROM matches
                WHERE season = ? AND matchday = ?
                ORDER BY id_match
                """,
                (season, matchday),
            ).fetchall()
            if not rows:
                raise ValueError(
                    f"No matches found for season {season}, matchday {matchday}"
                )
            return [self._row_to_match(conn, row) for row in rows]
        finally:
            conn.close()

    def get_played_matches_by_season(self, season: int) -> list[Match]:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                """
                SELECT * FROM matches
                WHERE season = ? AND played = 1
                ORDER BY id_match
                """,
                (season,),
            ).fetchall()
            return [self._row_to_match(conn, row) for row in rows]
        finally:
            conn.close()

    def get_matches_by_date(self, season: int, match_date: date) -> list[Match]:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        try:
            rows = conn.execute(
                """
                SELECT * FROM matches
                WHERE season = ? AND date(match_date_time) = ?
                ORDER BY match_date_time, id_match
                """,
                (season, match_date.isoformat()),
            ).fetchall()
            if not rows:
                raise ValueError(f"No matches found for date {match_date}")
            return [self._row_to_match(conn, row) for row in rows]
        finally:
            conn.close()

    def get_standings_raw(self, season: int) -> dict:
        standings = {}
        for match in self.get_played_matches_by_season(season):
            for team_id in (match.teamA_id, match.teamB_id):
                standings.setdefault(team_id, {
                    "points": 0,
                    "wins": 0,
                    "losses": 0,
                    "draws": 0,
                    "goalDifference": 0,
                })

            if match.result is None:
                for team_id in (match.teamA_id, match.teamB_id):
                    standings[team_id]["draws"] += 1
                    standings[team_id]["points"] += 1
                continue

            winner, loser = match.result
            standings[winner]["wins"] += 1
            standings[winner]["points"] += 3
            standings[winner]["goalDifference"] += match.goal_difference
            standings[loser]["losses"] += 1
            standings[loser]["goalDifference"] -= match.goal_difference

        return standings

    def get_yellow_cards_by_player_season(
        self, season: int, player_id: int
    ) -> int:
        return self._get_cards_by_player_season(season, player_id, "yellow")

    def get_red_cards_by_player_season(
        self, season: int, player_id: int
    ) -> int:
        return self._get_cards_by_player_season(season, player_id, "red")

    def _get_cards_by_player_season(
        self, season: int, player_id: int, card_type: str
    ) -> int:
        conn = get_connection()
        try:
            row = conn.execute(
                """
                SELECT COUNT(*)
                FROM cards
                JOIN matches ON matches.id_match = cards.id_match
                WHERE matches.season = ?
                    AND matches.played = 1
                    AND cards.id_player = ?
                    AND cards.type = ?
                """,
                (season, player_id, card_type),
            ).fetchone()
            return row[0]
        finally:
            conn.close()

    def update_match(self, match: Match) -> Match:
        conn = get_connection()
        try:
            conn.execute("BEGIN")

            row = conn.execute(
                "SELECT id_match FROM matches WHERE id_match = ?",
                (match.id_match,),
            ).fetchone()
            if row is None:
                raise ValueError(f"Match {match.id_match} not found")

            conn.execute(
                "UPDATE matches SET played = ? WHERE id_match = ?",
                (int(match.jugado), match.id_match),
            )
            conn.execute(
                "DELETE FROM goals WHERE id_match = ?",
                (match.id_match,),
            )
            conn.execute(
                "DELETE FROM cards WHERE id_match = ?",
                (match.id_match,),
            )

            for goal in match.goals:
                conn.execute(
                    """
                    INSERT INTO goals (id_match, id_team, id_player, own_goal)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        match.id_match,
                        goal.id_team,
                        goal.id_player,
                        int(goal.own_goal),
                    ),
                )

            for player_id in match.yellow_cards:
                conn.execute(
                    """
                    INSERT INTO cards (id_match, id_player, type)
                    VALUES (?, ?, ?)
                    """,
                    (match.id_match, player_id, "yellow"),
                )

            for player_id in match.red_cards:
                conn.execute(
                    """
                    INSERT INTO cards (id_match, id_player, type)
                    VALUES (?, ?, ?)
                    """,
                    (match.id_match, player_id, "red"),
                )

            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

        return self.get_match_by_id(match.id_match)

    def _row_to_match(self, conn: sqlite3.Connection, row: sqlite3.Row) -> Match:
        goal_rows = conn.execute(
            """
            SELECT id_team, id_player, own_goal
            FROM goals
            WHERE id_match = ?
            ORDER BY id
            """,
            (row["id_match"],),
        ).fetchall()
        card_rows = conn.execute(
            """
            SELECT id_player, type
            FROM cards
            WHERE id_match = ?
            ORDER BY id
            """,
            (row["id_match"],),
        ).fetchall()

        yellow_cards = []
        red_cards = []
        for card in card_rows:
            if card["type"] == "yellow":
                yellow_cards.append(card["id_player"])
            elif card["type"] == "red":
                red_cards.append(card["id_player"])

        return Match(
            id_match=row["id_match"],
            teamA_id=row["team_a_id"],
            teamB_id=row["team_b_id"],
            matchday=row["matchday"],
            match_date_time=(
                datetime.fromisoformat(row["match_date_time"])
                if row["match_date_time"]
                else None
            ),
            season=row["season"],
            goals=[
                Goal(
                    id_team=goal["id_team"],
                    id_player=goal["id_player"],
                    own_goal=bool(goal["own_goal"]),
                )
                for goal in goal_rows
            ],
            yellow_cards=yellow_cards,
            red_cards=red_cards,
            jugado=bool(row["played"]),
            phase=row["phase"],
        )
