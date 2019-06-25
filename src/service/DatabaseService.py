import sqlite3
import os
from datetime import date, datetime, timedelta
from __builtin__ import False

class DatabaseService:
    
    def __init__(self):
        self._createTables()
    
    def _createTables(self):
        self.connection = self.getConnection()
        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS temperature (temperature real, messTime int)")
        cursor.execute("CREATE TABLE IF NOT EXISTS rain(rain int, rainTime int)")
        cursor.execute("CREATE TABLE IF NOT EXISTS powerLog (status int, time int)")
        self.connection.commit()
            
    def getConnection(self):
        dirpath = os.getcwd()
        dbFile = dirpath + "/database/temperature.db"
        return sqlite3.connect(dbFile)

    # save the given temperature for the actual day
    def saveTemperature(self, temperature):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO temperature (temperature, messTime) VALUES (?, ?)", (int(temperature), date.today()))
        self.connection.commit()

    # save the given rain status for the actual messuring
    def saveRainStatus(self, rain):
        cursor = self.connection.cursor()
        statement = "INSERT INTO rain (rain, rainTime) VALUES (?, ?)"
        cursor.execute(statement, (rain, date.today()))
        self.connection.commit()

    # save the date when it is switched on and off
    def saveSwitchedOn(self, status):
        cursor = self.connection.cursor()
        statement = "INSERT INTO powerLog (status, time) VALUES (?, ?)"
        cursor.execute(statement, (status, date.today()))
        self.connection.commit()        
        
    def checkTemperatur(self):
        cursor = self.connection.cursor()
        checkDate = date.today() - timedelta(days=3)
        checkDate = checkDate.strftime('%s')
        cursor.execute("""SELECT temperature, messDate FROM temperature WHERE messTime > ?""", ([checkDate]))
        result = cursor.fetchall()
        daysMiddle = float(0)
        for row in result:
            daysMiddle += row[0]
            
        return daysMiddle/len(result)
    
    def checkRained(self):
        cursor = self.connection.cursor()
        checkDate = date.today() - timedelta(days=2)
        cursor.execute('''INSERT INTO rain (rain, rainTime) VALUES (?,?)''', (0, datetime.now()))
        cursor.execute('''INSERT INTO rain (rain, rainTime) VALUES (?,?)''', (1, '2019-06-23 15:23:34'))
        cursor.execute('''INSERT INTO rain (rain, rainTime) VALUES (?,?)''', (0, '2019-06-22 15:23:34'))
        checkDate = checkDate.strftime('%s')
        cursor.execute("""SELECT rain, date(rainTime) FROM rain WHERE rainTime > ?""", ([checkDate]))
        result = cursor.fetchall()
        checkYesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        checkBeforeYesterday = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
        checkResult = False
        for row in result:
            if (bool(row[0])):
                if (row[1] == checkYesterday):
                    if (self.checkRainDuration(row[1]) > 15):
                        checkResult = True
                    else:
                        checkResult = False
                elif(row[1] == checkBeforeYesterday):
                    checkResult &= False
                else:
                    checkResult &= False
        return checkResult

    def checkRainDuration(self, toCheck):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT rain FROM rain WHERE rainTime = ?''', toCheck)
        result = cursor.fetchall()
        duration = 0;
        for row in result:
            if (row[0] == 1):
                duration += 3
                
        return duration

    def closeConnection(self):
        self.connection.close