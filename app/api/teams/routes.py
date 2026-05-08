from fastapi import APIRouter, Depends, HTTPException
from app.api.teams.schema import Boss
from app.api.agents.mongo_repository import AgenteMongoRepository
from app.api.teams.application.use_cases import BuildTeamUseCase
from app.api.teams.services.team_builder import TeamBuilderService


router = APIRouter(prefix="/team", tags=["Team"])

def get_agent_repo():
    return AgenteMongoRepository()

def get_build_team_usecase():
    return BuildTeamUseCase(agentRepo=get_agent_repo(), team_builder=TeamBuilderService())

@router.post("/")
async def build_team(data: Boss, usecase: BuildTeamUseCase = Depends(get_build_team_usecase)):
    try:
        return await usecase.execute(data)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="ERROR"
        )