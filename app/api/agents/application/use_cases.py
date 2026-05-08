from typing import List
from app.api.agents.entity import Agente
from app.api.agents.repository import AgenteRepository

class CrearAgenteUseCase:
    def __init__(self, repo: AgenteRepository):
        self.repo = repo

    async def execute(self, name: str, rol: str, element: str, rank:str, tier: int, pasive_conditions: List[str], faction: str):
        agente = Agente(id=None, name=name, rol=rol, element=element, rank=rank, tier=tier, pasive_conditions=pasive_conditions, faction=faction)
        return await self.repo.create(agente)

class ListarAgentesUseCase:
    def __init__(self, repo: AgenteRepository):
        self.repo = repo

    async def execute(self):
        return await self.repo.list_all()
    
class UpdateAgentUseCase:
    def __init__(self, repo: AgenteRepository):
        self.repo = repo

    async def execute(self, name: str, rol: str, element: str, rank:str, tier: int, pasive_conditions: List[str], faction: str):
        agent = Agente(id=None, name=name, rol=rol, element=element, rank=rank, tier=tier, pasive_conditions=pasive_conditions, faction=faction)
        return await self.repo.update(agent)
    
class GetAgentByName:
    def __init__(self, repo: AgenteRepository):
        self.repo = repo

    async def execute(self, name: str):
        return await self.repo.getByName(name)