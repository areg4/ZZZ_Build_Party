from abc import ABC, abstractmethod
from typing import List
from app.api.agents.entity import Agente
from itertools import combinations

class Team(ABC):
    MAX_MEMBERS = 3

    def __init__(self, agents: List[Agente]):
        self.agents = agents

    def validate_team_size(self, team: List[Agente]):
        if len(team) > self.MAX_MEMBERS:
            raise ValueError(f"El team es mayor a: {self.MAX_MEMBERS}")
        
    @abstractmethod
    def get_teams(self, boss_weaknesses: List[str]) -> List[Agente]:
        pass

    @abstractmethod
    def validate_team(self, team: List[Agente]):
        pass

    def build_teams(self, main_dps, agents: List[Agente]):
        teams = []
        pares = combinations(agents, 2)
        team_combinations = [(main_dps, a, b) for a, b in pares]

        for team in team_combinations:
            if self.validate_team(team):
                teams.append(team)
        return teams

    def validate_teammate(self, agent: Agente, teammate: Agente) -> bool:
        conditions = agent.pasive_conditions
        for condition in conditions:
            match condition:
                case "elemento":
                    if teammate.element == agent.element: return True
                case "atributo":
                    if teammate.element == agent.element: return True
                case "faccion":
                    if teammate.faction == agent.faction: return True
                case "aturdidor":
                    if teammate.rol.lower() == "aturdidor": return True
                case "soporte":
                    if teammate.rol.lower() == "soporte": return True
                case "atacante":
                    if teammate.rol.lower() == "atacante": return True
                case "anomalo":
                    if teammate.rol.lower() == "anomalia": return True
                case "disruptor":
                    if teammate.rol.lower() == "disruptor": return True
                case "defensivo":
                    if teammate.rol.lower() == "defensivo": return True
        
        return False
    
    def getAttackers(self):
        return filter(lambda x: x.rol.lower() == "atacante", self.agents)
    
    def getAnomaly(self):
        return filter(lambda x: x.rol.lower() == "anomalia", self.agents)
    
    def getStunners(self):
        return filter(lambda x: x.rol.lower() == "aturdidor", self.agents)
    
    def getSupports(self):
        return filter(lambda x: x.rol.lower() == "soporte", self.agents)
    
    def getDisruptive(self):
        return filter(lambda x: x.rol.lower() == "disruptor", self.agents)
    
    def getDefensive(self):
        return filter(lambda x: x.rol.lower() == "defensivo", self.agents)
    
    def validate_team_pasives(self, team: List[Agente]):
        pairs = [
            (team[0], team[1]),
            (team[0], team[2]),
            (team[1], team[0]),
            (team[1], team[2]),
            (team[2], team[0]),
            (team[2], team[1])
        ]

        compatibility = sum(
            1 for a, b in pairs if self.validate_teammate(a, b)
        )

        return compatibility > 2
    
    @abstractmethod
    def validate_must_have_buffer(self, team: List[Agente]):
        pass

    def validate_attacker_pasive(self, team: List[Agente]):
        if ("atacante" not in team[0].pasive_conditions and any(agent.rol.lower() == "atacante" for agent in team[1:])):
            return False
        
        return True
    
    def validate_anomaly_teammate(self, team: List[Agente]):
        if ("anomalo" not in team[0].pasive_conditions and any(agent.rol.lower() == "anomalia" for agent in team[1:])):
            return False
        return True
    
    def validate_disruptive_teammate(self, team: List[Agente]):
        if ("ruptura" not in team[0].pasive_conditions and any(agent.rol.lower() == "disruptor" for agent in team[1:])):
            return False
        return True
    