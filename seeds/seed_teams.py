from app.database import SessionLocal
from entities.team import Team

db = SessionLocal()

team_names = [
# NO PUSE DEFENSORES PORQUE LO CARGUE MANUALMENTE DESDE SWAGGER ASI NO SE DUPLICA EL REGISTRO
    "JUVENTUD UNIDA",
    "AMIGOS UNIDOS",
    "QUILMES",
    "POLVORIN",
    "LOS SANTOS",
    "SAN MARTIN",
    "ONCE UNIDOS",
    "HURACANES",
    "DEFENSORES DEL SUR",
    "SUD AMERICA",
    "ATLETICO MIRAMAR",
]

for name in team_names:
    exists = db.query(Team).filter(Team.name == name).first()

    if not exists:
        db.add(Team(name=name))

db.commit()
db.close()

print("Equipos cargados correctamente.")