from typing import NoReturn
import requests
from env_var import getHeaders
from database.operations import dbOperations
from database.validators import Validators

validator = Validators


def makeLeagueRequest():
    country: str = "Brazil"
    headers: dict = getHeaders()
    campTypes: list[str] = ['league', 'cup']

    for campType in campTypes:
        url: str = f"https://v3.football.api-sports.io/leagues?country={country}&type={campType}"

        req = requests.get(url, headers=headers)
        response: dict = req.json()
        camps: list[dict[str, dict]] = response.get('response')
        campsInserted:list[int] = []
        for camp in camps:
            idChamp = camp.get('league').get('id')
            if idChamp not in campsInserted:
                dbOperations.insert_champ(camp)
                campsInserted.append(idChamp)


makeLeagueRequest()
