from api_requests.address_request import Request
from handlers.managers import Managers
from database.data_from_db import DataFromDatabase

def main():
    req = Request()
    manager = Managers()
    dataFromDb = DataFromDatabase()
    idLeagues = dataFromDb.get_all_leagues_id()

    for idLeague in idLeagues:
        fixturesRequestResponseRaw = req.league_fixtures(id_champ=idLeague)
        manager.fixture_management(fixturesRequestResponseRaw)

