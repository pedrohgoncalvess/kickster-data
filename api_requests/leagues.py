from typing import NoReturn
from env_var import get_leagues_to_analyze
from handlers.managers import Managers
from api_requests.address_request import Request

def main():
    req = Request()
    manager = Managers()
    idLeagues = get_leagues_to_analyze()

    for idLeague in idLeagues:
        leagueResponseRaw = req.league_by_id(id_league=idLeague)
        manager.league_management(leagueResponseRaw)
