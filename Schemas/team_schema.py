from pydantic import BaseModel

class TeamCreate(BaseModel):
    name: str

class TeamUpdate(BaseModel):
    name: str