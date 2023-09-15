from handlers.managers import Managers
from api_requests.address_request import Request
from database.data_from_db import DataFromDatabase


def main():
    req = Request()
    manager = Managers()
    dataFromDb = DataFromDatabase()

    listIdsFixtures = dataFromDb.get_all_fixtures_id()
    for idFixture in listIdsFixtures:
        teamsLineUpsResponseRaw = req.fixture_lineups(id_fixture=idFixture)
        manager.fixture_lineups_management(fixture_lineups_values=teamsLineUpsResponseRaw, id_fixture=idFixture)
