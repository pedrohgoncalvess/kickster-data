from datetime import datetime as dt
import datetime


class Validators:
    def __init__(self):
        self.actualYear = int(dt.now().year)

    def stadium_validator(self, stadium_infos: dict[str:str]) -> dict[str:str]:
        idExStadium = stadium_infos.get('id')
        nameStadium = stadium_infos.get("name")
        addressStadium = stadium_infos.get('address')
        capacityStadium = stadium_infos.get('capacity')
        surfaceStadium = stadium_infos.get('surface')
        imageStadium = stadium_infos.get('image')

        try:
            stateStadium = stadium_infos.get('city').split(',')[1]
            cityStatium = stadium_infos.get('city').split(',')[0]
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

    def team_validator(self, team_info: dict[str:any]) -> dict[str:str]:

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

    def league_validator(self, league_infos: dict[str:dict[str:str]]) -> dict[str:str]:

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
            "id": idLeague,
            "name": nameLeague,
            "logo": logoLeague,
            "type": typeLeague,
            "country": countryLeague,
            "start": startLeague,
            "end": endLeague,
            "season": self.actualYear
        }

        return dictToReturn

    def player_validator(self, player_infos: dict[str:any]) -> dict[str:any]:

        playerRoot = player_infos.get('player')
        playerID = playerRoot.get('id')
        playerName = playerRoot.get('name')
        playerFirstName = playerRoot.get('firstname')
        playerLastName = playerRoot.get('lastname')
        playerBirth = playerRoot.get('birth').get('date')
        playerNationality = playerRoot.get('nationality')
        playerHeight = playerRoot.get('height').replace(' cm', '') if playerRoot.get('height') is not None else 0
        playerWeight = playerRoot.get('weight').replace(' kg', '') if playerRoot.get('weight') is not None else 0
        playerPhoto = playerRoot.get('photo')
        playerInjured = playerRoot.get("injured")

        dictToReturn = {
            "id": playerID,
            "name": playerName,
            "first_name": playerFirstName,
            "last_name": playerLastName,
            "birth": playerBirth,
            "nationality": playerNationality,
            "height": playerHeight,
            "weight": playerWeight,
            "photo": playerPhoto,
            "injured": playerInjured
        }

        return dictToReturn

    def fixture_validator(self, fixture_infos: dict[str:any]) -> dict[str:str]:

        fixtureInfos: dict[str:any] = fixture_infos.get("fixture")
        leagueInfo = fixture_infos.get("league")
        teamsInfo = fixture_infos.get("teams")
        saoPauloTz = datetime.timezone(datetime.timedelta(hours=-3))

        idFixture: str = fixtureInfos.get("id")
        refereeFixture: str = fixtureInfos.get("referee")
        datetimeFixture = dt.fromtimestamp(fixtureInfos.get("periods").get("first"), saoPauloTz) if fixtureInfos.get(
            "periods").get("first") is not None else dt.utcfromtimestamp(946684800)

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
            "stadium": idStadium,
            "home_team": homeTeam,
            "away_team": awayTeam,
            "id_league": idLeague,
            "round": roundLeague,
            "season": seasonLeague,
            "result": winnerTeam,
            "status": statusFixture
        }

        return dictToReturn

    def team_squad_validator(self, team_squad_infos: dict[str:any]) -> list[dict[str:str]]:

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

    def fixture_stats_validator(self, team_fixture_stats_infos: dict[str:any], fixture_id: int):

        idTeam = team_fixture_stats_infos.get("team").get("id")
        statisticsRoot = team_fixture_stats_infos.get("statistics")
        dictToReturn: dict[str:any] = {"id_team": idTeam, "id_fixture": fixture_id}

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

    def fixture_events_validator(self, fixture_event_infos: dict[str:any], fixture_id: int):
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

    def player_stats_validator(self, player_stats_infos: dict[str:any]):
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
                ratingPlayer = "{:.2f}".format(float(gamesRoot.get('rating'))) if gamesRoot.get('rating') is not None else None
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
                    "shots_on": shotsOn, "goals": goalsTotal, "goals_conceded": goalsConceded, "goals_saved": goalsSaves,
                    "assists": goalsAssists, "total_passes": passesTotal,
                    "passes_key": passesKey, "accuracy_passes": passesAccuracy, "tackles_total": tacklesTotal,
                    "blocks": tacklesBlock, "interceptions": tacklesInterceptions,
                    "duels_total": duelsTotal, "duels_win": duelsWon, "dribbles_attempted": dribblesAttempts,
                    "dribbles_success": dribblesSuccess, "dribbles_past": dribblesPast,
                    "fouls_draw": foulsDrawn, "fouls_committed": foulsCommitted, "cards_yellow": cardsYellow,
                    "cards_yellowred": cardsYellowRed, "cards_red": cardsRed,
                    "penalties_won": penaltyWon, "penalties_committed": penaltyCommitted, "penalties_scored": penaltyScored,
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
