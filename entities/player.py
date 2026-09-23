from entities.person import Person

class Player(Person):
    def __init__(self, id_person:int, name, position):
        super().__init__(id_person, name, role="player")
        self.position = position
