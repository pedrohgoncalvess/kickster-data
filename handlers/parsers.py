from datetime import datetime as dt
import pytz
import datetime
from unidecode import unidecode


class Parsers:
    def __init__(self):
        self.actualYear = int(dt.now().year)

    def stadium_parser(self, stadium_infos: dict[str:str]) -> dict[str:str]:
        stadiumRoot = stadium_infos.get("venue")
        idExStadium = stadiumRoot.get('id')
        nameStadium = stadiumRoot.get("name")
        addressStadium = stadiumRoot.get('address')
        capacityStadium = stadiumRoot.get('capacity')
        surfaceStadium = stadiumRoot.get('surface')
        imageStadium = stadiumRoot.get('image')

        try:
            stateStadiumRaw = stadiumRoot.get('city').split(',')[1].strip().replace(" ", "_").lower()
            cityStatiumRaw = stadiumRoot.get('city').split(',')[0].strip().replace(" ", "_").lower()
            stateStadium = unidecode(stateStadiumRaw)
            cityStatium = unidecode(cityStatiumRaw)
        except:
            stateStadium = None
            cityStatium = None

        dictToReturn: dict[str:str] = {
            "id": idExStadium,
            "name": nameStadium,
            "address": addressStadium,
            "capacity": capacityStadium,
            "surface": surfaceStadium,
            "image": imageStadium,
            "state": stateStadium,
            "city": cityStatium
        }

        return dictToReturn

    def team_parser(self, team_info: dict[str:any]) -> dict[str:str]:

        idExTeam = team_info.get('team').get('id')
        idStadium = team_info.get('venue').get('id')
        nameTeam = team_info.get('team').get('name')
        logoTeam = team_info.get('team').get('logo')
        nationalTeam = team_info.get('team').get('national')
        codeTeam = team_info.get('team').get('code')
        countryTeam = team_info.get('team').get('country')
        foundedTeam = team_info.get('team').get('founded')

        dictToReturn = {
            "id": idExTeam,
            "name": nameTeam,
            "id_stadium": idStadium,
            "logo": logoTeam,
            "national": nationalTeam,
            "code": "000" if codeTeam is None else codeTeam,
            "country": countryTeam,
            "founded": 0000 if foundedTeam is None else foundedTeam
        }

        return dictToReturn

    def league_parser(self, league_infos: dict[str:dict[str:str]]) -> dict[str:str]:

        idLeague = league_infos.get('league').get('id')
        nameLeague = league_infos.get('league').get('name')
        typeLeague = league_infos.get('league').get('type')
        logoLeague = league_infos.get('league').get('logo')
        countryLeague = league_infos.get('country').get('name')

        seasonsInformation: list[dict[str:str]] = league_infos.get('seasons')
        for seasonInfo in seasonsInformation:
            if seasonInfo.get('year') == self.actualYear:
                startLeague = seasonInfo.get('start')
                endLeague = seasonInfo.get('end')
            else:
                startLeague = f'{self.actualYear}-01-01'
                endLeague = f'{self.actualYear}-01-01'

        dictToReturn = {
            "id": idLeague, "name": nameLeague, "logo": logoLeague, "type": typeLeague,
            "country": countryLeague, "start": startLeague, "end": endLeague, "season": self.actualYear
        }

        return dictToReturn

    def player_parser(self, player_infos: dict[str:any]) -> dict[str:any]:

        playerRoot = player_infos.get('player')
        playerID = playerRoot.get('id')
        playerName = playerRoot.get('name')
        playerFirstName = playerRoot.get('firstname')
        playerLastName = playerRoot.get('lastname')
        playerBirth = playerRoot.get('birth').get('date')
        playerNationality = playerRoot.get('nationality')
        playerHeight = playerRoot.get('height').replace(' cm', '') if playerRoot.get('height') is not None else 0
        playerWeight = playerRoot.get('weight').replace(' kg', '') if playerRoot.get('weight') is not None else 0
        playerImage = playerRoot.get('image')
        playerInjured = playerRoot.get("injured")

        dictToReturn = {
            "id": playerID, "name": playerName, "first_name": playerFirstName, "last_name": playerLastName,
            "birth": playerBirth, "nationality": playerNationality, "height": playerHeight,
            "weight": playerWeight, "photo": playerImage, "injured": playerInjured
        }

        for keyValue in list(dictToReturn.keys()):
            value = dictToReturn.get(keyValue)
            if value == "\n    ":
                dictToReturn.update({keyValue:0})

        return dictToReturn

    def fixture_parser(self, fixture_infos: dict[str:any]) -> dict[str:str]:

        fixtureInfos: dict[str:any] = fixture_infos.get("fixture")
        leagueInfo = fixture_infos.get("league")
        teamsInfo = fixture_infos.get("teams")

        idFixture: str = fixtureInfos.get("id")
        refereeFixture: str = fixtureInfos.get("referee")

        saoPauloTimezone = pytz.timezone('America/Sao_Paulo')
        datetimeFixtureRaw = fixtureInfos.get("periods").get("first")
        datetimeFixtureProceced = saoPauloTimezone.localize(dt.fromtimestamp(datetimeFixtureRaw)) if datetimeFixtureRaw is not None else dt.utcfromtimestamp(946684800)
        datetimeFixture = str(datetimeFixtureProceced).replace("-03:00", "")

        idStadium: int = fixtureInfos.get("venue").get("id") if fixtureInfos.get("venue").get("id") != "null" else None
        homeTeam: str = teamsInfo.get("home").get("id")
        awayTeam: str = teamsInfo.get("away").get("id")
        idLeague: int = leagueInfo.get("id")
        roundLeague: str = leagueInfo.get("round")
        seasonLeague: int = leagueInfo.get("season")

        statusFixture: str = fixtureInfos.get("status").get("long").lower().replace(" ", "_")

        winnerTeamRaw: bool | str = teamsInfo.get("home").get("winner")

        if winnerTeamRaw == True:
            winnerTeam = "home_winner"
        elif winnerTeamRaw == False:
            winnerTeam = "away_winner"
        else:
            winnerTeam = "draw"

        dictToReturn = {
            "id_fixture": idFixture,
            "date": datetimeFixture,
            "referee": refereeFixture,
            "id_stadium": idStadium,
            "home_team": homeTeam,
            "away_team": awayTeam,
            "id_league": idLeague,
            "round": roundLeague,
            "season": seasonLeague,
            "result": winnerTeam,
            "status": statusFixture
        }

        return dictToReturn

    def team_squad_parser(self, team_squad_infos: dict[str:any]) -> list[dict[str:str]]:

        idTeam = team_squad_infos.get("team").get("id")

        listPlayersToReturn: list[dict[str:any]] = []
        playersInfos: list[dict[str:any]] = team_squad_infos.get("players")
        for playerInfo in playersInfos:
            idPlayer = playerInfo.get("id")
            positionPlayer = playerInfo.get("position")
            numberPlayer = playerInfo.get("number")

            dictPlayer = {
                "id_player": idPlayer,
                "id_team": idTeam,
                "position": positionPlayer,
                "number": numberPlayer if numberPlayer is not None else 0,
            }
            listPlayersToReturn.append(dictPlayer)

        return listPlayersToReturn

    def fixture_stats_parser(self, team_fixture_stats_infos: dict[str:any],
                             fixture_lineups_infos: list[dict[str:any]], fixture_id: int):

        idTeam = team_fixture_stats_infos.get("team").get("id")

        global formationLineup
        for lineup in fixture_lineups_infos:
            idTeamLineUp = lineup.get("team").get("id")
            if idTeam == idTeamLineUp:
                formationLineup = lineup.get("formation") if lineup.get("formation") is not None else "0-0-0"
                coach = lineup.get("coach").get("id") if lineup.get("coach") is not None else 0

        statisticsRoot = team_fixture_stats_infos.get("statistics")
        dictToReturn: dict[str:any] = {"id_team": idTeam, "id_fixture": fixture_id,
                                       "formation": formationLineup, "coach": coach}

        for statistic in statisticsRoot:
            typeStat = statistic.get("type").lower().replace(" ", "_")
            valueStat = statistic.get("value")
            if type(valueStat) == str:
                try:
                    valueStat = int(valueStat.replace("%", ""))
                except:
                    valueStat = float(valueStat)
            if valueStat is None:
                valueStat = 0
            dictToReturn.update({typeStat: valueStat})

        return dictToReturn

    def fixture_events_parser(self, fixture_event_infos: dict[str:any], fixture_id: int):
        teamEvent = fixture_event_infos.get("team").get("id")
        timeElapsed = fixture_event_infos.get("time").get("elapsed")
        principalPlayer = fixture_event_infos.get("player").get("id")
        assistPlayer = fixture_event_infos.get("assist").get("id")
        typeEvent = fixture_event_infos.get("type")
        detailEvent = fixture_event_infos.get("detail")
        commentEvent = fixture_event_infos.get("comments")

        if principalPlayer is None:
            commentEvent = "coaching_staff"

        dictToReturn = {
            "id_fixture": fixture_id,
            "id_team": teamEvent,
            "time": timeElapsed,
            "id_player_principal": principalPlayer,
            "id_player_assist": assistPlayer,
            "type": typeEvent.lower().replace(" ", "_") if type(typeEvent) == str else None,
            "detail": detailEvent.lower().replace(" ", "_") if type(detailEvent) == str else None,
            "comment": commentEvent.lower().replace(" ", "_") if type(commentEvent) == str else 'null'
        }

        return dictToReturn

    def player_stats_parser(self, player_stats_infos: dict[str:any]) -> dict[str:any]:
        listOfStats: list[dict[str:any]] = []
        for teamInResponse in player_stats_infos:
            idPlayer = teamInResponse.get("player").get("id")
            statisticsRoot = teamInResponse.get("statistics")
            for stats in statisticsRoot:
                idLeague = stats.get("league").get("id")
                seasonLeague = stats.get("league").get("season")
                idTeam = stats.get("team").get("id")
                gamesRoot = stats.get("games")
                substitutesRoot = stats.get("substitutes")
                shotsRoot = stats.get("shots")
                goalsRoot = stats.get("goals")
                passesRoot = stats.get("passes")
                tacklesRoot = stats.get("tackles")
                duelsRoot = stats.get("duels")
                dribblesRoot = stats.get("dribbles")
                foulsRoot = stats.get("fouls")
                cardsRoot = stats.get("cards")
                penaltyRoot = stats.get("penalty")

                playerPosition = gamesRoot.get("position")
                gamesAppearances = gamesRoot.get("appearences")
                lineUps = gamesRoot.get("lineups")
                minutesPlayed = gamesRoot.get("minutes")
                ratingPlayer = "{:.2f}".format(float(gamesRoot.get('rating'))) if gamesRoot.get(
                    'rating') is not None else None
                playerCaptain = gamesRoot.get("captain")

                substitutesIn = substitutesRoot.get("in")
                substitutesOut = substitutesRoot.get("out")
                substitutesBench = substitutesRoot.get("bench")

                shotsTotal = shotsRoot.get("total")
                shotsOn = shotsRoot.get("on")

                goalsTotal = goalsRoot.get("total")
                goalsConceded = goalsRoot.get("conceded")
                goalsAssists = goalsRoot.get("assists")
                goalsSaves = goalsRoot.get("saves")

                passesTotal = passesRoot.get("total")
                passesKey = passesRoot.get("key")
                passesAccuracy = passesRoot.get("accuracy")

                tacklesTotal = tacklesRoot.get("total")
                tacklesBlock = tacklesRoot.get("blocks")
                tacklesInterceptions = tacklesRoot.get("interceptions")

                duelsTotal = duelsRoot.get("total")
                duelsWon = duelsRoot.get("won")

                dribblesAttempts = dribblesRoot.get("attempts")
                dribblesSuccess = dribblesRoot.get("success")
                dribblesPast = dribblesRoot.get("past")

                foulsDrawn = foulsRoot.get("drawm")
                foulsCommitted = foulsRoot.get("committed")

                cardsYellow = cardsRoot.get("yellow")
                cardsYellowRed = cardsRoot.get("yellowred")
                cardsRed = cardsRoot.get("red")

                penaltyWon = penaltyRoot.get("won")
                penaltyCommitted = penaltyRoot.get("committed")
                penaltyScored = penaltyRoot.get("scored")
                penaltyMissed = penaltyRoot.get("missed")
                penaltySaved = penaltyRoot.get("saved")

                dictToReturn = {
                    "id_player": idPlayer, "id_team": idTeam, "season": seasonLeague, "id_league": idLeague,
                    "position": playerPosition, "captain": playerCaptain, "appearances": gamesAppearances,
                    "line_ups": lineUps, "minutes": minutesPlayed,
                    "rating": ratingPlayer, "substitutes_in": substitutesIn, "substitutes_out": substitutesOut,
                    "bench": substitutesBench, "shots_total": shotsTotal,
                    "shots_on": shotsOn, "goals": goalsTotal, "goals_conceded": goalsConceded,
                    "goals_saved": goalsSaves,
                    "assists": goalsAssists, "total_passes": passesTotal,
                    "passes_key": passesKey, "accuracy_passes": passesAccuracy, "tackles_total": tacklesTotal,
                    "blocks": tacklesBlock, "interceptions": tacklesInterceptions,
                    "duels_total": duelsTotal, "duels_win": duelsWon, "dribbles_attempted": dribblesAttempts,
                    "dribbles_success": dribblesSuccess, "dribbles_past": dribblesPast,
                    "fouls_draw": foulsDrawn, "fouls_committed": foulsCommitted, "cards_yellow": cardsYellow,
                    "cards_yellowred": cardsYellowRed, "cards_red": cardsRed,
                    "penalties_won": penaltyWon, "penalties_committed": penaltyCommitted,
                    "penalties_scored": penaltyScored,
                    "penalties_missed": penaltyMissed, "penalties_saved": penaltySaved
                }

                for keyOfStats in list(dictToReturn.keys()):
                    valueStats = dictToReturn.get(keyOfStats)
                    if type(valueStats) == str:
                        valueStats = valueStats.lower().replace(" ", "_")
                        dictToReturn.update({keyOfStats: valueStats})
                    if valueStats is None:
                        valueStats = 0
                        dictToReturn.update({keyOfStats: valueStats})

                listOfStats.append(dictToReturn)

            return listOfStats

    def team_league_fixtures_stats_parser(self, team_league_stats_infos: dict[str:any]) -> dict[str:any]:
        idLeague = team_league_stats_infos.get("league").get("id")
        idTeam = team_league_stats_infos.get("team").get("id")
        fixturesRoot = team_league_stats_infos.get("fixtures")
        cleanSheetRoot = team_league_stats_infos.get("clean_sheet")
        failedToScoreRoot = team_league_stats_infos.get("failed_to_score")
        streakRoot = team_league_stats_infos.get("biggest")

        fixturesHome = fixturesRoot.get("played").get("home")
        fixturesAway = fixturesRoot.get("played").get("away")
        fixturesWinsHome = fixturesRoot.get("wins").get("home")
        fixturesWinsAway = fixturesRoot.get("wins").get("away")
        fixturesDrawsHome = fixturesRoot.get("draws").get("home")
        fixturesDrawsAway = fixturesRoot.get("draws").get("away")
        fixturesLosesHome = fixturesRoot.get("loses").get("home")
        fixturesLosesAway = fixturesRoot.get("loses").get("away")

        cleanSheetsHome = cleanSheetRoot.get("home")
        cleanSheetsAway = cleanSheetRoot.get("away")

        failedToScoreHome = failedToScoreRoot.get("home")
        failedToScoreAway = failedToScoreRoot.get("away")

        maxWinStreak = streakRoot.get("streak").get("wins")
        maxDrawStreak = streakRoot.get("streak").get("draws")
        maxLoseStreak = streakRoot.get("streak").get("loses")

        betterWinHome = streakRoot.get("wins").get("home")
        betterWinAway = streakRoot.get("wins").get("away")
        worstLoseHome = streakRoot.get("loses").get("home")
        worstLoseAway = streakRoot.get("loses").get("away")

        dictToReturn = {
            "id_team": idTeam, "id_league": idLeague, "fixtures_home": fixturesHome, "fixtures_away": fixturesAway,
            "wins_home": fixturesWinsHome, "wins_away": fixturesWinsAway, "draws_home": fixturesDrawsHome,
            "draws_away": fixturesDrawsAway, "loses_home": fixturesLosesHome, "loses_away": fixturesLosesAway,
            "clean_sheets_home": cleanSheetsHome, "clean_sheets_away": cleanSheetsAway,
            "not_scored_home": failedToScoreHome,
            "not_scored_away": failedToScoreAway, "max_wins_streak": maxWinStreak, "max_draws_streak": maxDrawStreak,
            "max_loses_streak": maxLoseStreak, "better_win_home": betterWinHome, "better_win_away": betterWinAway,
            "worst_lose_home": worstLoseHome, "worst_lose_away": worstLoseAway
        }

        for keyValue in list(dictToReturn.keys()):
            valueDict = dictToReturn.get(keyValue)
            if valueDict is None:
                dictToReturn.update({keyValue: 0})

        return dictToReturn

    def team_league_goals_stats_parser(self, team_league_goals_stats_infos: dict[str:any]) -> list[dict[str:str]]:

        goalsRoot = team_league_goals_stats_infos.get("goals")
        listToReturn: list[dict[str:any]] = []

        typesStats = ["for", "against"]
        for typeStat in typesStats:
            idLeague = team_league_goals_stats_infos.get("league").get("id")
            idTeam = team_league_goals_stats_infos.get("team").get("id")
            typeRoot = goalsRoot.get(typeStat)
            minuteRoot = typeRoot.get("minute")
            goalsTotalHome = typeRoot.get("total").get("home")
            goalsTotalAway = typeRoot.get("total").get("away")
            minute0_15 = minuteRoot.get("0-15").get("total")
            minute16_30 = minuteRoot.get("16-30").get("total")
            minute31_45 = minuteRoot.get("31-45").get("total")
            minute46_60 = minuteRoot.get("46-60").get("total")
            minute61_75 = minuteRoot.get("61-75").get("total")
            minute76_90 = minuteRoot.get("76-90").get("total")
            minute91_105 = minuteRoot.get("91-105").get("total")
            minute106_120 = minuteRoot.get("106-120").get("total")

            dictToReturn = {"type": typeStat, "id_league": idLeague, "id_team": idTeam, "goals_home": goalsTotalHome,
                            "goals_away": goalsTotalAway,
                            "in_minute_0_15": minute0_15, "in_minute_16_30": minute16_30,
                            "in_minute_31_45": minute31_45, "in_minute_46_60": minute46_60,
                            "in_minute_61_75": minute61_75,
                            "in_minute_76_90": minute76_90, "in_minute_91_105": minute91_105,
                            "in_minute_106_120": minute106_120
                            }

            for keyValue in list(dictToReturn.keys()):
                valueStat = dictToReturn.get(keyValue)
                if valueStat is None:
                    dictToReturn.update({keyValue: 0})

            listToReturn.append(dictToReturn)

        return listToReturn

    def team_league_cards_stats_parser(self, team_league_cards_stats_infos: dict[str:any]) -> dict[str:str]:
        cardTypes = ["red", "yellow"]

        idLeague = team_league_cards_stats_infos.get("league").get("id")
        idTeam = team_league_cards_stats_infos.get("team").get("id")
        cardsRoot = team_league_cards_stats_infos.get("cards")
        listToReturn: list[dict[str:any]] = []

        for cardType in cardTypes:
            cardTypeRoot = cardsRoot.get(cardType)
            minute0_15 = cardTypeRoot.get("0-15").get("total")
            minute16_30 = cardTypeRoot.get("16-30").get("total")
            minute31_45 = cardTypeRoot.get("31-45").get("total")
            minute46_60 = cardTypeRoot.get("46-60").get("total")
            minute61_75 = cardTypeRoot.get("61-75").get("total")
            minute76_90 = cardTypeRoot.get("76-90").get("total")
            minute91_105 = cardTypeRoot.get("91-105").get("total")
            minute106_120 = cardTypeRoot.get("106-120").get("total")

            dictToReturn = {
                "id_league": idLeague, "id_team": idTeam, "card_type": cardType, "in_minute_0_15": minute0_15,
                "in_minute_16_30": minute16_30, "in_minute_31_45": minute31_45, "in_minute_46_60": minute46_60,
                "in_minute_61_75": minute61_75, "in_minute_76_90": minute76_90, "in_minute_91_105": minute91_105,
                "in_minute_106_120": minute106_120
            }

            for keyValue in list(dictToReturn.keys()):
                valueStat = dictToReturn.get(keyValue)
                if valueStat is None:
                    dictToReturn.update({keyValue: 0})

            listToReturn.append(dictToReturn)

        return listToReturn

    def fixture_lineup_parser(self, fixture_lineup_infos: dict[str:any], id_fixture: str | int) -> dict[str:any]:
        idTeam = fixture_lineup_infos.get("team").get("id")
        typesLineUps = ["startXI", "substitutes"]
        listPlayers = []

        for typeLineUp in typesLineUps:
            typeLineUpRoot = fixture_lineup_infos.get(typeLineUp)
            for player in typeLineUpRoot:
                typeLine = "start" if typeLineUp == 'startXI' else "subst"
                playerRoot = player.get("player")
                idPlayer = playerRoot.get("id")
                posPlayer = playerRoot.get("pos")
                gridPlayer = playerRoot.get("grid") if playerRoot.get("grid") is not None else "0-0"
                dictPlayer = {
                    "id_fixture": id_fixture, "id_team": idTeam, "id_player": idPlayer,
                    "position": posPlayer, "grid": gridPlayer, "type":typeLine
                }
                listPlayers.append(dictPlayer)

        return listPlayers
