from entities.match import Match
class Matchday:
    def __init__(self, number:int, matches:list["Match"]):
        self.number = number
        self.matches = matches
