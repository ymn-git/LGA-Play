from sqlalchemy.orm import Session

from entities.coach import Coach


class CoachesRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):

        return (
            self.db.query(Coach)
            .order_by(Coach.id_coach)
            .all()
        )

    def get_by_id(self, id_coach: int):

        coach = (
            self.db.query(Coach)
            .filter(Coach.id_coach == id_coach)
            .first()
        )

        if coach is None:
            raise ValueError("Coach not found")

        return coach

    def create(self, coach: Coach):

        self.db.add(coach)
        self.db.commit()
        self.db.refresh(coach)

        return coach

    def update_full(self, id_coach: int, updated_coach: Coach):

        coach = self.get_by_id(id_coach)

        coach.name = updated_coach.name

        self.db.commit()
        self.db.refresh(coach)

        return coach

    def update_partial(self, id_coach: int, name=None):

        coach = self.get_by_id(id_coach)

        if name is not None:
            coach.name = name

        self.db.commit()
        self.db.refresh(coach)

        return coach

    def delete(self, id_coach: int):

        coach = self.get_by_id(id_coach)

        self.db.delete(coach)
        self.db.commit()

        return coach
