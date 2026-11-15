from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from repositories.users_repository import UserRepository
from schemas.user_schema import UserCreate, UserResponse
from services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(data: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = AuthService(repository)
    return service.register(data)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    repository = UserRepository(db)
    service = AuthService(repository)

    return service.login(
        email=form_data.username,
        password=form_data.password
    )
