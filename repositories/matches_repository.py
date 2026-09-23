from entities.match import Match
from services.team_service import teams_repo

class MatchesRepository:
    def __init__(self):
        self.matches = [
            # FECHA 1
            Match(1, 1, 7, 1, 2026),
            Match(2, 4, 8, 1, 2026),
            Match(3, 5, 9, 1, 2026),
            Match(4, 6, 10, 1, 2026),
            Match(5, 12, 11, 1, 2026),
            Match(6, 3, 2, 1, 2026),

            # FECHA 2
            Match(7, 2, 11, 2, 2026),
            Match(8, 10, 12, 2, 2026),
            Match(9, 9, 6, 2, 2026),
            Match(10, 8, 5, 2, 2026),
            Match(11, 7, 4, 2, 2026),
            Match(12, 3, 1, 2, 2026),

            # FECHA 3
            Match(13, 1, 2, 3, 2026),
            Match(14, 4, 3, 3, 2026),
            Match(15, 5, 7, 3, 2026),
            Match(16, 6, 8, 3, 2026),
            Match(17, 12, 9, 3, 2026),
            Match(18, 11, 10, 3, 2026),

            # FECHA 4
            Match(19, 2, 10, 4, 2026),
            Match(20, 9, 11, 4, 2026),
            Match(21, 8, 12, 4, 2026),
            Match(22, 7, 6, 4, 2026),
            Match(23, 3, 5, 4, 2026),
            Match(24, 4, 1, 4, 2026),

            # FECHA 5
            Match(25, 4, 2, 5, 2026),
            Match(26, 1, 5, 5, 2026),
            Match(27, 6, 3, 5, 2026),
            Match(28, 11, 8, 5, 2026),
            Match(29, 10, 9, 5, 2026),
            Match(30, 12, 7, 5, 2026),

            # FECHA 6
            Match(31, 2, 9, 6, 2026),
            Match(32, 8, 10, 6, 2026),
            Match(33, 7, 11, 6, 2026),
            Match(34, 3, 12, 6, 2026),
            Match(35, 6, 1, 6, 2026),
            Match(36, 4, 5, 6, 2026),

            # FECHA 7
            Match(37, 5, 2, 7, 2026),
            Match(38, 6, 4, 7, 2026),
            Match(39, 1, 12, 7, 2026),
            Match(40, 11, 3, 7, 2026),
            Match(41, 10, 7, 7, 2026),
            Match(42, 9, 8, 7, 2026),

            # FECHA 8
            Match(43, 8, 2, 8, 2026),
            Match(44, 7, 9, 8, 2026),
            Match(45, 3, 10, 8, 2026),
            Match(46, 1, 11, 8, 2026),
            Match(47, 4, 12, 8, 2026),
            Match(48, 5, 6, 8, 2026),

            # FECHA 9
            Match(49, 6, 2, 9, 2026),
            Match(50, 12, 5, 9, 2026),
            Match(51, 11, 4, 9, 2026),
            Match(52, 10, 1, 9, 2026),
            Match(53, 9, 3, 9, 2026),
            Match(54, 8, 7, 9, 2026),

            # FECHA 10
            Match(55, 2, 7, 10, 2026),
            Match(56, 3, 8, 10, 2026),
            Match(57, 1, 9, 10, 2026),
            Match(58, 4, 10, 10, 2026),
            Match(59, 5, 11, 10, 2026),
            Match(60, 6, 12, 10, 2026),

            # FECHA 11
            Match(61, 12, 2, 11, 2026),
            Match(62, 11, 6, 11, 2026),
            Match(63, 10, 5, 11, 2026),
            Match(64, 9, 4, 11, 2026),
            Match(65, 8, 1, 11, 2026),
            Match(66, 7, 3, 11, 2026),

            # FECHA 12 (inverso FECHA 1)
            Match(67, 7, 1, 12, 2026),
            Match(68, 8, 4, 12, 2026),
            Match(69, 9, 5, 12, 2026),
            Match(70, 10, 6, 12, 2026),
            Match(71, 11, 12, 12, 2026),
            Match(72, 2, 3, 12, 2026),

            # FECHA 13 (inverso FECHA 2)
            Match(73, 11, 2, 13, 2026),
            Match(74, 12, 10, 13, 2026),
            Match(75, 6, 9, 13, 2026),
            Match(76, 5, 8, 13, 2026),
            Match(77, 4, 7, 13, 2026),
            Match(78, 1, 3, 13, 2026),

            # FECHA 14 (inverso FECHA 3)
            Match(79, 2, 1, 14, 2026),
            Match(80, 3, 4, 14, 2026),
            Match(81, 7, 5, 14, 2026),
            Match(82, 8, 6, 14, 2026),
            Match(83, 9, 12, 14, 2026),
            Match(84, 10, 11, 14, 2026),

            # FECHA 15 (inverso FECHA 4)
            Match(85, 10, 2, 15, 2026),
            Match(86, 11, 9, 15, 2026),
            Match(87, 12, 8, 15, 2026),
            Match(88, 6, 7, 15, 2026),
            Match(89, 5, 3, 15, 2026),
            Match(90, 1, 4, 15, 2026),

            # FECHA 16 (inverso FECHA 5)
            Match(91, 2, 4, 16, 2026),
            Match(92, 5, 1, 16, 2026),
            Match(93, 3, 6, 16, 2026),
            Match(94, 8, 11, 16, 2026),
            Match(95, 9, 10, 16, 2026),
            Match(96, 7, 12, 16, 2026),

            # FECHA 17 (inverso FECHA 6)
            Match(97, 9, 2, 17, 2026),
            Match(98, 10, 8, 17, 2026),
            Match(99, 11, 7, 17, 2026),
            Match(100, 12, 3, 17, 2026),
            Match(101, 1, 6, 17, 2026),
            Match(102, 5, 4, 17, 2026),

            # FECHA 18 (inverso FECHA 7)
            Match(103, 2, 5, 18, 2026),
            Match(104, 4, 6, 18, 2026),
            Match(105, 12, 1, 18, 2026),
            Match(106, 3, 11, 18, 2026),
            Match(107, 7, 10, 18, 2026),
            Match(108, 8, 9, 18, 2026),

            # FECHA 19 (inverso FECHA 8)
            Match(109, 2, 8, 19, 2026),
            Match(110, 9, 7, 19, 2026),
            Match(111, 10, 3, 19, 2026),
            Match(112, 11, 1, 19, 2026),
            Match(113, 12, 4, 19, 2026),
            Match(114, 6, 5, 19, 2026),

            # FECHA 20 (inverso FECHA 9)
            Match(115, 2, 6, 20, 2026),
            Match(116, 5, 12, 20, 2026),
            Match(117, 4, 11, 20, 2026),
            Match(118, 1, 10, 20, 2026),
            Match(119, 3, 9, 20, 2026),
            Match(120, 7, 8, 20, 2026),

            # FECHA 21 (inverso FECHA 10)
            Match(121, 7, 2, 21, 2026),
            Match(122, 8, 3, 21, 2026),
            Match(123, 9, 1, 21, 2026),
            Match(124, 10, 4, 21, 2026),
            Match(125, 11, 5, 21, 2026),
            Match(126, 12, 6, 21, 2026),

            # FECHA 22 (inverso FECHA 11)
            Match(127, 2, 12, 22, 2026),
            Match(128, 6, 11, 22, 2026),
            Match(129, 5, 10, 22, 2026),
            Match(130, 4, 9, 22, 2026),
            Match(131, 1, 8, 22, 2026),
            Match(132, 3, 7, 22, 2026),
        ]

    def get_match_by_id(self, match_id):
        for match in self.matches:
            if match.id_match == match_id:
                return match

    def get_matches_by_matchday(self, matchday: int):
        matches = [match for match in self.matches if match.matchday == matchday]

        if not matches:
            raise ValueError(f"No matches found for matchday {matchday}")

        return matches

    def update_match_goals(self,match_id, goalsA, goalsB):
        for match in self.matches:
            if match.id_match == match_id:
                match.goalsA = goalsA
                match.goalsB = goalsB
                return match

    def update_match(self, match: Match):
        # Como el objeto ya está en la lista, no hace falta reemplazar nada
        return match

    def mark_match_as_played(self, match_id):
        for match in self.matches:
            if match.id_match == match_id:
                match.jugado = True
                return match
        raise ValueError("Match not found")

    def add_scorer(self, match_id, player_id):
        for match in self.matches:
            if match.id_match == match_id:
                match.scorers_list.append(player_id)
                return match
        raise ValueError("Match not found")


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