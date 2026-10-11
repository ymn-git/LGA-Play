from entities.person import Person


class Users(Person):
    def __init__(self, id_user: int, username: str, password: str, role: str = "admin", name: str = ""):
        super().__init__(id_person=id_user, name=name or username, role=role)
        self.id_user = id_user
        self.username = username
        self.password = password

    @property
    def id(self) -> int:
        return self.id_user

    @property
    def is_admin(self) -> bool:
        return str(self.role).strip().lower() == "admin"

    def check_password(self, password: str) -> bool:
        return self.password == password

    def to_dict(self, include_password: bool = False) -> dict:
        data = {
            "id_user": self.id_user,
            "username": self.username,
            "name": self.name,
            "role": self.role,
            "is_admin": self.is_admin,
        }
        if include_password:
            data["password"] = self.password
        return data

    def __repr__(self) -> str:
        return f"<Users id={self.id_user} username='{self.username}' role='{self.role}'>"


User = Users
