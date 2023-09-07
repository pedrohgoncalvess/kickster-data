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


def insert_json_players(players_request_raw: list[dict[str:dict[str:any]]]):
    playersInserted: list[int] = []
    for player in players_request_raw:
        idPlayer = player.get('player').get('id')
        if idPlayer not in playersInserted:
            manager.player_management(player)
            playersInserted.append(idPlayer)


if __name__ == '__main__':
    idTeams = dataFromDb.get_all_teams_id()
    for team in idTeams:
        request, currentPage, maxPage = make_team_player_request(team)
        insert_json_players(request)

        while currentPage <= maxPage:
            currentPage += 1
            request, currentPage, _ = make_team_player_request(team, currentPage)
            insert_json_players(request)
