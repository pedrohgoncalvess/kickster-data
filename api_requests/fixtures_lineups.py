from handlers.managers import Managers
from api_requests.address_request import Request
from database.operations import Operations


def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()

    listIdsFixtures = dataFromDb.get_not_collectd_fixtures_lineups()
    for idFixture in listIdsFixtures:
        teamsLineUpsResponseRaw = req.fixture_lineups(id_fixture=idFixture)
        manager.fixture_lineups_management(fixture_lineups_values=teamsLineUpsResponseRaw, id_fixture=idFixture)