from database.queries import Queries
from database.connection import DatabaseConnection


class DataFromDatabase:
    def __init__(self):
        self.queries = Queries()
        self.__connection__ = DatabaseConnection()
        self.execute_consult = self.__connection__.__perform_consult_query__

    def get_all_players_id_serie_a(self) -> list[int]:

        queryPlayer = self.queries.get_all_id_players_serie_a

        resultQuery = self.execute_consult(queryPlayer)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList

    def get_all_teams_id(self) -> list[int]:

        queryTeams = self.queries.get_all_team_id

        resultQuery = self.execute_consult(queryTeams)
        idsList: list[int] = []

        for queryTuple in resultQuery:
            idsList.append(queryTuple[0])

        return idsList

    def get_all_players_id(self) -> list:
        queryPlayers = self.queries.get_all_id_players

        resultQuery = self.execute_consult(queryPlayers)
        idsList = []

        if resultQuery is not None:
            for queryTuple in resultQuery:
                idsList.append(queryTuple[0])

        return idsList

    def get_all_players_squad_id(self):
        queryPlayerSquad = self.queries.get_all_id_players_squad

        resultQuery = self.execute_consult(queryPlayerSquad)

        idsList = []

        if resultQuery is not None:
            for queryTuple in resultQuery:
                idsList.append(queryTuple[0])

        return idsList

    def get_all_league_id(self) -> list[int]:

        queryLeagues = self.queries.get_all_league_id

        resultQuery = self.execute_consult(queryLeagues)
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

    def get_all_league_teams_id(self) -> dict[int:int]:
        queryTeamsLeague = self.queries.get_leagues_teams_relation_id
        resultQuery = self.execute_consult(queryTeamsLeague)
        idsRelationDict: dict[dict[str:int]] = {}

        for resultTuple in resultQuery:
            keyValue = resultTuple[0]
            idLeague = resultTuple[1]
            idTeam = resultTuple[2]
            idsRelationDict.update({keyValue: {"id_league": idLeague, "id_team": idTeam}})

        return idsRelationDict
