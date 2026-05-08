from fastapi import APIRouter, Depends, HTTPException

from app.api.agents.exceptions import DuplicateAgentError, AgentNotFoundError
from app.api.agents.mongo_repository import AgenteMongoRepository
from app.api.agents.application.use_cases import CrearAgenteUseCase, ListarAgentesUseCase, UpdateAgentUseCase, GetAgentByName
from app.api.agents.schemas import AgenteCreate, AgenteResponse, AgentUpdate

router = APIRouter(prefix="/agentes", tags=["Agentes"])

def get_repo():
    return AgenteMongoRepository()

@router.post("/")
async def crear_agente(data: AgenteCreate, repo=Depends(get_repo)):
    try:
        usecase = CrearAgenteUseCase(repo)
        return await usecase.execute(data.name, data.rol, data.element, data.rank, data.tier, data.pasive_conditions, data.faction)
    except DuplicateAgentError:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un agente con ese nombre"
        )
    

@router.get("/")
async def listar_agentes(repo=Depends(get_repo)):
    usecase = ListarAgentesUseCase(repo)
    return await usecase.execute()

@router.get("/{name}")
async def get_by_name(name: str, repo=Depends(get_repo)):
    try:
        usecase = GetAgentByName(repo)
        result = await usecase.execute(name)
        return result
    except AgentNotFoundError:
        raise HTTPException(status_code=404, detail="Agente no encontrado")

@router.patch("/{name}")
async def update_agent(name: str, data: AgentUpdate, repo=Depends(get_repo)):
    try:
        usecase = UpdateAgentUseCase(repo)
        result = await usecase.execute(data.name or name, data.rol, data.element, data.rank, data.tier, data.pasive_conditions, data.faction)
        return result
    except AgentNotFoundError:
        raise HTTPException(status_code=404, detail="Agente no encontrado")
    