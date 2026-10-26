from entities.player_x_team import Player_x_Team

class PlayerXTeamsRepository:
    def __init__(self):

        self.player_x_teams_list = []

    def assign_player(self,player_id: int, team_id: int):
        relation = Player_x_Team(
            player_id=player_id,
            team_id=team_id,
            active=True
        )
        self.player_x_teams_list.append(relation)
        return relation

    def get_active_team(self,player_id: int):
        for relation in self.player_x_teams_list:
            if (relation.player_id == player_id and relation.active):
                return relation
        return None

    def deactivate_relation(self, player_id: int):
        relation = self.get_active_team(player_id)
        if relation:
            relation.active = False
            return relation
        raise ValueError("Player has no active team")

    def get_players_by_team(self,team_id: int):
        return [
            relation for relation in self.player_x_teams_list
            if (relation.team_id == team_id and relation.active)
        ]