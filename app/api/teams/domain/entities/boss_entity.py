from typing import List, Optional
from app.api.agents.entity import Agente

class Boss:
    weaknesses = List[str]
    resistances = Optional(List[str])
    archetype = Optional(List[Agente])