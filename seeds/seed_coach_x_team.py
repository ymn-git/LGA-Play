from app.database import SessionLocal

from entities.team import Team
from entities.coach import Coach
from entities.coach_x_team import CoachXTeam

db = SessionLocal()

relations = [
# ESTA COMENTADO PORQUE LO CARGUE DESDE SWAGGER
    # AMIGOS_UNIDOS
    #CoachXTeam(
     #   coach_id=29303884,
      #  team_id=3,
       # active=True
    #),

    # DEFENSORES
    CoachXTeam(
        coach_id=22487733,
        team_id=1,
        active=True
    ),

    # LOS_SANTOS
    CoachXTeam(
        coach_id=20555600,
        team_id=6,
        active=True
    ),

    # ONCE_UNIDOS
    CoachXTeam(
        coach_id=29909556,
        team_id=8,
        active=True
    ),

    # SUD_AMERICA
    CoachXTeam(
        coach_id=27461240,
        team_id=11,
        active=True
    ),

    # POLVORIN
    CoachXTeam(
        coach_id=27826947,
        team_id=5,
        active=True
    ),

    # ATLETICO_MIRAMAR
    CoachXTeam(
        coach_id=27804032,
        team_id=12,
        active=True
    ),

    # HURACANES
    CoachXTeam(
        coach_id=29728013,
        team_id=9,
        active=True
    ),

    # JUVENTUD_UNIDA
    CoachXTeam(
        coach_id=24384068,
        team_id=2,
        active=True
    ),

    # SAN_MARTIN
    CoachXTeam(
        coach_id=17568723,
        team_id=7,
        active=True
    ),

    # DEFENSORES_DEL_SUR
    CoachXTeam(
        coach_id=10921983,
        team_id=10,
        active=True
    ),

    # QUILMES
    CoachXTeam(
        coach_id=26763358,
        team_id=4,
        active=True
    ),
]

for relation in relations:

    exists = (
        db.query(CoachXTeam)
        .filter(
            CoachXTeam.coach_id == relation.coach_id,
            CoachXTeam.team_id == relation.team_id,
            CoachXTeam.active == True
        )
        .first()
    )

    if not exists:
        db.add(relation)

db.commit()
db.close()

print("CoachXTeam cargado correctamente")
