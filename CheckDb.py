import sqlite3
from datetime import date, timedelta, datetime

class CheckDb:
    
    def __init__(self):	
        self.connect()
        self.create()

    def connect(self):
        self.connection = sqlite3.connect('./temperature.db')

    def create(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS temperature (temperature REAL, messDate int)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS rain (rained, messDate int)''')
        self.connection.commit()
    
    def check(self):
        temperatur = self.checkTemperatur()
        rained = self.checkRained()
        print(rained, temperatur)
        if (rained == False):
            if (round(temperatur) > 21):
                return True

    def checkTemperatur(self):
        cursor = self.connection.cursor()
        checkDate = date.today() - timedelta(days=3)
        checkDate = checkDate.strftime('%s')
        cursor.execute("""SELECT temperature, messDate FROM temperature WHERE messDate > ?""", ([checkDate]))
        result = cursor.fetchall()
        daysMiddle = float(0)
        for row in result:
            daysMiddle += row[0]
            
        return daysMiddle/len(result)
    
    def checkRained(self):
        cursor = self.connection.cursor()
        checkDate = date.today() - timedelta(days=2)
        cursor.execute('''INSERT INTO rain (rained, messDate) VALUES (?,?)''', (0, datetime.now()))
        cursor.execute('''INSERT INTO rain (rained, messDate) VALUES (?,?)''', (1, '2019-06-23 15:23:34'))
        cursor.execute('''INSERT INTO rain (rained, messDate) VALUES (?,?)''', (0, '2019-06-22 15:23:34'))
        checkDate = checkDate.strftime('%s')
        # change to rain table
        cursor.execute("""SELECT rained, date(messDate )FROM rain WHERE messDate > ?""", ([checkDate]))
        result = cursor.fetchall()
        checkYesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        checkBeforeYesterday = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
        checkResult = False
        for row in result:
            if (bool(row[0])):
                if (row[1] == checkYesterday):
                    # add check how long it has rained
                    checkResult = True
                elif(row[1] == checkBeforeYesterday):
                    checkResult &= False
                else:
                    checkResult &= False
        return checkResult