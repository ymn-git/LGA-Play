from entities.person import Person

class Coach(Person):
    def __init__(self, id_person, name):
        super().__init__(id_person, name, role="coach")
