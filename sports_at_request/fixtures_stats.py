from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()


def insert_json_fixture_stats(fixture_stats_raw: list[dict[str:any]], fixture_id: int):
    for team_stats in fixture_stats_raw:
        manager.fixture_stats_management(team_stats, fixture_id)


if __name__ == '__main__':
    listIdFixtures = dataFromDb.get_all_fixtures_id()

    for idFixture in listIdFixtures:
        jsonFixtureStaticRaw = req.fixture_stats(idFixture)
        insert_json_fixture_stats(jsonFixtureStaticRaw, idFixture)
