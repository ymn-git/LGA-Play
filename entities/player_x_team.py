class Player_x_Team:

    def __init__(
        self,
        player_id: int,
        team_id: int,
        active: bool = True,
        _id: int = None
    ):
        self._id = _id
        self.player_id = player_id
        self.team_id = team_id
        self.active = active