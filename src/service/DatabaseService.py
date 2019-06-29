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
        cursor.execute("""SELECT temperature, messTime FROM temperature WHERE messTime > ?""", ([checkDate]))
        result = cursor.fetchall()
        daysMiddle = float(0)
        for row in result:
            daysMiddle += row[0]
            
        if (len(result) != 0):
            return daysMiddle/len(result)
        return 17

    def checkRained(self):
        cursor = self.connection.cursor()
        checkDate = date.today() - timedelta(days=2)
        checkDate = checkDate.strftime('%s')
        cursor.execute("""SELECT rain, date(rainTime) FROM rain WHERE rainTime > ?""", ([checkDate]))
        result = cursor.fetchall()
        thisDay = (date.today()).strftime('%Y-%m-%d')
        checkYesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        checkBeforeYesterday = (date.today() - timedelta(days=2)).strftime('%Y-%m-%d')
        checkResult = False
        for row in result:
            if (bool(row[0])):
                if (row[1] == thisDay):
                    if (self.checkRainDuration(row[1]) > 15):
                        return True
                    else:
                        checkResult = False
                elif (row[1] == checkYesterday):
                    if (self.checkRainDuration(row[1]) > 15):
                        return True
                    else:
                        checkResult = False
                else:
                    checkResult = checkResult
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

    def clean(self):
            cursor = self.connection.cursor()
            getDate = date.today() - timedelta(days=3)
            getDate = getDate.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""DELETE FROM temperature WHERE messTime < ?""", ([getDate]))
            cursor.execute("""DELETE FROM rain WHERE rainTime < ?""", ([getDate]))
            self.connection.commit()

    def closeConnection(self):
        self.connection.close
