from entities.coach import Coach


class CoachesRepository:
    def __init__(self):
        self.coaches = [
            Coach(1, "Carlos"),
            Coach(2, "Marcelo"),
            Coach(3, "Ramón")
        ]

    def get_all(self):
        return self.coaches

    def get_by_id(self, id_coach: int):
        for coach in self.coaches:
            if coach.id_person == id_coach:
                return coach

        raise ValueError("Coach not found")

    def create(self, coach: Coach):
        self.coaches.append(coach)
        return coach

    def update_full(self,id_coach: int,updated_coach: Coach):
        coach = self.get_by_id(id_coach)
        coach.name = updated_coach.name
        return coach

    def update_partial(self,id_coach: int,name=None):
        coach = self.get_by_id(id_coach)
        if name is not None:
            coach.name = name
        return coach

    def delete(self, id_coach: int):
        coach = self.get_by_id(id_coach)
        self.coaches.remove(coach)