import threading

class Monitor:
    def __init__(self):
        self.cond = threading.Condition()

    def run(self, should_wait, action):
        with self.cond:
            while should_wait():
                self.cond.wait()

            val = action()

            self.cond.notify_all()
            return val
