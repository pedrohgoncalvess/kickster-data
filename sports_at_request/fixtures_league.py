from sports_at_request.address_request import Request
from handlers.managers import Managers
from env_var import getVar

req = Request()
manager = Managers()
idLeagues = getVar("LEAGUES_TO_ANALYZE")


if __name__ == '__main__':
    for idLeague in idLeagues:
        fixturesRequestResponseRaw = req.league_fixtures(id_champ=idLeague)
        manager.fixture_management(fixturesRequestResponseRaw)

