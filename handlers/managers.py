from database.connection import DatabaseConnection
from typing import NoReturn
from managers.validators import Validators
from database.queries import Queries


class Operations:
    def __init__(self):
        self.validator = Validators()
        self.queries = Queries()
        self.__operations__ = DatabaseConnection()
        self.__perform_insert_query__ = self.__operations__.__perform_insert_query__
        self.__perform_consult_query__ = self.__operations__.__perform_consult_query__

    def stadium_management(self, stadium_infos: dict[str:str]) -> NoReturn:

        stadiumInfosTreated: dict = self.validator.stadium_validator(stadium_infos)
        queryInsert = self.queries.insert_stadium(stadium_values=stadiumInfosTreated)

        self.__perform_insert_query__(queryInsert)

    def team_management(self, team_info: dict[str:any]) -> NoReturn:

        teamInfos = self.validator.team_validator(team_info)
        queryInsert = self.queries.insert_team(team_values=teamInfos)

        self.__perform_insert_query__(queryInsert)

    def champ_management(self, champ_infos: dict[str, dict]):

        champInfos = self.validator.champ_validator(champ_infos)
        queryInsert = self.queries.insert_champ(champInfos)

        self.__perform_insert_query__(queryInsert)

    def player_management(self, player_values: dict):

        playerInfos = self.validator.player_validator(player_values)
        queryInsert = self.queries.insert_player(playerInfos)

        self.__perform_insert_query__(queryInsert)

    def fixture_management(self, fixtures_values: dict):
        fixturesInfos = self.validator.fixture_validator(fixtures_values)
        queryInsert = self.queries.insert_fixture(fixturesInfos)

        self.__perform_insert_query__(queryInsert)

    def get_all_teams_id(self) -> list[int]:

        queryTeams = self.queries.get_all_team_id

        resultQuery = self.__perform_consult_query__(queryTeams)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList

    def get_all_champs_id(self) -> list[int]:

        queryChamps = self.queries.get_all_champ_id

        resultQuery = self.__perform_consult_query__(queryChamps)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList


dbOperations = Operations()
