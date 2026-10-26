from repositories.users_repository import UsersRepository
from entities.users import User

users_repo = UsersRepository()


def _user_to_dict(user: User) -> dict:
    return {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
    }


def authenticate_user(username: str, password: str) -> dict:
    """
    Valida las credenciales del usuario por nombre de usuario o email.
    Retorna los datos del usuario si es correcto y está activo,
    o lanza un ValueError si las credenciales son incorrectas o la cuenta está inactiva.
    """
    user = users_repo.get_by_username(username) or users_repo.get_by_email(username)
    if not user or user.password != password:
        raise ValueError("Usuario o contraseña incorrectos")

    if not user.is_active:
        raise ValueError("El usuario está inactivo")

    return _user_to_dict(user)


def get_all_users() -> list:
    return [_user_to_dict(u) for u in users_repo.get_all()]


def get_user_by_id(id: int) -> dict:
    user = users_repo.get_by_id(id)
    return _user_to_dict(user)


def create_user(
    id: int,
    email: str,
    username: str,
    password: str,
    is_active: bool = True,
    is_admin: bool = False,
) -> dict:
    new_user = User(
        id=id,
        email=email,
        username=username,
        password=password,
        is_active=is_active,
        is_admin=is_admin,
    )
    created = users_repo.create(new_user)
    return _user_to_dict(created)
