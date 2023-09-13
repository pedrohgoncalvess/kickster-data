from typing import NoReturn
from handlers.managers import Managers
from api_requests.address_request import Request
from database.data_from_db import DataFromDatabase

req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()


def insert_json_team_squad(team_squad_request_raw: dict[str:any]) -> NoReturn:
    manager.team_squad_management(team_squad_request_raw)


if __name__ == '__main__':
    season = "2023"
    idTeamsList = dataFromDb.get_all_teams_id()

    for idTeam in idTeamsList:
        teamSquadRaw = req.team_squad(id_team=idTeam)
        insert_json_team_squad(team_squad_request_raw=teamSquadRaw)
