from DatabaseService import DatabaseService

class CheckService:

    def __init__(self):
        self.databaseService = DatabaseService()

    def check(self):
        temperatur = self.databaseService.checkTemperatur()
        rained = self.databaseService.checkRained()
        print(rained, temperatur)
        if (rained == False):
            if (round(temperatur) > 21):
                return True
