class Team:
    def __init__(self,id_team:int, name:str, points=0, wins=0, losses=0, draws=0, goalDifference=0, qualified=False):
        self.id_team = id_team
        self.name = name
        self._points = points
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self._goalDifference = goalDifference
        self.qualified = qualified

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def goal_difference(self):
        return self._goalDifference

    @goal_difference.setter
    def goal_difference(self, value):
        self._goalDifference = value
