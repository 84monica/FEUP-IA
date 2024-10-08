import threading
import time

class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.count = 0

    def run(self):
        while self.count >= 0 and not self.event.is_set():
            # print (self.count)
            self.count += 1
            self.event.wait(1)

    def stop(self):
        self.event.set()

    def get_count(self):
        return self.count