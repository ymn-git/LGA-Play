from typing import List, Optional
from entities.users import User, Users


class UsersRepository:
    def __init__(self):
        # Usuarios precargados para pruebas y administración
        self.users: List[User] = [
            User(
                id=1,
                email="admin@lga.com",
                username="admin",
                password="admin123",
                is_active=True,
                is_admin=True,
            ),
            User(
                id=2,
                email="micaela@lga.com",
                username="micaela",
                password="password123",
                is_active=True,
                is_admin=True,
            ),
            User(
                id=3,
                email="usuario@lga.com",
                username="usuario",
                password="user123",
                is_active=True,
                is_admin=False,
            ),
        ]

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, id: int) -> User:
        for u in self.users:
            if u.id == id or u.user_id == id:
                return u
        raise ValueError(f"Usuario con id {id} no encontrado")

    def get_by_username(self, username: str) -> Optional[User]:
        for u in self.users:
            if u.username.strip().lower() == username.strip().lower():
                return u
        return None

    def get_by_email(self, email: str) -> Optional[User]:
        for u in self.users:
            if u.email.strip().lower() == email.strip().lower():
                return u
        return None

    def create(self, user: User) -> User:
        if self.get_by_username(user.username) is not None:
            raise ValueError(f"El nombre de usuario '{user.username}' ya existe")
        if self.get_by_email(user.email) is not None:
            raise ValueError(f"El email '{user.email}' ya está registrado")
        self.users.append(user)
        return user
