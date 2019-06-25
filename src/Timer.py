import time

class Timer:
    minutes = 0
    def timer(self):
        mins = 0
        # Loop until we reach 2 minutes running
        while self.minutes != 2:
            print ">>>>>>>>>>>>>>>>>>>>>", self.minutes #@TODO remove debug output
            # Sleep for a minute
            time.sleep(60)
            # Increment the minute total
            self.minutes += 1
        #@TODO remove debug output
        print ">>>>>>>>>>>>>>>>>>>>>", self.minutes , "End"
            