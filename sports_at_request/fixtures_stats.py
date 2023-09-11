from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()


if __name__ == '__main__':
    listIdFixtures = dataFromDb.get_all_fixtures_id()

    for idFixture in listIdFixtures:
        fixtureStaticResponseRaw = req.fixture_stats(idFixture)
        fixtureLineUpResponseRaw = req.fixture_lineups(idFixture)
        manager.fixture_stats_management(fixtureStaticResponseRaw, fixtureLineUpResponseRaw, idFixture)
