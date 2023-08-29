from database.database import DatabaseConnection
from typing import NoReturn
from database.validators import Validators


class Operations:
    validator = Validators()

    @classmethod
    def insert_stadium(cls, stadium_infos: dict[str:str]) -> NoReturn:

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        stadiumInfosTreated: dict = cls.validator.stadium_validator(stadium_infos)

        idExStadium = stadiumInfosTreated.get('id')
        nameStadium = stadiumInfosTreated.get("name")
        stateStadium = stadiumInfosTreated.get('state')
        cityStatium = stadiumInfosTreated.get('city')
        addressStatium = stadiumInfosTreated.get('address')
        capacityStatium = stadiumInfosTreated.get('capacity')
        surfaceStadium = stadiumInfosTreated.get('surface')
        imageStadium = stadiumInfosTreated.get('image')

        queryInsert = f"""
        
        insert into "football_data".stadiums (id_stadium, "name", state, city, address, capacity, surface, image)
        values ({idExStadium}, '{nameStadium}', '{stateStadium}', '{cityStatium}', '{addressStatium}', {capacityStatium}, '{surfaceStadium}', '{imageStadium}')
        
        """

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except:
            connection.rollback()

        finally:
            connection.close()

    @classmethod
    def insert_team(cls, team_info: dict[str:any]) -> NoReturn:

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        teamInfos = cls.validator.team_validator(team_info)

        idExTeam = teamInfos.get('id')
        idStadium = teamInfos.get('id_stadium')
        nameTeam = teamInfos.get('name')
        logoTeam = teamInfos.get('logo')
        nationalTeam = teamInfos.get('national')
        codeTeam = teamInfos.get('code')
        countryTeam = teamInfos.get('country')
        foundedTeam = teamInfos.get('founded')

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

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except:
            connection.rollback()

        finally:
            connection.close()

    @classmethod
    def insert_champ(cls, champ_infos:dict[str, dict]):

        connection = DatabaseConnection().connection
        cursor = connection.cursor()

        champInfos = cls.validator.champ_validator(champ_infos)

        idChamp = champInfos.get("id")
        nameChamp = champInfos.get('name')
        startChamp = champInfos.get('start')
        endChamp = champInfos.get('end')
        logoChamp = champInfos.get('logo')
        countryChamp = champInfos.get('country')
        typeChamp = champInfos.get('type')
        seasonChamp = champInfos.get('season')

        queryInsert = f"""
        insert into football_data.champs (id_champ,"name",country,"type",season,start_champ,end_champ,logo)
        values ({idChamp},'{nameChamp}','{countryChamp}','{typeChamp}',{seasonChamp},'{startChamp}','{endChamp}','{logoChamp}')
        """

        try:
            cursor.execute(queryInsert)
            connection.commit()

        except Exception as error:
            print(error)
            connection.rollback()

        finally:
            connection.close()


dbOperations = Operations
