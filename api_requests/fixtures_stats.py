from handlers.managers import Managers
from api_requests.address_request import Request
from database.data_from_db import DataFromDatabase

def main():
    req = Request()
    manager = Managers()
    dataFromDb = DataFromDatabase()

    listIdFixtures = dataFromDb.get_all_fixtures_id()

    for idFixture in listIdFixtures:
        fixtureStaticResponseRaw = req.fixture_stats(idFixture)
        fixtureLineUpResponseRaw = req.fixture_lineups(idFixture)
        manager.fixture_stats_management(fixtureStaticResponseRaw, fixtureLineUpResponseRaw, idFixture)
