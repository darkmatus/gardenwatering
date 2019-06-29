from src.Timer import Timer
from src.UsbSwitcher import UsbSwitcher
from src.service.CheckService import CheckService

checkService = CheckService()

if (checkService.check()):
    switcher = UsbSwitcher()
    switcher.switch()
    timer = Timer()
    timer.timer()
    switcher.switch()
