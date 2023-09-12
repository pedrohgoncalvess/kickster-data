from sports_at_request.address_request import Request
from handlers.managers import Managers
from database.data_from_db import DataFromDatabase

req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()
idLeagues = dataFromDb.get_all_league_id()


if __name__ == '__main__':
    for idLeague in idLeagues:
        fixturesRequestResponseRaw = req.league_fixtures(id_champ=idLeague)
        manager.fixture_management(fixturesRequestResponseRaw)

