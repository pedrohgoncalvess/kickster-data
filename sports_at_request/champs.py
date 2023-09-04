from typing import NoReturn
from database.operations import dbOperations
from sports_at_request.api_request import Request

req = Request()


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
        responseList.append(req.champs("Brazil", campType))

    for jsonChamp in responseList:
        insert_json_champ(jsonChamp)
