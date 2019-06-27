from src.Timer import Timer
from src.UsbSwitcher import UsbSwitcher

switcher = UsbSwitcher()
switcher.switch()
timer = Timer()
timer.timer()
switcher.switch()