class Queries:
    def __init__(self):
        self.get_all_team_id = "select id_team from football_data.teams"
        self.get_all_champ_id = "select id_champ from football_data.champs"

    def insert_stadium(self, stadium_values:dict[str:str]) -> str:

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


    def insert_team(self, team_values:dict[str:str]) -> str:

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

    def insert_champ(self, champ_values:dict[str:any]) -> str:

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

    def insert_player(self, player_values:dict[str:any]) -> str:

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
        insert into football_data.players (id_player, "name", first_name, last_name, date_of_birth, nationality, height, weight, photo)
        values ({idPlayer},'{namePlayer}','{firstNamePlayer}','{lastNamePlayer}','{birthPlayer}','{nationalityPlayer}',{heightPlayer},{weightPlayer}, '{photoPlayer}')
        """

        return queryInsert


