import abc
import math
import os
import time
from typing import Callable, Union, Optional, Tuple, TypeVar, Type, Generic

from utilities.common_utilities import if_none_get
from utilities.logger import Logger
from utilities.timer import timer
from utilities.types import Int_Or_Float, T

logger = Logger(os.path.basename(__file__))
Exception_T = TypeVar("Exception_T", bound=BaseException)


class Equality(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def test(self, actual: T, expected: T, message: str) -> T:
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Equality"


class Equal(Equality):

    def test(self, actual: T, expected: T, message: str) -> T:
        assert actual == expected, f"{message}. Expected: [{expected}], Actual: [{actual}]"
        return actual

    def __str__(self):
        return "equal"


class NotEqual(Equality):

    def test(self, actual: T, expected: T, message: str) -> T:
        assert actual != expected, f"{message}. Expected: [{expected}], Actual: [{actual}]"
        return actual

    def __str__(self):
        return "not_equal"


class EqualWithTolerance(Equality, Generic[Int_Or_Float]):
    def __init__(self, tolerance: Int_Or_Float):
        self.tolerance = tolerance

    def test(self, actual: Int_Or_Float, expected: Int_Or_Float, message: str):
        assert math.isclose(actual, expected, abs_tol=self.tolerance), f"{message}. Expected: [{expected}], Actual: [{actual}]"
        return actual

    def __str__(self):
        return "equal_within_tolerance"


class EqualNotWithTolerance(Equality, Generic[Int_Or_Float]):
    def __init__(self, tolerance: Int_Or_Float):
        self.tolerance = tolerance

    def test(self, actual: Int_Or_Float, expected: Int_Or_Float, message: str):
        assert not math.isclose(actual, expected, abs_tol=self.tolerance), f"{message}. Expected: [{expected}], Actual: [{actual}]"
        return actual

    def __str__(self):
        return "not_within_tolerance"


class AssertTimeout:

    def __init__(self, timeout: Int_Or_Float, poll: Int_Or_Float):
        self._default_timeout: Int_Or_Float = timeout
        self._default_polling_period: Int_Or_Float = poll

    def _timeout(self, candidate: Optional[Int_Or_Float]):
        return if_none_get(candidate, self._default_timeout)

    def _polling(self, candidate: Optional[Int_Or_Float]):
        return if_none_get(candidate, self._default_polling_period)

    def wait_for_condition(self, expected_condition: Callable[[], bool],
                           timeout_in_seconds: Union[int, float] = None,
                           polling_period_in_seconds: Union[int, float] = None) -> bool:

        tmr = timer(self._timeout(timeout_in_seconds)).start()
        while tmr:
            if expected_condition():
                return True
            time.sleep(self._polling(polling_period_in_seconds))
        logger.debug("Wait condition failed")
        return False

    def _equality(self, actual: Callable[[], T], expected: T, message,
                  operator: Equality,
                  timeout_in_seconds: Union[int, float] = None,
                  polling_period_in_seconds: Union[int, float] = None,
                  ignored_exceptions: Tuple = ()):

        timeout = self._timeout(timeout_in_seconds)

        logger.debug(f"Waiting for callable to be {operator} to {expected} within {timeout} seconds")

        tmr = timer(timeout).start()
        actual_value = None
        while True:
            try:
                actual_value = actual()
                return operator.test(actual_value, expected, message)
            except ignored_exceptions as e:
                logger.debug(f"One of ignored exceptions [{type(e)}] was raised during execution of ['{operator}'] operation")
                last_exception = e
            except AssertionError as e:
                logger.debug(f"Actual value [{actual_value}] not met expected [{expected}]. Time remains [{tmr.remains()}] seconds.")
                last_exception = e
            if not tmr:
                logger.error(f"Given function return value was not met expected [{expected}] after [{timeout}] seconds.")
                raise last_exception from None

            time.sleep(self._polling(polling_period_in_seconds))

    def are_equal(self, actual: Callable[[], T], expected: T, message,
                  timeout_in_seconds: Union[int, float] = None,
                  polling_period_in_seconds: Union[int, float] = None,
                  ignored_exceptions: Tuple = ()):

        return self._equality(actual=actual,
                              expected=expected,
                              message=message,
                              operator=Equal(),
                              timeout_in_seconds=timeout_in_seconds,
                              polling_period_in_seconds=polling_period_in_seconds,
                              ignored_exceptions=ignored_exceptions
                              )

    def are_not_equal(self, actual: Callable[[], T], expected: T, message: str,
                      timeout_in_seconds: Union[int, float] = None,
                      polling_period_in_seconds: Union[int, float] = None,
                      ignored_exceptions: Tuple[Type[Exception_T]] = ()):

        return self._equality(actual=actual,
                              expected=expected,
                              message=message,
                              operator=NotEqual(),
                              timeout_in_seconds=timeout_in_seconds,
                              polling_period_in_seconds=polling_period_in_seconds,
                              ignored_exceptions=ignored_exceptions
                              )

    def is_true(self, actual: Callable[[], bool], message: str,
                timeout_in_seconds: Union[int, float] = None,
                polling_period_in_seconds: Union[int, float] = None,
                ignored_exceptions: Tuple[Type[Exception_T]] = ()):

        self._equality(actual=actual,
                       expected=True,
                       message=message,
                       operator=Equal(),
                       timeout_in_seconds=timeout_in_seconds,
                       polling_period_in_seconds=polling_period_in_seconds,
                       ignored_exceptions=ignored_exceptions
                       )

    def is_false(self, actual: Callable, message: str,
                 timeout_in_seconds: Union[int, float] = None,
                 polling_period_in_seconds: Union[int, float] = None,
                 ignored_exceptions: Tuple[Type[Exception_T]] = ()):

        self._equality(actual=actual,
                       expected=False,
                       message=message,
                       operator=Equal(),
                       timeout_in_seconds=timeout_in_seconds,
                       polling_period_in_seconds=polling_period_in_seconds,
                       ignored_exceptions=ignored_exceptions
                       )

    def wait_no_exception(self, actual: Callable[[], T], message: str, timeout_in_seconds: Union[int, float] = None,
                          polling_period_in_seconds: Union[int, float] = None,
                          ignored_exceptions: Tuple[Type[Exception_T]] = ()) -> T:

        tmr = timer(self._timeout(timeout_in_seconds)).start()
        while True:
            try:
                actual_value = actual()
                return actual_value
            except ignored_exceptions as e:
                logger.debug(f"Exception of type [{type(e)}] was raised during execution of 'wait_no_exception' operation")
            except Exception as e:
                if not tmr:
                    logger.error(f"Wait condition failed: {e}")
                    assert False, message
            time.sleep(self._polling(polling_period_in_seconds))

    def value_is_within_tolerance(self, actual: Callable[[], Int_Or_Float], expected: Int_Or_Float, tolerance: Int_Or_Float,
                                  message: str,
                                  timeout_in_seconds: Union[int, float] = None,
                                  polling_period_in_seconds: Union[int, float] = None,
                                  ignored_exceptions: Tuple[Type[Exception_T]] = ()):

        return self._equality(actual=actual,
                              expected=expected,
                              message=message,
                              operator=EqualWithTolerance(tolerance),
                              timeout_in_seconds=timeout_in_seconds,
                              polling_period_in_seconds=polling_period_in_seconds,
                              ignored_exceptions=ignored_exceptions
                              )

    def value_is_not_within_tolerance(self, actual: Callable, expected: float, tolerance: float,
                                      message: str,
                                      timeout_in_seconds: Union[int, float] = None,
                                      polling_period_in_seconds: Union[int, float] = None,
                                      ignored_exceptions: Tuple[Type[Exception_T]] = ()):

        return self._equality(actual=actual,
                              expected=expected,
                              message=message,
                              operator=EqualNotWithTolerance(tolerance),
                              timeout_in_seconds=timeout_in_seconds,
                              polling_period_in_seconds=polling_period_in_seconds,
                              ignored_exceptions=ignored_exceptions
                              )

    def value_remains_same(self, actual: Callable[[], T], expected: T,
                           message: str,
                           timeout_in_seconds: Union[int, float] = None,
                           polling_period_in_seconds: Union[int, float] = None,
                           ignored_exceptions: Tuple[Type[Exception_T]] = ()):

        logger.debug(f"Waiting for callable to be equal to {expected} for next {timeout_in_seconds} seconds")
        timeout = self._timeout(timeout_in_seconds)
        tmr = timer(timeout).start()
        while tmr:
            actual_value = actual()
            try:
                assert actual_value == expected, f"{message}. Expected: [{expected}], Actual: [{actual}]"
            except ignored_exceptions as e:
                logger.debug(f"Exception of type [{type(e)}] was raised during execution of 'value_remains_same' operation")
            time.sleep(self._polling(polling_period_in_seconds))
