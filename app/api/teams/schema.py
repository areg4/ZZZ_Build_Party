from pydantic import BaseModel, field_validator
from typing import List, Optional
from app.api.agents.schemas import AgenteResponse

class TeamResponse(BaseModel):
    weaknesses: List[str]
    resistances: Optional[List[str]] = []
    team: List[AgenteResponse]
    tier: float

class Boss(BaseModel):
    weaknesses: List[str]
    resistances: Optional[List[str]] = []
    archetype: Optional[str] = None

    @field_validator("weaknesses", mode="before")
    def lowercase_list(cls, v):
        return [item.lower() for item in v]