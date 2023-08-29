from datetime import datetime


class Validators:
    actualYear = int(datetime.now().year)

    @classmethod
    def stadium_validator(cls, stadium_infos: dict[str:str]) -> dict[str:str]:
        idExStadium = stadium_infos.get('id')
        nameStadium = stadium_infos.get("name")
        addressStatium = stadium_infos.get('address')
        capacityStatium = stadium_infos.get('capacity')
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
            "address": addressStatium,
            "capacity": capacityStatium,
            "surface": surfaceStadium,
            "image": imageStadium,
            "state": stateStadium,
            "city": cityStatium
        }

        return dictToReturn

    @classmethod
    def team_validator(cls, team_info: dict[str:any]) -> dict[str:str]:

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

    @classmethod
    def champ_validator(cls, champ_infos: dict[str:dict[str:str]]) -> dict[str:str]:

        idChamp = champ_infos.get('league').get('id')
        nameChamp = champ_infos.get('league').get('name')
        typeChamp = champ_infos.get('league').get('type')
        logoChamp = champ_infos.get('league').get('logo')
        countryChamp = champ_infos.get('country').get('name')

        seasonsInformation: list[dict[str:str]] = champ_infos.get('seasons')
        for seasonInfo in seasonsInformation:
            if seasonInfo.get('year') == cls.actualYear:
                startChamp = seasonInfo.get('start')
                endChamp = seasonInfo.get('end')
            else:
                startChamp = f'{cls.actualYear}-01-01'
                endChamp = f'{cls.actualYear}-01-01'

        dictToReturn = {
            "id": idChamp,
            "name": nameChamp,
            "logo": logoChamp,
            "type": typeChamp,
            "country": countryChamp,
            "start": startChamp,
            "end": endChamp,
            "season": cls.actualYear
        }

        return dictToReturn
