import math
from typing import List

from app.api.agents.entity import Agente
from app.api.agents.repository import AgenteRepository
from app.api.teams.services.team_builder import TeamBuilderService
from app.api.teams.schema import Boss, TeamResponse

class BuildTeamUseCase:
    def __init__(self, agentRepo: AgenteRepository, team_builder: TeamBuilderService):
        self.agentRepo = agentRepo
        self.team_builder = team_builder

    async def execute(self, data: Boss):
        agents = await self.agentRepo.list_all()
        teams = self.team_builder.build(agents, data.archetype, data.weaknesses)
        team_with_tier = []
        for team in teams:
            team_with_tier.append({
                "team": team,
                "tier": self.get_tier_team(team)
            })

        team_with_tier = sorted(team_with_tier, key=lambda x: x["tier"])

        response = { 
            "weakness": data.weaknesses,
            "resistances": data.resistances,
            "teams_data" : team_with_tier
        }

        return response


    
    def get_tier_team(self, team: List[Agente]):
        tier = sum(x.tier for x in team) / len(team)
        return math.ceil(tier)
