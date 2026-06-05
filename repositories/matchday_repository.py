from entities.match import Match
from entities.matchday import Matchday
from repositories.team_repository import TeamsRepository
from helpers.helpers import get_team_by_name

teams = TeamsRepository()
# FECHA 1
matchday1 = Matchday(
    1,
    [
        Match(teams.Defensores, teams.San_Martin),
        Match(teams.Quilmes, teams.Once_Unidos),
        Match(teams.Polvorin, teams.Huracanes),
        Match(teams.Los_Santos, teams.Defensores_DS),
        Match(teams.Atletico, teams.Sudamerica),
        Match(teams.Amigos_Unidos, teams.Juventud_Unida),
    ]
)

# FECHA 2
matchday2 = Matchday(
    2,
    [
        Match(teams.Juventud_Unida, teams.Sudamerica),
        Match(teams.Defensores_DS, teams.Atletico),
        Match(teams.Huracanes, teams.Los_Santos),
        Match(teams.Once_Unidos, teams.Polvorin),
        Match(teams.San_Martin, teams.Quilmes),
        Match(teams.Amigos_Unidos, teams.Defensores),
    ]
)

# FECHA 3
matchday3 = Matchday(
    3,
    [
        Match(teams.Defensores, teams.Juventud_Unida),
        Match(teams.Quilmes, teams.Amigos_Unidos),
        Match(teams.Polvorin, teams.San_Martin),
        Match(teams.Los_Santos, teams.Once_Unidos),
        Match(teams.Atletico, teams.Huracanes),
        Match(teams.Sudamerica, teams.Defensores_DS),
    ]
)

# FECHA 4
matchday4 = Matchday(
    4,
    [
        Match(teams.Juventud_Unida, teams.Defensores_DS),
        Match(teams.Huracanes, teams.Sudamerica),
        Match(teams.Once_Unidos, teams.Atletico),
        Match(teams.San_Martin, teams.Los_Santos),
        Match(teams.Amigos_Unidos, teams.Polvorin),
        Match(teams.Quilmes, teams.Defensores),
    ]
)

# FECHA 5
matchday5 = Matchday(
    5,
    [
        Match(teams.Quilmes, teams.Juventud_Unida),
        Match(teams.Defensores, teams.Polvorin),
        Match(teams.Los_Santos, teams.Amigos_Unidos),
        Match(teams.Sudamerica, teams.Once_Unidos),
        Match(teams.Defensores_DS, teams.Huracanes),
        Match(teams.Atletico, teams.San_Martin),
    ]
)

# FECHA 6
matchday6 = Matchday(
    6,
    [
        Match(teams.Juventud_Unida, teams.Huracanes),
        Match(teams.Once_Unidos, teams.Defensores_DS),
        Match(teams.San_Martin, teams.Sudamerica),
        Match(teams.Amigos_Unidos, teams.Atletico),
        Match(teams.Los_Santos, teams.Defensores),
        Match(teams.Quilmes, teams.Polvorin),
    ]
)

# FECHA 7
matchday7 = Matchday(
    7,
    [
        Match(teams.Polvorin, teams.Juventud_Unida),
        Match(teams.Los_Santos, teams.Quilmes),
        Match(teams.Defensores, teams.Atletico),
        Match(teams.Sudamerica, teams.Amigos_Unidos),
        Match(teams.Defensores_DS, teams.San_Martin),
        Match(teams.Huracanes, teams.Once_Unidos),
    ]
)

# FECHA 8
matchday8 = Matchday(
    8,
    [
        Match(teams.Once_Unidos, teams.Juventud_Unida),
        Match(teams.San_Martin, teams.Huracanes),
        Match(teams.Amigos_Unidos, teams.Defensores_DS),
        Match(teams.Defensores, teams.Sudamerica),
        Match(teams.Quilmes, teams.Atletico),
        Match(teams.Polvorin, teams.Los_Santos),
    ]
)

# FECHA 9
matchday9 = Matchday(
    9,
    [
        Match(teams.Los_Santos, teams.Juventud_Unida),
        Match(teams.Atletico, teams.Polvorin),
        Match(teams.Sudamerica, teams.Quilmes),
        Match(teams.Defensores_DS, teams.Defensores),
        Match(teams.Huracanes, teams.Amigos_Unidos),
        Match(teams.Once_Unidos, teams.San_Martin),
    ]
)

# FECHA 10
matchday10 = Matchday(
    10,
    [
        Match(teams.Juventud_Unida, teams.San_Martin),
        Match(teams.Amigos_Unidos, teams.Once_Unidos),
        Match(teams.Defensores, teams.Huracanes),
        Match(teams.Quilmes, teams.Defensores_DS),
        Match(teams.Polvorin, teams.Sudamerica),
        Match(teams.Los_Santos, teams.Atletico),
    ]
)

# FECHA 11
matchday11 = Matchday(
    11,
    [
        Match(teams.Atletico, teams.Juventud_Unida),
        Match(teams.Sudamerica, teams.Los_Santos),
        Match(teams.Defensores_DS, teams.Polvorin),
        Match(teams.Huracanes, teams.Quilmes),
        Match(teams.Once_Unidos, teams.Defensores),
        Match(teams.San_Martin, teams.Amigos_Unidos),
    ]
)

# FECHA 12 (inverso de FECHA 1)
matchday12 = Matchday(
    12,
    [
        Match(teams.San_Martin, teams.Defensores),
        Match(teams.Once_Unidos, teams.Quilmes),
        Match(teams.Huracanes, teams.Polvorin),
        Match(teams.Defensores_DS, teams.Los_Santos),
        Match(teams.Sudamerica, teams.Atletico),
        Match(teams.Juventud_Unida, teams.Amigos_Unidos),
    ]
)

