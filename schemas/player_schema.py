from pydantic import BaseModel


class PlayerCreate(BaseModel):
    dni: int
    name: str
    position: str | None = None


class PlayerUpdate(BaseModel):
    name: str
    position: str | None = None