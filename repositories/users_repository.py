from typing import List, Optional
from entities.users import Users


class UsersRepository:
    def __init__(self):
        # Usuarios precargados para pruebas y administración
        self.users: List[Users] = [
            Users(
                id_user=1,
                username="admin",
                password="admin123",
                role="admin",
                name="Administrador LGA"
            ),
            Users(
                id_user=2,
                username="micaela",
                password="password123",
                role="admin",
                name="Micaela Astrada"
            ),
            Users(
                id_user=3,
                username="usuario",
                password="user123",
                role="user",
                name="Usuario Estandar"
            ),
        ]

    def get_all(self) -> List[Users]:
        return self.users

    def get_by_id(self, id_user: int) -> Users:
        for u in self.users:
            if u.id_user == id_user:
                return u
        raise ValueError(f"Usuario con id {id_user} no encontrado")

    def get_by_username(self, username: str) -> Optional[Users]:
        for u in self.users:
            if u.username.strip().lower() == username.strip().lower():
                return u
        return None

    def create(self, user: Users) -> Users:
        if self.get_by_username(user.username) is not None:
            raise ValueError(f"El nombre de usuario '{user.username}' ya existe")
        self.users.append(user)
        return user
