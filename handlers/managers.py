from database.connection import DatabaseConnection
from typing import NoReturn
from handlers.parsers import Parsers
from database.queries import Queries
from database.data_from_db import DataFromDatabase


class Managers:
    def __init__(self):
        self.parser = Parsers()
        self.queries = Queries()
        self.data_from_db = DataFromDatabase()
        self.__operations__ = DatabaseConnection()
        self.execute_insert_query = self.__operations__.__perform_insert_query__
        self.execute_update_query = self.__operations__.__perform__update_query__

    def stadium_management(self, stadium_infos: dict[str:str]) -> NoReturn:
        for stadium in stadium_infos:
            stadiumInfosTreated: dict = self.parser.stadium_parser(stadium)
            queryInsert = self.queries.insert_stadium(stadium_values=stadiumInfosTreated)

            self.execute_insert_query(queryInsert)

    def team_management(self, team_info: dict[str:any]) -> NoReturn:
        for team in team_info:
            teamInfos = self.parser.team_parser(team)
            queryInsert = self.queries.insert_team(team_values=teamInfos)

            self.execute_insert_query(queryInsert)

    def league_management(self, league_infos: dict[str, dict]):
        for league in league_infos:
            leagueInfos = self.parser.league_parser(league)
            queryInsert = self.queries.insert_league(leagueInfos)

            self.execute_insert_query(queryInsert)

    def player_management(self, player_values: list[dict[str:str]]):
        playersInDb = self.data_from_db.get_all_players_id()
        for playerValue in player_values:
            playerInfos = self.parser.player_parser(playerValue)
            idPlayer = playerInfos.get("id")

            if idPlayer not in playersInDb:
                queryInsert = self.queries.insert_player(playerInfos)
                self.execute_insert_query(queryInsert)

    def fixture_management(self, fixtures_values: dict) -> NoReturn:
        for fixtureValues in fixtures_values:
            fixturesInfos = self.parser.fixture_parser(fixtureValues)
            queryInsert = self.queries.insert_fixture(fixturesInfos)

            self.execute_insert_query(queryInsert)

    def team_squad_management(self, players_squad_values: list[dict[str:any]]) -> NoReturn:
        playersSquadInfo = self.parser.team_squad_parser(players_squad_values[0])
        idPlayersSquadInDb = self.data_from_db.get_all_players_squad_id()

        for playerInfo in playersSquadInfo:
            idPlayer = playerInfo.get("id_player")
            if idPlayer not in idPlayersSquadInDb:
                queryInsert = self.queries.insert_team_player_squad(playerInfo)

                self.execute_insert_query(queryInsert)

    def fixture_stats_management(self, fixture_stats_values: list[dict[str:any]],
                                 fixture_lineups_values: list[dict[str:any]], fixture_id: int) -> NoReturn:
        fixturesInDb = self.data_from_db.get_all_fixtures_id()

        for team_stats in fixture_stats_values:
            fixtureStatsInfo = self.parser.fixture_stats_parser(team_stats, fixture_lineups_values, fixture_id)
            idFixture = fixtureStatsInfo.get("id_fixture")

            if idFixture not in fixturesInDb:
                queryInsert = self.queries.insert_fixture_stats(fixtureStatsInfo)
                self.execute_insert_query(queryInsert)

    def fixture_event_management(self, fixture_events_values: list[dict[str:any]], fixture_id: int):
        for event in fixture_events_values:
            fixtureEventInfo = self.parser.fixture_events_parser(event, fixture_id)
            queryInsert = self.queries.insert_fixture_event(fixtureEventInfo)
            self.execute_insert_query(queryInsert)
        queryUpdate = self.queries.update_fixture_data_status(fixture_id)
        self.execute_update_query(queryUpdate)

    def player_stats_management(self, player_stats_values: list[dict[str:any]]) -> NoReturn:
        playerStat = self.parser.player_stats_parser(player_stats_values)
        for stat in playerStat:
            queryInsert = self.queries.insert_player_stat(stat)
            self.execute_insert_query(queryInsert)

    def team_league_fixtures_stats_management(self, team_league_stat_values: dict[str:any]) -> NoReturn:
        teamLeagueStat = self.parser.team_league_fixtures_stats_parser(team_league_stat_values)
        queryInsert = self.queries.insert_team_league_fixtures_stats(teamLeagueStat)
        self.execute_insert_query(queryInsert)

    def team_league_goals_stats_management(self, team_league_goals_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueGoalsStat = self.parser.team_league_goals_stats_parser(team_league_goals_stats_values)
        for typeGoal in teamLeagueGoalsStat:
            queryInsert = self.queries.insert_team_league_goals_stats(typeGoal)
            self.execute_insert_query(queryInsert)

    def team_league_cards_stats_management(self, team_league_cards_stats_values: list[dict[str:any]]) -> NoReturn:
        teamLeagueCardsStats = self.parser.team_league_cards_stats_parser(team_league_cards_stats_values)
        for typeCard in teamLeagueCardsStats:
            queryInsert = self.queries.insert_team_league_cards_stats(typeCard)
            self.execute_insert_query(queryInsert)

    def fixture_lineups_management(self, fixture_lineups_values: list[dict[str:any]],
                                   id_fixture: str | int) -> NoReturn:
        for teamLineUp in fixture_lineups_values:
            fixtureTeamLineUp = self.parser.fixture_lineup_parser(teamLineUp, id_fixture)
            for playerInLineUp in fixtureTeamLineUp:
                queryInsert = self.queries.insert_fixture_lineup(playerInLineUp)
                self.execute_insert_query(queryInsert)
