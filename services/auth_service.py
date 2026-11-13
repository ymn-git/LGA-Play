from fastapi import HTTPException, status
from models.user import User
from repositories.users_repository import UserRepository
from schemas.user_schema import UserCreate
from services.password_service import hash_password
from services.password_service import verify_password
from security.jwt_service import create_access_token

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, data: UserCreate) -> User:
        if self.user_repository.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un usuario con ese email"
            )

        if self.user_repository.get_by_username(data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un usuario con ese username"
            )

        user = User(
            email=data.email,
            username=data.username,
            hashed_password=hash_password(data.password)
        )

        return self.user_repository.create(user)

    def login(self, email: str, password: str) -> dict:
        user = self.user_repository.get_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        token = create_access_token(data={"sub": str(user.id)})

        return {
            "access_token": token,
            "token_type": "bearer"
        }