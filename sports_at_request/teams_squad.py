from typing import NoReturn
from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()


def insert_json_team_squad(team_squad_request_raw: dict[str:any]) -> NoReturn:
    manager.team_squad_management(team_squad_request_raw)


if __name__ == '__main__':
    season = "2023"
    idTeamsList = dataFromDb.get_all_teams_id_serie_a()

    for idTeam in idTeamsList:
        teamSquadRaw = req.team_squad(id_team=idTeam)
        insert_json_team_squad(team_squad_request_raw=teamSquadRaw)
