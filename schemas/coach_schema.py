from pydantic import BaseModel

class CoachCreate(BaseModel):
    dni: int
    name: str

class CoachUpdate(BaseModel):
    name: str