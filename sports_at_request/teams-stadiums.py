from typing import NoReturn
from sports_at_request.address_request import Request
from handlers.managers import Managers
from handlers.validators import Validators

validator = Validators()
req = Request()
manager = Managers()

def insert_json_stadium(teams_request_raw: list[dict[str:dict]]) -> NoReturn:
    for team in teams_request_raw:

        stadiumInfo: dict = team.get('venue')
        stadiumInserted: list[int] = []
        stadiumId = stadiumInfo.get('id')

        if stadiumId is not None and stadiumId not in stadiumInserted:
            manager.stadium_management(stadiumInfo)
            stadiumInserted.append(stadiumId)


def insert_json_team(teams_request_raw: list[dict[str:dict]]) -> NoReturn:
    for team in teams_request_raw:

        teamInserted: list[int] = []
        teamId = team.get('team').get('id')

        if teamId is not None and teamId not in teamInserted:
            manager.team_management(team)
            teamInserted.append(teamId)


if __name__ == '__main__':
    jsonTeams = req.team_stadium("Brazil")
    insert_json_stadium(jsonTeams)
    insert_json_team(jsonTeams)
