from typing import NoReturn
from sports_at_request.address_request import Request
from handlers.managers import Managers
from handlers.validators import Validators
from env_var import getVar

validator = Validators()
req = Request()
manager = Managers()
idLeagues = getVar("LEAGUES_TO_ANALYZE")


if __name__ == '__main__':
    for idLeague in idLeagues:
        teamsAndStadiumResponseRaw = req.team_stadium(idLeague)
        manager.stadium_management(teamsAndStadiumResponseRaw)
        manager.team_management(teamsAndStadiumResponseRaw)
