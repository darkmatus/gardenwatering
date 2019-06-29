from DatabaseService import DatabaseService

class CheckService:

    def __init__(self):
        self.databaseService = DatabaseService()

    def check(self):
        temperatur = self.databaseService.checkTemperatur()
        rained = self.databaseService.checkRained()
        if (rained == False) and (round(temperatur) > 18):
            return True
        elif (rained == True and round(temperatur) > 23):
            return True
        else:
            return False
