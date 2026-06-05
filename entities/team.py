class Team:
    def __init__(self, name:str, points=0, wins=0, losses=0, draws=0, goalDifference=0, qualified=False):
        self.name = name
        self.points = points
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.goalDifference = goalDifference
        self.qualified = qualified
