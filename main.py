from src.TempChecker import TempChecker
from src.RainChecker import RainChecker
import sched, time

rainScheduler = sched.scheduler(time.time, time.sleep)
tempScheduler = sched.scheduler(time.time, time.sleep)

def rainChecker(sc):
    rainCheck = RainChecker()
    rainCheck.checkRain()
    rainScheduler.enter(300, 1, rainChecker, (sc,))

rainScheduler.enter(10, 1, rainChecker, (rainScheduler,))
rainScheduler.run()

def tempCheck(tempSched):
    tempChecker = TempChecker()
    tempChecker.check()
    tempScheduler.enter(14400, 1, tempCheck, (tempSched,))

tempScheduler.enter(11, 1, tempCheck, (tempScheduler,))
tempScheduler.run()