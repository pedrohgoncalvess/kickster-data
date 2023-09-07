from database.queries import Queries
from database.connection import DatabaseConnection


class DataFromDatabase:
    def __init__(self):
        self.queries = Queries()
        self.__connection__ = DatabaseConnection()
        self.execute_consult = self.__connection__.__perform_insert_query__

    def get_all_teams_id(self) -> list[int]:

        queryTeams = self.queries.get_all_team_id

        resultQuery = self.execute_consult(queryTeams)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList

    def get_all_champs_id(self) -> list[int]:

        queryChamps = self.queries.get_all_champ_id

        resultQuery = self.execute_consult(queryChamps)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList

    def get_all_teams_id_serie_a(self) -> list[int]:
        queryTeamsSerieA = self.queries.get_all_teams_id_serie_a
        resultQuery = self.execute_consult(queryTeamsSerieA)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList

    def get_all_fixtures_id(self) -> list[int]:

        queryFixturesId = self.queries.get_all_fixtures_id

        resultQuery = self.execute_consult(queryFixturesId)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList
