from DatabaseService import DatabaseService

class CheckService:

    def __init__(self):
        self.databaseService = DatabaseService()

    def check(self):
        temperatur = self.databaseService.checkTemperatur()
        rained = self.databaseService.checkRained()
        print(rained, temperatur)
        if (rained == False) and (round(temperatur) > 19):
            return True
        elif (rained == True & round(temperatur) > 23):
            return True
        else:
            return False