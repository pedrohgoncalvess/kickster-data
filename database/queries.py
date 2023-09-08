from typing import NoReturn


class Queries:
    def __init__(self):
        self.get_all_team_id = "select id_team from football_data.teams"
        self.get_all_champ_id = "select id_champ from football_data.champs"
        self.get_all_teams_id_serie_a = "select distinct(team.id_team) as id_team from football_data.fixtures fx inner join football_data.teams team on team.id = fx.id_team_home where fx.id_league = 1"
        self.get_all_fixtures_id = "select id_fixture from football_data.fixtures"

    def update_fixture_data_status(self, id_fixture: int) -> NoReturn:
        return f"update football_data.fixtures set data_status = 'collected' where id_fixture = {id_fixture}"

    def insert_stadium(self, stadium_values: dict[str:str]) -> str:

        idExStadium = stadium_values.get('id')
        nameStadium = stadium_values.get('name')
        stateStadium = stadium_values.get('state')
        cityStatium = stadium_values.get('city')
        addressStatium = stadium_values.get('address')
        capacityStatium = stadium_values.get('capacity')
        surfaceStadium = stadium_values.get('surface')
        imageStadium = stadium_values.get('image')

        queryInsert = f"""

        insert into "football_data".stadiums (id_stadium, "name", state, city, address, capacity, surface, image)
        values ({idExStadium}, '{nameStadium}', '{stateStadium}', '{cityStatium}', '{addressStatium}', {capacityStatium}, '{surfaceStadium}', '{imageStadium}')

        """

        return queryInsert

    def insert_team(self, team_values: dict[str:str]) -> str:

        idExTeam = team_values.get('id')
        idStadium = team_values.get('id_stadium')
        nameTeam = team_values.get('name')
        logoTeam = team_values.get('logo')
        nationalTeam = team_values.get('national')
        codeTeam = team_values.get('code')
        countryTeam = team_values.get('country')
        foundedTeam = team_values.get('founded')

        if idStadium is not None:
            queryInsert = f"""
            insert into football_data.teams (id_team, id_stadium, code, "name", country, logo, founded, "national") values
            ({idExTeam}, (select id from football_data.stadiums where id_stadium = {idStadium}), '{codeTeam}', '{nameTeam}', '{countryTeam}', '{logoTeam}', {foundedTeam}, {nationalTeam})       
            """
        else:
            queryInsert = f"""
                        insert into football_data.teams (id_team, code, "name", country, logo, founded, "national") values
                        ({idExTeam}, '{codeTeam}', '{nameTeam}', '{countryTeam}', '{logoTeam}', {foundedTeam}, {nationalTeam})       
                        """

        return queryInsert

    def insert_champ(self, champ_values: dict[str:any]) -> str:

        idChamp = champ_values.get("id")
        nameChamp = champ_values.get('name')
        startChamp = champ_values.get('start')
        endChamp = champ_values.get('end')
        logoChamp = champ_values.get('logo')
        countryChamp = champ_values.get('country')
        typeChamp = champ_values.get('type')
        seasonChamp = champ_values.get('season')

        queryInsert = f"""
        insert into football_data.champs (id_champ,"name",country,"type",season,start_champ,end_champ,logo)
        values ({idChamp},'{nameChamp}','{countryChamp}','{typeChamp}',{seasonChamp},'{startChamp}','{endChamp}','{logoChamp}')
        """

        return queryInsert

    def insert_player(self, player_values: dict[str:any]) -> str:

        idPlayer = player_values.get('id')
        namePlayer = player_values.get('name')
        firstNamePlayer = player_values.get('first_name')
        lastNamePlayer = player_values.get('last_name')
        birthPlayer = player_values.get('birth')
        nationalityPlayer = player_values.get('nationality')
        heightPlayer = player_values.get('height')
        weightPlayer = player_values.get('weight')
        photoPlayer = player_values.get('photo')

        queryInsert = f"""
        insert into football_data.players (id_player, "name", first_name, last_name, date_of_birth, nationality, height, weight,photo)
        values ({idPlayer},'{namePlayer}','{firstNamePlayer}','{lastNamePlayer}','{birthPlayer}','{nationalityPlayer}',{heightPlayer},{weightPlayer},'{photoPlayer}')
        """

        return queryInsert

    def insert_fixture(self, fixture_values: dict[str:any]) -> str:
        idFixture = fixture_values.get("id_fixture")
        dateFixture = fixture_values.get("date")
        refereeFixture = fixture_values.get("referee")
        idStadiumFixture = fixture_values.get("stadium")
        idHomeTeamFixture = fixture_values.get("home_team")
        idAwayTeamFixture = fixture_values.get("away_team")
        idLeague = fixture_values.get("id_league")
        roundFixture = fixture_values.get("round")
        seasonFixture = fixture_values.get("season")
        resultFixture = fixture_values.get("result")
        statusFixture = fixture_values.get("status")

        if idStadiumFixture != None:
            queryInsert = f"""
            insert into football_data.fixtures (id_fixture,id_stadium,id_league,id_team_home,id_team_away,start_at,result,round,referee,status) 
            values 
            ({idFixture},
            (select id from football_data.stadiums where id_stadium = {idStadiumFixture}),
            (select id from football_data.champs where id_champ = {idLeague} and season = {seasonFixture}),
            (select id from football_data.teams where id_team = {idHomeTeamFixture}),
            (select id from football_data.teams where id_team = {idAwayTeamFixture}),
            '{dateFixture}',
            '{resultFixture}',
            '{roundFixture}',
            '{refereeFixture}',
            '{statusFixture}'
            )
            """
        else:
            queryInsert = f"""
            insert into football_data.fixtures (id_fixture,id_league,id_team_home,id_team_away,start_at,result,round,referee,status) 
            values 
            ({idFixture},
            (select id from football_data.champs where id_champ = {idLeague} and season = {seasonFixture}),
            (select id from football_data.teams where id_team = {idHomeTeamFixture}),
            (select id from football_data.teams where id_team = {idAwayTeamFixture}),
            '{dateFixture}',
            '{resultFixture}',
            '{roundFixture}',
            '{refereeFixture}',
            '{statusFixture}'
            )
            """

        return queryInsert

    def insert_team_player_squad(self, player_squad_infos: dict[str:any]):
        idPlayer = player_squad_infos.get("id_player")
        idTeam = player_squad_infos.get("id_team")
        positionPlayer = player_squad_infos.get("position")
        numberPlayer = player_squad_infos.get("number")

        queryInsert = f"""
        insert into football_data.teams_squad (id_team, id_player, shirt_number, "position") 
        values
         (
         (select id from football_data.teams where id_team = {idTeam}),
         (select id from football_data.players where id_player = {idPlayer}),
         {numberPlayer},
         '{positionPlayer}'
         )
        """

        return queryInsert

    def insert_fixture_stats(self, team_fixture_stats_infos: dict[str:any]):

        idFixture = team_fixture_stats_infos.get("id_fixture")
        idTeam = team_fixture_stats_infos.get("id_team")
        shotsOnGoal = team_fixture_stats_infos.get("shots_on_goal")
        shotsOffGoal = team_fixture_stats_infos.get("shots_off_goal")
        shotsBlocked = team_fixture_stats_infos.get("blocked_shots")
        shotsInsideBox = team_fixture_stats_infos.get("shots_insidebox")
        shotsOutsideBox = team_fixture_stats_infos.get("shots_outsidebox")
        fouls = team_fixture_stats_infos.get("fouls")
        cornerKicks = team_fixture_stats_infos.get("corner_kicks")
        offSides = team_fixture_stats_infos.get("offsides")
        ballPossession = team_fixture_stats_infos.get("ball_possession")
        yellowCards = team_fixture_stats_infos.get("yellow_cards")
        redCards = team_fixture_stats_infos.get("red_cards")
        goalKeeperSaves = team_fixture_stats_infos.get("goalkeeper_saves")
        totalPasses = team_fixture_stats_infos.get("total_passes")
        accuratePasses = team_fixture_stats_infos.get("passes_accurate")
        expectedGoals = team_fixture_stats_infos.get("expected_goals")

        queryInsert = f"""
        insert into football_data.fixtures_stats (id_fixture, id_team, home, shots_on_goal, shots_off_goal, shots_blocked, shots_inside_box, shots_offside_box, fouls, corners, offsides, possession, yellow_cards, red_cards, goalkeeper_saves, total_passes, accurate_passes, expected_goals)
        values (
        (select id from football_data.fixtures where id_fixture = {idFixture}),
        (select id from football_data.teams where id_team = {idTeam}),
        (select case when id_team_home = (select id from football_data.teams where id_team = {idTeam}) then true else false end from football_data.fixtures where id_fixture = {idFixture}),
        {shotsOnGoal},
        {shotsOffGoal},
        {shotsBlocked},
        {shotsInsideBox},
        {shotsOutsideBox},
        {fouls},
        {cornerKicks},
        {offSides},
        {ballPossession},
        {yellowCards},
        {redCards},
        {goalKeeperSaves},
        {totalPasses},
        {accuratePasses},
        {expectedGoals}
        )
        """

        return queryInsert


    def insert_fixture_event(self, fixture_events_infos: dict[str:any]) -> str:
        idTeam = fixture_events_infos.get("id_team")
        idFixture = fixture_events_infos.get("id_fixture")
        timeElapsed = fixture_events_infos.get("time")
        idPrincipalPlayer = fixture_events_infos.get("id_player_principal")
        idPlayerAssist = fixture_events_infos.get("id_player_assist")
        typeEvent = fixture_events_infos.get("type")
        detailEvent = fixture_events_infos.get("detail")
        commentEvent = fixture_events_infos.get("comment")

        if idPlayerAssist is not None:
            queryInsert = f"""
            insert into football_data.fixtures_events (id_team, id_fixture, id_player_principal, id_player_assist, "time", type_event, "detail", "comments")
            values (
            (select id from football_data.teams where id_team = {idTeam}),
            (select id from football_data.fixtures where id_fixture = {idFixture}),
            (select id from football_data.players where id_player = {idPrincipalPlayer}),
            (select id from football_data.players where id_player = {idPlayerAssist}),
            {timeElapsed},
            '{typeEvent}',
            '{detailEvent}',
            '{commentEvent}'
            )
            """
        else:
            queryInsert = f"""
            insert into football_data.fixtures_events (id_team, id_fixture, id_player_principal, "time", type_event, "detail", "comments")
            values (
            (select id from football_data.teams where id_team = {idTeam}),
            (select id from football_data.fixtures where id_fixture = {idFixture}),
            (select id from football_data.players where id_player = {idPrincipalPlayer}),
            {timeElapsed},
            '{typeEvent}',
            '{detailEvent}',
            '{commentEvent}'
            )
            """
            if idPrincipalPlayer is None:
                queryInsert = f"""
                insert into football_data.fixtures_events (id_team, id_fixture, "time", type_event, "detail", "comments")
                values (
                (select id from football_data.teams where id_team = {idTeam}),
                (select id from football_data.fixtures where id_fixture = {idFixture}),
                {timeElapsed},
                '{typeEvent}',
                '{detailEvent}',
                '{commentEvent}'
                )
                """

        return queryInsert
