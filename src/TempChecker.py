import Adafruit_DHT
from src.service.DatabaseService import DatabaseService

class TempChecker:
    pin = 4

    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
    
    def check(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        dbService = DatabaseService()
        dbService.saveTemperature(temperature)
