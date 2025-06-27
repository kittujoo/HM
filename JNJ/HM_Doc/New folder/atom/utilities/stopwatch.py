from time import time


class InvalidOperationException(Exception):
    pass


class StopWatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        if self.start_time:
            raise InvalidOperationException("Timer was already started")
        self.start_time = time()
        return self

    def end(self):
        if self.end_time:
            raise InvalidOperationException("Timer was already finished")
        self.end_time = time()
        return self

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()

    def elapsed(self, digits=2):
        if self.start_time is None:
            raise ValueError("You forgot to start the timer")
        return round((self.end_time or time()) - self.start_time, digits)

    def __repr__(self):
        return str(self.elapsed())

    def __str__(self):
        return self.__repr__()


stopwatch = StopWatch
