from typing import List, Optional
from pydantic import BaseModel, Field, field_validator

class AgenteCreate(BaseModel):
    name: str = Field(..., min_length=3)
    rol: str = Field(..., min_length=3)
    element: str
    rank: str
    tier: int
    pasive_conditions: List[str]
    faction: str

    @field_validator("pasive_conditions", mode="before")
    def lowercase_list(cls, v):
        return [item.lower() for item in v]
    
class AgentUpdate(BaseModel):
    name: Optional[str] = None
    rol: Optional[str] = None
    element: Optional[str] = None
    rank: Optional[str] = None
    tier: Optional[int] = None
    pasive_conditions: Optional[List[str]] = None
    faction: Optional[str] = None

    @field_validator("pasive_conditions", mode="before")
    def lowercase_list(cls, v):
        return [item.lower() for item in v]

class AgenteResponse(BaseModel):
    id: str
    name: str
    rol: str
    element: str
    rank: str
    tier: int
    pasive_conditions: List[str]
    faction: str