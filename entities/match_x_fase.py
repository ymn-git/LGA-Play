from typing import Optional

class MatchXFase:
    def __init__(
        self,
        id_match_x_fase: Optional[int],
        match_id: int,
        fase_id: int,
        tipo_fase: str,
        matchday: Optional[int] = None,
        round_name: Optional[str] = None,
        bracket_order: Optional[int] = None,
        penaltiesA: Optional[int] = None,
        penaltiesB: Optional[int] = None,
        winner_id: Optional[int] = None
    ):
        self.id = id_match_x_fase
        self.match_id = match_id
        self.fase_id = fase_id
        self.tipo_fase = tipo_fase  # 'REGULAR' o 'PLAYOFF'
        self.matchday = matchday
        self.round_name = round_name
        self.bracket_order = bracket_order
        self.penaltiesA = penaltiesA
        self.penaltiesB = penaltiesB
        self.winner_id = winner_id
