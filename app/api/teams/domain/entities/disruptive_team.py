from app.api.teams.domain.entities.team import Team
from typing import List
from app.api.agents.entity import Agente

class DisruptiveTeam(Team):

    def get_teams(self, boss_weaknesses: List[str]):
        teams = []
        disruptive = [x for x in self.getDisruptive() if x.element.lower() in boss_weaknesses]
        for main_dps in disruptive:
            teams.extend(self.build_teams(main_dps, filter(lambda x: x.name != main_dps.name, self.agents)))
        
        return teams
    
    def validate_team(self, team: List[Agente]):
        self.validate_team_size(team)
        if team[1].rol.lower() == team[2].rol.lower(): return None

        if not self.validate_team_pasives(team): return None

        if not self.validate_must_have_buffer(team): return None

        if not self.validate_attacker_pasive(team): return None

        if not self.validate_anomaly_teammate(team): return None

        if not self.validate_disruptive_teammate(team): return None

        return team
    
    def validate_must_have_buffer(self, team: List[Agente]):
        buffer_rols = ["soporte", "defensivo", "aturdidor"]
        
        return any(agent.rol.lower() in buffer_rols for agent in team)
    