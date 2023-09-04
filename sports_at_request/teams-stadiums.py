from typing import NoReturn
import requests
from env_var import getHeaders
from database.operations import dbOperations
from database.validators import Validators

validator = Validators


def make_team_stadium_request() -> list[dict[str:dict]]:
    country: str = "Brazil"
    headers: dict = getHeaders()
    url: str = f"https://v3.football.api-sports.io/teams?country={country}"

    req = requests.get(url, headers=headers)
    response: dict = req.json()
    teams: list[dict[str, dict]] = response.get('response')

    return teams


def insert_json_stadium(teams_request_raw: list[dict[str:dict]]) -> NoReturn:
    for team in teams_request_raw:

        stadiumInfo: dict = team.get('venue')
        stadiumInserted: list[int] = []
        stadiumId = stadiumInfo.get('id')

        if stadiumId is not None and stadiumId not in stadiumInserted:
            dbOperations.insert_stadium(stadiumInfo)
            stadiumInserted.append(stadiumId)


def insert_json_team(teams_request_raw: list[dict[str:dict]]) -> NoReturn:
    for team in teams_request_raw:

        teamInserted: list[int] = []
        teamId = team.get('team').get('id')

        if teamId is not None and teamId not in teamInserted:
            dbOperations.insert_team(team)
            teamInserted.append(teamId)


if __name__ == '__main__':
    jsonTeams = make_team_stadium_request()
    insert_json_stadium(jsonTeams)
    insert_json_team(jsonTeams)