"""
Script para inicializar la base de datos (SQLite) con los 12 equipos de la LGA,
las fases 'Fase Regular' y 'Playoffs', y los partidos iniciales vinculados
a través de la tabla intermedia match_x_fase.
"""
from app.database import Base, engine, SessionLocal
from models.team import Team
from models.fase import Fase
from models.match import Match
from models.match_x_fase import MatchXFase
from repositories.match_x_fase_repository import MatchXFaseRepository

def seed():
    # 1. Crear las tablas si no existen
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 2. Cargar los 12 Equipos
        equipos_base = [
            (1, "Defensores"),
            (2, "Juventud Unida"),
            (3, "Amigos Unidos"),
            (4, "Quilmes"),
            (5, "Polvorin"),
            (6, "Los Santos"),
            (7, "San Martin"),
            (8, "Once Unidos"),
            (9, "Huracanes"),
            (10, "Defensores DS"),
            (11, "Sudamerica"),
            (12, "Atletico")
        ]

        for team_id, name in equipos_base:
            existing = db.query(Team).filter(Team.id == team_id).first()
            if not existing:
                team = Team(id=team_id, name=name)
                db.add(team)
        db.commit()

        # 3. Inicializar repositorio intermedio
        repo = MatchXFaseRepository(db)

        # 4. Asegurar fases
        fase_reg = repo.get_or_create_fase("REGULAR", 2026)
        fase_play = repo.get_or_create_fase("PLAYOFF", 2026)

        # 5. Cargar partidos de ejemplo para Fecha 1 (Fase Regular)
        partidos_f1 = [
            (1, 7, 1),
            (4, 8, 1),
            (5, 9, 1),
            (6, 10, 1),
            (12, 11, 1),
            (3, 2, 1)
        ]

        # Verificar si ya hay partidos cargados
        hay_partidos = db.query(Match).first()
        if not hay_partidos:
            for teamA, teamB, matchday in partidos_f1:
                repo.create_regular_match(
                    teamA_id=teamA,
                    teamB_id=teamB,
                    matchday=matchday,
                    season=2026
                )

            # 6. Cargar llaves iniciales de Playoffs (Primera Ronda - 8 clasificados)
            llaves_playoff = [
                (1, 8, "PRIMERA_RONDA", 1),
                (4, 5, "PRIMERA_RONDA", 2),
                (2, 7, "PRIMERA_RONDA", 3),
                (3, 6, "PRIMERA_RONDA", 4)
            ]
            for teamA, teamB, round_name, bracket_order in llaves_playoff:
                repo.create_playoff_match(
                    teamA_id=teamA,
                    teamB_id=teamB,
                    round_name=round_name,
                    bracket_order=bracket_order,
                    season=2026
                )

            print("Base de datos inicializada exitosamente con Fase Regular y Playoffs!")
        else:
            print("La base de datos ya contiene partidos.")

    finally:
        db.close()

if __name__ == "__main__":
    seed()
