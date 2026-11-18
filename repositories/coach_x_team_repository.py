from sqlalchemy.orm import Session

from entities.coach_x_team import CoachXTeam

class CoachXTeamsRepository:

    def __init__(self, db: Session):
        self.db = db

    def assign_coach(self, coach_id: int, team_id: int):
        active_relation = self.get_active_team(coach_id)
        if active_relation:
            raise ValueError("Coach already has an active team")

        relation = CoachXTeam(
            coach_id=coach_id,
            team_id=team_id,
            active=True
        )
        self.db.add(relation)
        self.db.commit()
        self.db.refresh(relation)
        return relation

    def get_active_team(self, coach_id: int):

        return (
            self.db.query(CoachXTeam)
            .filter(
                CoachXTeam.coach_id == coach_id,
                CoachXTeam.active.is_(True)
            )
            .first()
        )

    def deactivate_relation(self, coach_id: int):

        relation = self.get_active_team(coach_id)

        if relation is None:
            raise ValueError("Coach has no active team")

        relation.active = False

        self.db.commit()
        self.db.refresh(relation)

        return relation

    def get_coaches_by_team(self, team_id: int):

        return (
            self.db.query(CoachXTeam)
            .filter(
                CoachXTeam.team_id == team_id,
                CoachXTeam.active.is_(True)
            )
            .all()
        )