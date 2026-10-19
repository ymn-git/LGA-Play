from repositories.users_repository import UsersRepository

users_repo = UsersRepository()


def authenticate_user(username: str, password: str) -> dict:
    """
    Valida las credenciales utilizando el método check_password de la clase Users.
    Retorna el diccionario con la información del usuario si es correcto,
    o lanza un ValueError si son incorrectas.
    """
    user = users_repo.get_by_username(username)
    if not user or not user.check_password(password):
        raise ValueError("Usuario o contraseña incorrectos")

    return user.to_dict()


def get_all_users() -> list:
    return [u.to_dict() for u in users_repo.get_all()]


def get_user_by_id(id_user: int) -> dict:
    return users_repo.get_by_id(id_user).to_dict()
