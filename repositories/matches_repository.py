from entities.match import Match

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


"""

INSERT INTO matches VALUES (1,1,7,1,0,0,0);
INSERT INTO matches VALUES (2,4,8,1,0,0,0);
INSERT INTO matches VALUES (3,5,9,1,0,0,0);
INSERT INTO matches VALUES (4,6,10,1,0,0,0);
INSERT INTO matches VALUES (5,12,11,1,0,0,0);
INSERT INTO matches VALUES (6,3,2,1,0,0,0);

INSERT INTO matches VALUES (7,2,11,2,0,0,0);
INSERT INTO matches VALUES (8,10,12,2,0,0,0);
INSERT INTO matches VALUES (9,9,6,2,0,0,0);
INSERT INTO matches VALUES (10,8,5,2,0,0,0);
INSERT INTO matches VALUES (11,7,4,2,0,0,0);
INSERT INTO matches VALUES (12,3,1,2,0,0,0);

INSERT INTO matches VALUES (13,1,2,3,0,0,0);
INSERT INTO matches VALUES (14,4,3,3,0,0,0);
INSERT INTO matches VALUES (15,5,7,3,0,0,0);
INSERT INTO matches VALUES (16,6,8,3,0,0,0);
INSERT INTO matches VALUES (17,12,9,3,0,0,0);
INSERT INTO matches VALUES (18,11,10,3,0,0,0);

INSERT INTO matches VALUES (19,2,10,4,0,0,0);
INSERT INTO matches VALUES (20,9,11,4,0,0,0);
INSERT INTO matches VALUES (21,8,12,4,0,0,0);
INSERT INTO matches VALUES (22,7,6,4,0,0,0);
INSERT INTO matches VALUES (23,3,5,4,0,0,0);
INSERT INTO matches VALUES (24,4,1,4,0,0,0);

INSERT INTO matches VALUES (25,4,2,5,0,0,0);
INSERT INTO matches VALUES (26,1,5,5,0,0,0);
INSERT INTO matches VALUES (27,6,3,5,0,0,0);
INSERT INTO matches VALUES (28,11,8,5,0,0,0);
INSERT INTO matches VALUES (29,10,9,5,0,0,0);
INSERT INTO matches VALUES (30,12,7,5,0,0,0);

INSERT INTO matches VALUES (31,2,9,6,0,0,0);
INSERT INTO matches VALUES (32,8,10,6,0,0,0);
INSERT INTO matches VALUES (33,7,11,6,0,0,0);
INSERT INTO matches VALUES (34,3,12,6,0,0,0);
INSERT INTO matches VALUES (35,6,1,6,0,0,0);
INSERT INTO matches VALUES (36,4,5,6,0,0,0);

INSERT INTO matches VALUES (37,5,2,7,0,0,0);
INSERT INTO matches VALUES (38,6,4,7,0,0,0);
INSERT INTO matches VALUES (39,1,12,7,0,0,0);
INSERT INTO matches VALUES (40,11,3,7,0,0,0);
INSERT INTO matches VALUES (41,10,7,7,0,0,0);
INSERT INTO matches VALUES (42,9,8,7,0,0,0);

INSERT INTO matches VALUES (43,8,2,8,0,0,0);
INSERT INTO matches VALUES (44,7,9,8,0,0,0);
INSERT INTO matches VALUES (45,3,10,8,0,0,0);
INSERT INTO matches VALUES (46,1,11,8,0,0,0);
INSERT INTO matches VALUES (47,4,12,8,0,0,0);
INSERT INTO matches VALUES (48,5,6,8,0,0,0);

INSERT INTO matches VALUES (49,6,2,9,0,0,0);
INSERT INTO matches VALUES (50,12,5,9,0,0,0);
INSERT INTO matches VALUES (51,11,4,9,0,0,0);
INSERT INTO matches VALUES (52,10,1,9,0,0,0);
INSERT INTO matches VALUES (53,9,3,9,0,0,0);
INSERT INTO matches VALUES (54,8,7,9,0,0,0);

INSERT INTO matches VALUES (55,2,7,10,0,0,0);
INSERT INTO matches VALUES (56,3,8,10,0,0,0);
INSERT INTO matches VALUES (57,1,9,10,0,0,0);
INSERT INTO matches VALUES (58,4,10,10,0,0,0);
INSERT INTO matches VALUES (59,5,11,10,0,0,0);
INSERT INTO matches VALUES (60,6,12,10,0,0,0);

INSERT INTO matches VALUES (61,12,2,11,0,0,0);
INSERT INTO matches VALUES (62,11,6,11,0,0,0);
INSERT INTO matches VALUES (63,10,5,11,0,0,0);
INSERT INTO matches VALUES (64,9,4,11,0,0,0);
INSERT INTO matches VALUES (65,8,1,11,0,0,0);
INSERT INTO matches VALUES (66,7,3,11,0,0,0);

INSERT INTO matches VALUES (67,7,1,12,0,0,0);
INSERT INTO matches VALUES (68,8,4,12,0,0,0);
INSERT INTO matches VALUES (69,9,5,12,0,0,0);
INSERT INTO matches VALUES (70,10,6,12,0,0,0);
INSERT INTO matches VALUES (71,11,12,12,0,0,0);
INSERT INTO matches VALUES (72,2,3,12,0,0,0);

INSERT INTO matches VALUES (73,11,2,13,0,0,0);
INSERT INTO matches VALUES (74,12,10,13,0,0,0);
INSERT INTO matches VALUES (75,6,9,13,0,0,0);
INSERT INTO matches VALUES (76,5,8,13,0,0,0);
INSERT INTO matches VALUES (77,4,7,13,0,0,0);
INSERT INTO matches VALUES (78,1,3,13,0,0,0);

INSERT INTO matches VALUES (79,2,1,14,0,0,0);
INSERT INTO matches VALUES (80,3,4,14,0,0,0);
INSERT INTO matches VALUES (81,7,5,14,0,0,0);
INSERT INTO matches VALUES (82,8,6,14,0,0,0);
INSERT INTO matches VALUES (83,9,12,14,0,0,0);
INSERT INTO matches VALUES (84,10,11,14,0,0,0);

INSERT INTO matches VALUES (85,10,2,15,0,0,0);
INSERT INTO matches VALUES (86,11,9,15,0,0,0);
INSERT INTO matches VALUES (87,12,8,15,0,0,0);
INSERT INTO matches VALUES (88,6,7,15,0,0,0);
INSERT INTO matches VALUES (89,5,3,15,0,0,0);
INSERT INTO matches VALUES (90,1,4,15,0,0,0);

INSERT INTO matches VALUES (91,2,4,16,0,0,0);
INSERT INTO matches VALUES (92,5,1,16,0,0,0);
INSERT INTO matches VALUES (93,3,6,16,0,0,0);
INSERT INTO matches VALUES (94,8,11,16,0,0,0);
INSERT INTO matches VALUES (95,9,10,16,0,0,0);
INSERT INTO matches VALUES (96,7,12,16,0,0,0);

INSERT INTO matches VALUES (97,9,2,17,0,0,0);
INSERT INTO matches VALUES (98,10,8,17,0,0,0);
INSERT INTO matches VALUES (99,11,7,17,0,0,0);
INSERT INTO matches VALUES (100,12,3,17,0,0,0);
INSERT INTO matches VALUES (101,1,6,17,0,0,0);
INSERT INTO matches VALUES (102,5,4,17,0,0,0);

INSERT INTO matches VALUES (103,2,5,18,0,0,0);
INSERT INTO matches VALUES (104,4,6,18,0,0,0);
INSERT INTO matches VALUES (105,12,1,18,0,0,0);
INSERT INTO matches VALUES (106,3,11,18,0,0,0);
INSERT INTO matches VALUES (107,7,10,18,0,0,0);
INSERT INTO matches VALUES (108,8,9,18,0,0,0);

INSERT INTO matches VALUES (109,2,8,19,0,0,0);
INSERT INTO matches VALUES (110,9,7,19,0,0,0);
INSERT INTO matches VALUES (111,10,3,19,0,0,0);
INSERT INTO matches VALUES (112,11,1,19,0,0,0);
INSERT INTO matches VALUES (113,12,4,19,0,0,0);
INSERT INTO matches VALUES (114,6,5,19,0,0,0);

INSERT INTO matches VALUES (115,2,6,20,0,0,0);
INSERT INTO matches VALUES (116,5,12,20,0,0,0);
INSERT INTO matches VALUES (117,4,11,20,0,0,0);
INSERT INTO matches VALUES (118,1,10,20,0,0,0);
INSERT INTO matches VALUES (119,3,9,20,0,0,0);
INSERT INTO matches VALUES (120,7,8,20,0,0,0);

INSERT INTO matches VALUES (121,7,2,21,0,0,0);
INSERT INTO matches VALUES (122,8,3,21,0,0,0);
INSERT INTO matches VALUES (123,9,1,21,0,0,0);
INSERT INTO matches VALUES (124,10,4,21,0,0,0);
INSERT INTO matches VALUES (125,11,5,21,0,0,0);
INSERT INTO matches VALUES (126,12,6,21,0,0,0);

INSERT INTO matches VALUES (127,2,12,22,0,0,0);
INSERT INTO matches VALUES (128,6,11,22,0,0,0);
INSERT INTO matches VALUES (129,5,10,22,0,0,0);
INSERT INTO matches VALUES (130,4,9,22,0,0,0);
INSERT INTO matches VALUES (131,1,8,22,0,0,0);
INSERT INTO matches VALUES (132,3,7,22,0,0,0);

"""