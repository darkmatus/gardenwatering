import os

class UsbSwitcher:

    status = False;
    
    def switch(self):
        if self.status == True:
            commandResult = os.popen('sispmctl -o 0').read()
            #@TODO remove debug output
            print "switch off"
            print(commandResult)
        else:
            #@TODO remove debug output
            commandResult = os.popen('sispmctl -o 1').read()
            self.status = True
            print(commandResult)
            print "switch on"