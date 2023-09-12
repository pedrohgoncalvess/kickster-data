from typing import NoReturn
from env_var import get_leagues_to_analyze
from handlers.managers import Managers
from sports_at_request.address_request import Request

req = Request()
manager = Managers()
idLeagues = get_leagues_to_analyze()


if __name__ == '__main__':
    responseList = []
    for idLeague in idLeagues:
        leagueResponseRaw = req.league_by_id(id_league=idLeague)
        manager.league_management(leagueResponseRaw)
