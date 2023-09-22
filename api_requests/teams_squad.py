from typing import NoReturn
from handlers.managers import Managers
from api_requests.address_request import Request
from database.operations import Operations


def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()

    idTeamsList = dataFromDb.get_all_teams_id()

    for idTeam in idTeamsList:
        teamSquadRaw = req.team_squad(id_team=idTeam)
        manager.team_squad_management(teamSquadRaw)
