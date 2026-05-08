from dataclasses import asdict

from pymongo.errors import DuplicateKeyError

from app.api.agents.entity import Agente
from app.api.agents.exceptions import DuplicateAgentError, AgentNotFoundError
from app.api.agents.repository import AgenteRepository
from app.database import mongo

class AgenteMongoRepository(AgenteRepository):

    async def create(self, agente: Agente) -> Agente:
        mongo.db.agentes.create_index("name", unique=True)
        data = {"name": agente.name, "rol": agente.rol, "element": agente.element, "rank": agente.rank, "tier": agente.tier, "pasive_conditions": agente.pasive_conditions, "faction": agente.faction}
        try:
            result = await mongo.db.agentes.insert_one(data)
        except DuplicateKeyError:
            raise DuplicateAgentError()
        agente.id = str(result.inserted_id)
        return agente

    async def list_all(self):
        docs = mongo.db.agentes.find()
        result = []
        async for doc in docs:
            result.append(
                Agente(
                    id=str(doc["_id"]),
                    name=doc["name"],
                    rol=doc["rol"],
                    element=doc["element"],
                    rank=doc["rank"],
                    tier=doc["tier"],
                    pasive_conditions=doc["pasive_conditions"],
                    faction=doc["faction"]
                )
            )
        return result
    
    async def update(self, agent: Agente) -> Agente:
        update_data = {k: v for k, v in asdict(agent).items() if v is not None}
        result = await mongo.db.agentes.find_one_and_update(
            {"name": update_data["name"]},
            {"$set": update_data},
            return_document=True
        )

        if not result:
            raise AgentNotFoundError()
        
        result["_id"] = str(result["_id"])
        return result
    
    async def getByName(self, name) -> Agente:
        result = await mongo.db.agentes.find_one({"name": name})
        if not result:
            raise AgentNotFoundError()
        
        result["_id"] = str(result["_id"])
        return result
    
    async def getByElement(self, element):
        docs = mongo.db.agentes.find({"element": element})
        result = []
        async for doc in docs:
            result.append(
                Agente(
                    id=str(doc["_id"]),
                    name=doc["name"],
                    rol=doc["rol"],
                    element=doc["element"],
                    rank=doc["rank"],
                    tier=doc["tier"],
                    pasive_conditions=doc["pasive_conditions"],
                    faction=doc["faction"]
                )
            )
        return result
