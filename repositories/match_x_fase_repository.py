from typing import List, Optional
from sqlalchemy.orm import Session
from models.match import Match
from models.match_x_fase import MatchXFase
from models.fase import Fase

class MatchXFaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create_fase(self, tipo: str, season: int = 2026) -> Fase:
        fase = self.db.query(Fase).filter(Fase.tipo == tipo, Fase.season == season).first()
        if not fase:
            name = "Fase Regular" if tipo == "REGULAR" else "Playoffs"
            fase = Fase(name=name, tipo=tipo, season=season)
            self.db.add(fase)
            self.db.commit()
            self.db.refresh(fase)
        return fase

    def create_regular_match(
        self,
        teamA_id: int,
        teamB_id: int,
        matchday: int,
        season: int = 2026,
        match_date=None
    ) -> Match:
        """
        Crea un partido de Fase Regular y lo asocia en la tabla intermedia match_x_fase.
        """
        fase = self.get_or_create_fase("REGULAR", season)

        match = Match(
            teamA_id=teamA_id,
            teamB_id=teamB_id,
            season=season,
            match_date=match_date,
            goalsA=0,
            goalsB=0,
            jugado=False
        )
        self.db.add(match)
        self.db.flush()

        # Guardar en la tabla intermedia
        intermedia = MatchXFase(
            match_id=match.id,
            fase_id=fase.id,
            tipo_fase="REGULAR",
            matchday=matchday,
            round_name=None,
            bracket_order=None,
            penaltiesA=None,
            penaltiesB=None,
            winner_id=None
        )
        self.db.add(intermedia)
        self.db.commit()
        self.db.refresh(match)
        return match

    def create_playoff_match(
        self,
        teamA_id: int,
        teamB_id: int,
        round_name: str,
        bracket_order: int,
        season: int = 2026,
        match_date=None
    ) -> Match:
        """
        Crea un partido de Playoffs y lo asocia en la tabla intermedia match_x_fase.
        """
        fase = self.get_or_create_fase("PLAYOFF", season)

        match = Match(
            teamA_id=teamA_id,
            teamB_id=teamB_id,
            season=season,
            match_date=match_date,
            goalsA=0,
            goalsB=0,
            jugado=False
        )
        self.db.add(match)
        self.db.flush()

        # Guardar en la tabla intermedia con sus datos particulares
        intermedia = MatchXFase(
            match_id=match.id,
            fase_id=fase.id,
            tipo_fase="PLAYOFF",
            matchday=None,
            round_name=round_name,
            bracket_order=bracket_order,
            penaltiesA=None,
            penaltiesB=None,
            winner_id=None
        )
        self.db.add(intermedia)
        self.db.commit()
        self.db.refresh(match)
        return match

    def get_regular_matches_by_matchday(self, matchday: int, season: int = 2026) -> List[Match]:
        """
        Consulta todos los partidos regulares de una fecha específica.
        """
        return (
            self.db.query(Match)
            .join(MatchXFase, Match.id == MatchXFase.match_id)
            .filter(
                Match.season == season,
                MatchXFase.tipo_fase == "REGULAR",
                MatchXFase.matchday == matchday
            )
            .all()
        )

    def get_all_regular_matches(self, season: int = 2026) -> List[Match]:
        """
        Consulta todos los partidos de la fase regular para una temporada.
        """
        return (
            self.db.query(Match)
            .join(MatchXFase, Match.id == MatchXFase.match_id)
            .filter(
                Match.season == season,
                MatchXFase.tipo_fase == "REGULAR"
            )
            .order_by(MatchXFase.matchday.asc())
            .all()
        )

    def get_playoff_matches_by_season(self, season: int = 2026) -> List[Match]:
        """
        Consulta todos los partidos de playoffs de una temporada, ordenados por ronda y llave.
        """
        return (
            self.db.query(Match)
            .join(MatchXFase, Match.id == MatchXFase.match_id)
            .filter(
                Match.season == season,
                MatchXFase.tipo_fase == "PLAYOFF"
            )
            .order_by(MatchXFase.bracket_order.asc())
            .all()
        )

    def update_playoff_result(
        self,
        match_id: int,
        goalsA: int,
        goalsB: int,
        winner_id: int,
        penaltiesA: Optional[int] = None,
        penaltiesB: Optional[int] = None,
        scorers: Optional[list] = None,
        yellow_cards: Optional[list] = None,
        red_cards: Optional[list] = None
    ) -> Match:
        """
        Actualiza el resultado de un partido de playoffs incluyendo penales y el equipo clasificado.
        """
        match = self.db.query(Match).filter(Match.id == match_id).first()
        if not match:
            raise ValueError(f"Match con id {match_id} no encontrado")

        intermedia = self.db.query(MatchXFase).filter(MatchXFase.match_id == match_id).first()
        if not intermedia or intermedia.tipo_fase != "PLAYOFF":
            raise ValueError(f"El partido {match_id} no corresponde a la fase de playoffs")

        # Actualizar datos generales del partido
        match.goalsA = goalsA
        match.goalsB = goalsB
        match.jugado = True
        if scorers is not None:
            match.scorers = scorers
        if yellow_cards is not None:
            match.yellow_cards = yellow_cards
        if red_cards is not None:
            match.red_cards = red_cards

        # Actualizar datos particulares en la tabla intermedia
        intermedia.penaltiesA = penaltiesA
        intermedia.penaltiesB = penaltiesB
        intermedia.winner_id = winner_id

        self.db.commit()
        self.db.refresh(match)
        return match
