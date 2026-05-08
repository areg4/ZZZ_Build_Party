from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Agente:
    id: Optional[str]
    name: str
    rol: str
    element: str
    rank: str
    tier: int
    pasive_conditions: List[str]
    faction: str