# FECHA 13 (inverso de FECHA 2)
matchday13 = Matchday(
    13,
    [
        Match(teams.Sudamerica, teams.Juventud_Unida),
        Match(teams.Atletico, teams.Defensores_DS),
        Match(teams.Los_Santos, teams.Huracanes),
        Match(teams.Polvorin, teams.Once_Unidos),
        Match(teams.Quilmes, teams.San_Martin),
        Match(teams.Defensores, teams.Amigos_Unidos),
    ]
)

# FECHA 14 (inverso de FECHA 3)
matchday14 = Matchday(
    14,
    [
        Match(teams.Juventud_Unida, teams.Defensores),
        Match(teams.Amigos_Unidos, teams.Quilmes),
        Match(teams.San_Martin, teams.Polvorin),
        Match(teams.Once_Unidos, teams.Los_Santos),
        Match(teams.Huracanes, teams.Atletico),
        Match(teams.Defensores_DS, teams.Sudamerica),
    ]
)

# FECHA 15 (inverso de FECHA 4)
matchday15 = Matchday(
    15,
    [
        Match(teams.Defensores_DS, teams.Juventud_Unida),
        Match(teams.Sudamerica, teams.Huracanes),
        Match(teams.Atletico, teams.Once_Unidos),
        Match(teams.Los_Santos, teams.San_Martin),
        Match(teams.Polvorin, teams.Amigos_Unidos),
        Match(teams.Defensores, teams.Quilmes),
    ]
)

# FECHA 16 (inverso de FECHA 5)
matchday16 = Matchday(
    16,
    [
        Match(teams.Juventud_Unida, teams.Quilmes),
        Match(teams.Polvorin, teams.Defensores),
        Match(teams.Amigos_Unidos, teams.Los_Santos),
        Match(teams.Once_Unidos, teams.Sudamerica),
        Match(teams.Huracanes, teams.Defensores_DS),
        Match(teams.San_Martin, teams.Atletico),
    ]
)

# FECHA 17 (inverso de FECHA 6)
matchday17 = Matchday(
    17,
    [
        Match(teams.Huracanes, teams.Juventud_Unida),
        Match(teams.Defensores_DS, teams.Once_Unidos),
        Match(teams.Sudamerica, teams.San_Martin),
        Match(teams.Atletico, teams.Amigos_Unidos),
        Match(teams.Defensores, teams.Los_Santos),
        Match(teams.Polvorin, teams.Quilmes),
    ]
)

# FECHA 18 (inverso de FECHA 7)
matchday18 = Matchday(
    18,
    [
        Match(teams.Juventud_Unida, teams.Polvorin),
        Match(teams.Quilmes, teams.Los_Santos),
        Match(teams.Atletico, teams.Defensores),
        Match(teams.Amigos_Unidos, teams.Sudamerica),
        Match(teams.San_Martin, teams.Defensores_DS),
        Match(teams.Once_Unidos, teams.Huracanes),
    ]
)

# FECHA 19 (inverso de FECHA 8)
matchday19 = Matchday(
    19,
    [
        Match(teams.Juventud_Unida, teams.Once_Unidos),
        Match(teams.Huracanes, teams.San_Martin),
        Match(teams.Defensores_DS, teams.Amigos_Unidos),
        Match(teams.Sudamerica, teams.Defensores),
        Match(teams.Atletico, teams.Quilmes),
        Match(teams.Los_Santos, teams.Polvorin),
    ]
)

# FECHA 20 (inverso de FECHA 9)
matchday20 = Matchday(
    20,
    [
        Match(teams.Juventud_Unida, teams.Los_Santos),
        Match(teams.Polvorin, teams.Atletico),
        Match(teams.Quilmes, teams.Sudamerica),
        Match(teams.Defensores, teams.Defensores_DS),
        Match(teams.Amigos_Unidos, teams.Huracanes),
        Match(teams.San_Martin, teams.Once_Unidos),
    ]
)

# FECHA 21 (inverso de FECHA 10)
matchday21 = Matchday(
    21,
    [
        Match(teams.San_Martin, teams.Juventud_Unida),
        Match(teams.Once_Unidos, teams.Amigos_Unidos),
        Match(teams.Huracanes, teams.Defensores),
        Match(teams.Defensores_DS, teams.Quilmes),
        Match(teams.Sudamerica, teams.Polvorin),
        Match(teams.Atletico, teams.Los_Santos),
    ]
)

# FECHA 22 (inverso de FECHA 11)
matchday22 = Matchday(
    22,
    [
        Match(teams.Juventud_Unida, teams.Atletico),
        Match(teams.Los_Santos, teams.Sudamerica),
        Match(teams.Polvorin, teams.Defensores_DS),
        Match(teams.Quilmes, teams.Huracanes),
        Match(teams.Defensores, teams.Once_Unidos),
        Match(teams.Amigos_Unidos, teams.San_Martin),
    ]
)
fixture = [
    matchday1,
    matchday2,
    matchday3,
    matchday4,
    matchday5,
    matchday6,
    matchday7,
    matchday8,
    matchday9,
    matchday10,
    matchday11,
    matchday12,
    matchday13,
    matchday14,
    matchday15,
    matchday16,
    matchday17,
    matchday18,
    matchday19,
    matchday20,
    matchday21,
    matchday22,
]
