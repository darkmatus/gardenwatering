import RPi.GPIO as GPIO
from src.service.DatabaseService import DatabaseService


class RainChecker:
    pin = 17  # GPIO fuer den Regensensor

    def checkRain(self):
        print self.pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)
        # 0 for rain, 1 for no rain! we need to map it
        rain = GPIO.input(self.pin)
        dbService = DatabaseService()
        dbService.saveRainStatus(self.mapRain(rain))
        
    def mapRain(self, rain):
        if rain == 1:
            return 0
        else:
            return 1
