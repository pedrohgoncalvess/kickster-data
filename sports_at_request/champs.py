from typing import NoReturn
from handlers.managers import Managers
from sports_at_request.address_request import Request

req = Request()
manager = Managers()


def insert_json_champ(champ_request_raw: list[dict]) -> NoReturn:
    campsInserted: list[int] = []
    for camp in champ_request_raw:
        idChamp = camp.get('league').get('id')
        if idChamp not in campsInserted:
            manager.champ_management(camp)
            campsInserted.append(idChamp)


if __name__ == '__main__':
    campTypes: list[str] = ['league', 'cup']

    responseList = []
    for campType in campTypes:
        responseList.append(req.champs("Brazil", campType))

    for jsonChamp in responseList:
        insert_json_champ(jsonChamp)
