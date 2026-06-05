import services.match_service
from entities.match import *
class MatchController:
    def __init__(self):
        self.service = services.match_service.MatchService()

    def match_result(self, match:Match):
        winner = match.result
        points = match.goal_difference
        if winner is not None:
            self.service.update_points_to_winner(3, winner)
        else:
            self.service.update_points_to_both(1, match.teamA, match.teamB)
