import csv

from app.database import SessionLocal
from entities.player import Player

db = SessionLocal()

with open("seeds/players.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        exists = (
            db.query(Player)
            .filter(Player.id_player == int(row["id_player"]))
            .first()
        )

        if not exists:
            player = Player(
                id_player=int(row["id_player"]),
                name=row["name"],
                position=None
            )

            db.add(player)

    db.commit()

db.close()

print("Jugadores cargados correctamente")