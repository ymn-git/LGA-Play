from app.database import SessionLocal
from entities.team import Team

db = SessionLocal()

team_names = [
    "Defensores",
    "Juventud_Unida",
    "Amigos_Unidos",
    "Quilmes",
    "Polvorin",
    "Los_Santos",
    "San_Martin",
    "Once_Unidos",
    "Huracanes",
    "Defensores_del_Sur",
    "Sud_America",
    "Atletico_Miramar",
]

for name in team_names:
    exists = db.query(Team).filter(Team.name == name).first()

    if not exists:
        db.add(Team(name=name))

db.commit()
db.close()

print("Equipos cargados correctamente.")