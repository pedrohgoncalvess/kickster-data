from typing import NoReturn
import requests
from env_var import getHeaders
from database.operations import dbOperations


def make_league_request(country: str, camp_type: str) -> list[dict]:
    headers: dict = getHeaders()

    url: str = f"https://v3.football.api-sports.io/leagues?country={country}&type={camp_type}"

    req = requests.get(url, headers=headers)
    response: list[dict] = req.json()
    return response


def insert_json_champ(champ_request_raw: list[dict]) -> NoReturn:
    campsInserted: list[int] = []
    for camp in champ_request_raw:
        idChamp = camp.get('league').get('id')
        if idChamp not in campsInserted:
            dbOperations.insert_champ(camp)
            campsInserted.append(idChamp)


if __name__ == '__main__':
    campTypes: list[str] = ['league', 'cup']

    responseList = []
    for campType in campTypes:
        responseList.append(make_league_request("Brazil", campType))

    for jsonChamp in responseList:
        insert_json_champ(jsonChamp)
