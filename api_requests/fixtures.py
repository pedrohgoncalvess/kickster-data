from api_requests.address_request import Request
from handlers.managers import Managers
from database.operations import Operations

def main():
    req = Request()
    manager = Managers()
    dataFromDb = Operations()
    idLeagues = dataFromDb.get_all_leagues_id()

    for idLeague in idLeagues:
        fixturesRequestResponseRaw = req.league_fixtures(id_champ=idLeague)
        manager.fixture_management(fixturesRequestResponseRaw)

