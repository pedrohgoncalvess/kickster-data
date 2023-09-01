from datetime import datetime


class Validators:
    def __init__(self):
        self.actualYear = int(datetime.now().year)

    def stadium_validator(self, stadium_infos: dict[str:str]) -> dict[str:str]:
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

    def champ_validator(self, champ_infos: dict[str:dict[str:str]]) -> dict[str:str]:

        idChamp = champ_infos.get('league').get('id')
        nameChamp = champ_infos.get('league').get('name')
        typeChamp = champ_infos.get('league').get('type')
        logoChamp = champ_infos.get('league').get('logo')
        countryChamp = champ_infos.get('country').get('name')

        seasonsInformation: list[dict[str:str]] = champ_infos.get('seasons')
        for seasonInfo in seasonsInformation:
            if seasonInfo.get('year') == self.actualYear:
                startChamp = seasonInfo.get('start')
                endChamp = seasonInfo.get('end')
            else:
                startChamp = f'{self.actualYear}-01-01'
                endChamp = f'{self.actualYear}-01-01'

        dictToReturn = {
            "id": idChamp,
            "name": nameChamp,
            "logo": logoChamp,
            "type": typeChamp,
            "country": countryChamp,
            "start": startChamp,
            "end": endChamp,
            "season": self.actualYear
        }

        return dictToReturn

    def player_validator(self, player_infos) -> dict[str:any]:

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

        dictToReturn = {
            "id": playerID,
            "name": playerName,
            "first_name": playerFirstName,
            "last_name": playerLastName,
            "birth": playerBirth,
            "nationality": playerNationality,
            "height": playerHeight,
            "weight": playerWeight,
            "photo": playerPhoto
        }

        return dictToReturn
