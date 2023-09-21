from database.connection import db_connection
from typing import NoReturn
from handlers.parsers import Parsers
from handlers.generators import Queries
from database.data_from_db import DataFromDatabase


class Managers:
    def __init__(self):
        self.parser = Parsers()
        self.queries = Queries()
        self.data_from_db = DataFromDatabase()
        self.__insert__ = db_connection.insert_object
        self.execute_insert_query = "pass"
        self.execute_update_query = "pass"

    def stadium_management(self, stadium_infos: dict[str:str]) -> NoReturn:
        for stadium in stadium_infos:
            stadiumInfosTreated: dict = self.parser.stadium_parser(stadium)
            newStadium = self.queries.generator_stadium(stadium_values=stadiumInfosTreated)
            self.__insert__(newStadium)

    def team_management(self, team_info: dict[str:any]) -> NoReturn:
        for team in team_info:
            teamInfos = self.parser.team_parser(team)
            newTeam = self.queries.generator_team(team_values=teamInfos)
            self.__insert__(newTeam)

    def league_management(self, league_infos: dict[str, dict]):
        for league in league_infos:
            leagueInfos = self.parser.league_parser(league)
            newLeague = self.queries.generator_league(leagueInfos)
            self.__insert__(newLeague)

    def player_management(self, player_values: list[dict[str:str]]):
        playersInDb = self.data_from_db.get_all_players_id()
        for playerValue in player_values:
            if len(playersInDb) != 0:
                playerInfos = self.parser.player_parser(playerValue)
                idPlayer = playerInfos.get("id")

                if idPlayer not in playersInDb:
                    newPlayer = self.queries.generator_player(playerInfos)
                    self.__insert__(newPlayer)
            else:
                playerInfos = self.parser.player_parser(playerValue)
                newPlayer = self.queries.generator_player(playerInfos)
                self.__insert__(newPlayer)

    def fixture_management(self, fixtures_values: dict) -> NoReturn:
        stadiumsInDB = self.data_from_db.get_all_stadiums_id()
        fixturesInDb = []
        for fixtureValues in fixtures_values:
            fixturesInfos = self.parser.fixture_parser(fixtureValues)
            fixtureId = fixturesInfos.get("id_fixture")

            stadiumId = fixturesInfos.get("id_stadium")
            if stadiumId not in stadiumsInDB:
                fixturesInfos.update({"id_stadium": None})

            if fixtureId not in fixturesInDb:
                newFixture = self.queries.generator_fixture(fixturesInfos)
                self.__insert__(newFixture)

    def team_squad_management(self, players_squad_values: list[dict[str:any]]) -> NoReturn:
        playersSquadInfo = self.parser.team_squad_parser(players_squad_values[0])
        idPlayersSquadInDb = self.data_from_db.get_all_players_squad_id()

        for playerInfo in playersSquadInfo:
            idPlayer = playerInfo.get("id_player")
            if idPlayer not in idPlayersSquadInDb:
                queryInsert = self.queries.generator_team_player_squad(playerInfo)

                self.execute_insert_query(queryInsert)

    def fixture_stats_management(self, fixture_stats_values: list[dict[str:any]],
                                 fixture_lineups_values: list[dict[str:any]], fixture_id: int) -> NoReturn:
        fixturesInDb = self.data_from_db.get_all_fixtures_id()

        for team_stats in fixture_stats_values:
            fixtureStatsInfo = self.parser.fixture_stats_parser(team_stats, fixture_lineups_values, fixture_id)
            idFixture = fixtureStatsInfo.get("id_fixture")

            if idFixture not in fixturesInDb:
                queryInsert = self.queries.generator_fixture_stats(fixtureStatsInfo)
                self.execute_insert_query(queryInsert)

    def fixture_event_management(self, fixture_events_values: list[dict[str:any]], fixture_id: int):
        for event in fixture_events_values:
            fixtureEventInfo = self.parser.fixture_events_parser(event, fixture_id)
            queryInsert = self.queries.generator_fixture_event(fixtureEventInfo)
            self.execute_insert_query(queryInsert)
        queryUpdate = self.queries.update_fixture_data_status(fixture_id)
        self.execute_update_query(queryUpdate)

    def player_stats_management(self, player_stats_values: list[dict[str:any]]) -> NoReturn:
        playerStat = self.parser.player_stats_parser(player_stats_values)
        for stat in playerStat:
            queryInsert = self.queries.generator_player_stat(stat)
            self.execute_insert_query(queryInsert)

    def team_league_fixtures_stats_management(self, team_league_stat_values: dict[str:any]) -> NoReturn:
        teamLeagueStat = self.parser.team_league_fixtures_stats_parser(team_league_stat_values)
        queryInsert = self.queries.generator_team_league_fixtures_stats(teamLeagueStat)
        self.execute_insert_query(queryInsert)

    def team_league_goals_stats_management(self, team_league_goals_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueGoalsStat = self.parser.team_league_goals_stats_parser(team_league_goals_stats_values)
        for typeGoal in teamLeagueGoalsStat:
            queryInsert = self.queries.generator_team_league_goals_stats(typeGoal)
            self.execute_insert_query(queryInsert)

    def team_league_cards_stats_management(self, team_league_cards_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueCardsStats = self.parser.team_league_cards_stats_parser(team_league_cards_stats_values)
        for typeCard in teamLeagueCardsStats:
            queryInsert = self.queries.generator_team_league_cards_stats(typeCard)
            self.execute_insert_query(queryInsert)

    def fixture_lineups_management(self, fixture_lineups_values: list[dict[str:any]],
                                   id_fixture: str | int) -> NoReturn:
        for teamLineUp in fixture_lineups_values:
            fixtureTeamLineUp = self.parser.fixture_lineup_parser(teamLineUp, id_fixture)
            for playerInLineUp in fixtureTeamLineUp:
                queryInsert = self.queries.generator_fixture_lineup(playerInLineUp)
                self.execute_insert_query(queryInsert)
