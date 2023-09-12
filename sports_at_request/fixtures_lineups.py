from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()

if __name__ == '__main__':
    listIdsFixtures = dataFromDb.get_all_fixtures_id()
    for idFixture in listIdsFixtures:
        teamsLineUpsResponseRaw = req.fixture_lineups(id_fixture=idFixture)
        manager.fixture_lineups_management(fixture_lineups_values=teamsLineUpsResponseRaw, id_fixture=idFixture)