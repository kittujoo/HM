from time import time

from utilities.types import Int_Or_Float


class InvalidOperationException(Exception):
    pass


class Timer:
    def __init__(self, timer_in_seconds: Int_Or_Float):
        if timer_in_seconds < 0:
            raise ValueError("Timer must be greater than 0")
        self._timer_in_seconds = timer_in_seconds
        self._end_time_value = None

    @property
    def _end_time(self):
        if not self._end_time_value:
            raise InvalidOperationException("Timer was not started")
        return self._end_time_value

    @_end_time.setter
    def _end_time(self, value: Int_Or_Float):
        self._end_time_value = value

    def start(self):
        self._end_time = time() + self._timer_in_seconds
        return self

    def __bool__(self):
        return time() < self._end_time

    def remains(self, digits=2):
        if time() > self._end_time:
            return 0
        return round((self._end_time - time()), digits)

    def __repr__(self):
        return str(f"Timer for {self._timer_in_seconds} seconds")

    def __str__(self):
        return self.__repr__()


timer = Timer
