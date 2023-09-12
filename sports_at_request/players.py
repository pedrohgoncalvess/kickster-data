from handlers.managers import Managers
from handlers.validators import Validators
from sports_at_request.address_request import Request
from database.data_from_db import DataFromDatabase

validator = Validators()
req = Request()
manager = Managers()
dataFromDb = DataFromDatabase()


def make_team_player_request(id_team: str | int, page: str | int = 1) -> tuple[list[dict[str, dict]], str | int, int]:
    response = req.team_player(id_team=id_team, page=page)

    players: list[dict[str, dict]] = response.get('response')
    maxPage = response.get('paging').get('total')

    return players, page, maxPage


if __name__ == '__main__':
    idTeams = dataFromDb.get_all_teams_id()
    for team in idTeams:
        request, currentPage, maxPage = make_team_player_request(team)
        manager.player_management(request)

        while currentPage <= maxPage:
            currentPage += 1
            request, currentPage, _ = make_team_player_request(team, currentPage)
            manager.player_management(request)
