from handlers.managers import Managers
from api_requests.address_request import Request
from database.operations import Operations

def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()

    listIdFixtures = dataFromDb.get_finished_fixtures_id()

    for idFixture in listIdFixtures:
        fixtureStaticResponseRaw = req.fixture_stats(idFixture)
        fixtureLineUpResponseRaw = req.fixture_lineups(idFixture)
        manager.fixture_stats_management(fixtureStaticResponseRaw, fixtureLineUpResponseRaw, idFixture)
