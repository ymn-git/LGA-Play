from entities.match import Match
import sqlite3

class MatchesRepository:
    def __init__(self, conn):
        self.conn = conn  # con conn.row_factory = sqlite3.Row

    def _build_matches(self, rows):
        "Convierte filas en Match, cargando goles en una sola query."
        if not rows:
            return []
        ids = [r["id_match"] for r in rows]
        marks = ",".join(["?"] * len(ids))
        goals = self.conn.execute(
            f"SELECT id_match, id_team, id_player, own_goal FROM goals "
            f"WHERE id_match IN ({marks})", ids
        ).fetchall()

        cards = self.conn.execute(
            f"SELECT id_match, id_player, type FROM cards WHERE id_match IN ({marks})", ids
        ).fetchall()
        yellow, red = {}, {}
        for c in cards:
            target = yellow if c["type"] == "yellow" else red
            target.setdefault(c["id_match"], []).append(c["id_player"])

        by_match = {}
        for g in goals:
            by_match.setdefault(g["id_match"], []).append({
                "team_id": g["id_team"],
                "player_id": g["id_player"],
                "own_goal": bool(g["own_goal"]),
            })

        return [
            Match(
                id_match=r["id_match"],
                teamA_id=r["team_a_id"],
                teamB_id=r["team_b_id"],
                matchday=r["matchday"],
                season=r["season"],
                full_date=r["full_date"],
                scorers=by_match.get(r["id_match"], []),
                yellow_cards=yellow.get(r["id_match"], []),
                red_cards=red.get(r["id_match"], []),
                jugado=bool(r["jugado"]),
            )
            for r in rows
        ]

    def get_match_by_id(self, match_id):
        rows = self.conn.execute(
            "SELECT * FROM matches WHERE id_match = ?", (match_id,)
        ).fetchall()
        if not rows:
            raise ValueError("Match not found")
        return self._build_matches(rows)[0]

    def get_matches_by_matchday(self, matchday, season):
        rows = self.conn.execute(
            "SELECT * FROM matches WHERE matchday = ? AND season = ? "
            "ORDER BY id_match", (matchday, season)
        ).fetchall()
        if not rows:
            raise ValueError(f"No matches found for matchday {matchday}")
        return self._build_matches(rows)

    def get_played_matches_by_season(self, season):
        rows = self.conn.execute(
            "SELECT * FROM matches WHERE season = ? AND jugado = 1", (season,)
        ).fetchall()
        return self._build_matches(rows)

    def get_played_matches_by_team(self, team_id, season, limit=None):
        sql = ("SELECT * FROM matches WHERE season = ? AND jugado = 1 "
               "AND (team_a_id = ? OR team_b_id = ?) ORDER BY matchday DESC")
        params = [season, team_id, team_id]
        if limit:
            sql += " LIMIT ?"
            params.append(limit)
        return self._build_matches(self.conn.execute(sql, params).fetchall())

    def update_match(self, match: Match):
        with self.conn:
            self.conn.execute(
                "UPDATE matches SET jugado = ? WHERE id_match = ?",
                (int(match.jugado), match.id_match),
            )
            self.conn.execute("DELETE FROM goals WHERE id_match = ?", (match.id_match,))
            self.conn.executemany(
                "INSERT INTO goals (id_match, id_team, id_player, own_goal) VALUES (?, ?, ?, ?)",
                [(match.id_match, g["team_id"], g["player_id"], int(g["own_goal"]))
                 for g in match.scorers],
            )
            self.conn.execute("DELETE FROM cards WHERE id_match = ?", (match.id_match,))
            self.conn.executemany(
                "INSERT INTO cards (id_match, id_player, type) VALUES (?, ?, ?)",
                [(match.id_match, p, "yellow") for p in match.yellow_cards]
                + [(match.id_match, p, "red") for p in match.red_cards],
            )
        return match

    def mark_match_as_played(self, match_id):
        match = self.get_match_by_id(match_id)  # ValueError si no existe
        with self.conn:
            self.conn.execute(
                "UPDATE matches SET jugado = 1 WHERE id_match = ?", (match_id,)
            )
        match.jugado = True
        return match

    def get_next_matchday(self, season):
        row = self.conn.execute(
            "SELECT MIN(matchday) AS md FROM matches WHERE season = ? AND jugado = 0",
            (season,),
        ).fetchone()
        return row["md"]  # None si la temporada terminó