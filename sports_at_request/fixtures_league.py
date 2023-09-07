from typing import NoReturn
from sports_at_request.address_request import Request
from handlers.managers import Managers

req = Request()
manager = Managers()


def insert_json_fixtures(fixtures_request_raw: list[dict[str:dict]]) -> NoReturn:
    fixtureInserted: list[int] = []
    for fixture in fixtures_request_raw:
        idFixture = fixture.get("fixture").get("id")
        if idFixture not in fixtureInserted:
            manager.fixture_management(fixture)
            fixtureInserted.append(idFixture)


if __name__ == '__main__':
    season = "2023"
    idChamps = [71,73]
    for idChamp in idChamps:
        fixturesRequestRaw = req.champ_fixture(id_champ=idChamp,season=season)
        insert_json_fixtures(fixturesRequestRaw)

