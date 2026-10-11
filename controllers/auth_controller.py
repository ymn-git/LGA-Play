from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services import user_service

router = APIRouter(tags=["Autenticación"])


class LoginRequest(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "admin",
                "password": "admin123"
            }
        }
    }


@router.post("/login", summary="Iniciar sesión de usuario")
@router.post("/api/login", summary="Iniciar sesión (alias API)", include_in_schema=False)
def login(credentials: LoginRequest):
    """
    Endpoint para autenticación de usuarios.
    Valida las credenciales contra la clase de entidad `Users`.
    Devuelve los datos del usuario si es correcto o HTTP 401 si falla.
    """
    try:
        user_data = user_service.authenticate_user(
            username=credentials.username,
            password=credentials.password
        )
        return {
            "message": "Inicio de sesión exitoso",
            "user": user_data
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )


@router.get("/users", summary="Listar usuarios registrados")
def get_users():
    """Retorna la lista de usuarios precargados en el sistema."""
    return user_service.get_all_users()
