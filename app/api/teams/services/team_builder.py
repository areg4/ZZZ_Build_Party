from app.api.agents.entity import Agente
from typing import List
from app.api.teams.domain.entities.attack_team import AttackTeam
from app.api.teams.domain.entities.anomaly_team import AnomalyTeam
from app.api.teams.domain.entities.disruptive_team import DisruptiveTeam

class TeamBuilderService:
    @staticmethod
    def build(agents: List[Agente], archetype: str, boss_weaknesses: List[str]):
        match archetype:
            case "atacante":
                return AttackTeam(agents).get_teams(boss_weaknesses)
            case "anomalia":
                return AnomalyTeam(agents).get_teams(boss_weaknesses)
            case "disruptivo":
                return DisruptiveTeam(agents).get_teams(boss_weaknesses)
            case "aturdidor":
                attackTeams = AttackTeam(agents).get_teams(boss_weaknesses)
                anomalyTeams = AnomalyTeam(agents).get_teams(boss_weaknesses)
                disruptiveTeams = DisruptiveTeam(agents).get_teams(boss_weaknesses)
                stunerTeams = [*attackTeams, *anomalyTeams, *disruptiveTeams]
                return list(filter(lambda t : any(a.rol.lower() == "aturdidor" for a in t), stunerTeams))
            case _:
                raise ValueError("Arquetipo de equipo no válido")