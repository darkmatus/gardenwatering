import os

class UsbSwitcher:

    status = False;
    
    def switch(self):
        if self.status == True:
            commandResult = os.popen('sispmctl -o 0').read()
            self.status = False
        else:
            commandResult = os.popen('sispmctl -o 1').read()
            self.status = True