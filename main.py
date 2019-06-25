#from src.Timer import Timer
#from src.UsbSwitcher import UsbSwitcher
from src.TempChecker import TempChecker
#from src.RainChecker import RainChecker
import sched, time

#rainScheduler = sched.scheduler(time.time, time.sleep)
tempScheduler = sched.scheduler(time.time, time.sleep)

#def rainChecker(sc):
#    rainCheck = RainChecker()
#    rainCheck.check
#    rainScheduler.enter(600, 1, rainChecker, (sc,))

#rainScheduler.enter(10, 1, rainChecker, (rainScheduler,))
#rainScheduler.run()

def tempCheck(tempSched):
    tempChecker = TempChecker()
    tempChecker.check()
    tempScheduler.enter(14400, 1, tempCheck, (tempSched,))

tempScheduler.enter(11, 1, tempCheck, (tempScheduler,))
tempScheduler.run()
#switcher = UsbSwitcher()
#switcher.switch()
#timer = Timer()
#timer.timer()
#switcher.switch()
