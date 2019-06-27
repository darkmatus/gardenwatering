import time

class Timer:
    minutes = 1
    def timer(self):
        # Loop until we reach 2 minutes running
        while self.minutes != 5:
            print self.minutes
            # Sleep for a minute
            time.sleep(60)
            # Increment the minute total
            self.minutes += 1
            