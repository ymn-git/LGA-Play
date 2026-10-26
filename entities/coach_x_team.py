class Coach_x_Team:
    def __init__(
        self,
        _id,
        coach_id,
        team_id,
        active=True
    ):
        self._id = _id
        self.coach_id = coach_id
        self.team_id = team_id
        self.active = active