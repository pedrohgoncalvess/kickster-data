from database.connection import DatabaseConnection
from typing import NoReturn, Tuple, Any
from database.validators import Validators
from database.queries import Queries


class Operations:
    def __init__(self):
        self.validator = Validators()
        self.queries = Queries()
        self.__connection = DatabaseConnection().connection
        self.__cursor = self.__connection.cursor()

    def stadium_management(self, stadium_infos: dict[str:str]) -> NoReturn:

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        stadiumInfosTreated: dict = self.validator.stadium_validator(stadium_infos)

        queryInsert = self.queries.insert_stadium(stadium_values=stadiumInfosTreated)

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except:
            connection.rollback()

        finally:
            connection.close()

    def team_management(self, team_info: dict[str:any]) -> NoReturn:

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        teamInfos = self.validator.team_validator(team_info)

        queryInsert = self.queries.insert_team(team_values=teamInfos)

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except:
            connection.rollback()

        finally:
            connection.close()

    def champ_management(self, champ_infos: dict[str, dict]):

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        champInfos = self.validator.champ_validator(champ_infos)

        queryInsert = self.queries.insert_champ(champInfos)

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except:
            connection.rollback()

        finally:
            connection.close()

    def player_management(self, player_values: dict):

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        playerInfos = self.validator.player_validator(player_values)
        queryInsert = self.queries.insert_player(playerInfos)

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except:
            connection.rollback()

        finally:
            connection.close()


    def __perform_consult_query__(self, statement: str) -> Any:
        try:
            self.__cursor.execute(statement)
            resultQuery = self.__cursor.fetchall()
        except:
            self.__connection.rollback()
            resultQuery = None
        finally:
            return resultQuery

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
