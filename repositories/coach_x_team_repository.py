from entities.coach_x_team import Coach_x_Team


class CoachXTeamsRepository:
    def __init__(self):

        self.coach_x_teams_list = []

    def assign_coach(
        self,
        coach_id: int,
        team_id: int
    ):
        relation = Coach_x_Team(
            coach_id=coach_id,
            team_id=team_id,
            active=True
        )

        self.coach_x_teams_list.append(relation)

        return relation

    def get_active_team(
        self,
        coach_id: int
    ):
        for relation in self.coach_x_teams_list:

            if (
                relation.coach_id == coach_id
                and relation.active
            ):
                return relation

        return None

    def deactivate_relation(
        self,
        coach_id: int
    ):
        relation = self.get_active_team(coach_id)

        if relation:
            relation.active = False
            return relation

        raise ValueError(
            "Coach has no active team"
        )

    def get_coaches_by_team(
        self,
        team_id: int
    ):
        return [
            relation
            for relation in self.coach_x_teams_list
            if (
                relation.team_id == team_id
                and relation.active
            )
        ]