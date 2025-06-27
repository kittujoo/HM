import math
import os
from threading import Timer
from typing import Any

import pytest

from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from utilities.timer import timer

logger = Logger(os.path.basename(__file__))

value = None
failure_message = "failure message"


def change_value(new_value):
    global value
    value = new_value


def get_value() -> Any:
    return value


def raiser(to_compare: str):
    global value
    if value != to_compare:
        raise ValueError("")


def test_when_are_equal_values_are_equal_should_pass(assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: "value", "value", failure_message, timeout_in_seconds=1)


def test_when_are_equal_values_are_not_equal_should_fail(assert_timeout: AssertTimeout):
    timeout = 5
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.are_equal(lambda: "value 1", "value 2", failure_message, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"are_equal failed with no respect to timeout equal to {timeout}"


def test_when_are_equal_values_are_equal_with_timeout_should_pass(assert_timeout: AssertTimeout):
    global value
    value = "value"
    timeout = 5
    tmr = timer(timeout).start()
    Timer(timeout, change_value, args=["new value"]).start()
    assert_timeout.are_equal(get_value, "new value", failure_message, timeout_in_seconds=10)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"are_equal failed with no respect to timeout equal to {timeout}"


def test_when_are_equal_values_are_not_equal_with_timeout_should_fail(assert_timeout: AssertTimeout):
    global value
    value = "value"
    timeout = 5
    Timer(6, change_value, args=["new value"]).start()
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.are_equal(get_value, "new value", failure_message, timeout_in_seconds=timeout)
    assert tmr.remains() == 0, f"are_equal failed with no respect to timeout equal to {timeout}"


def test_when_are_not_equal_values_are_not_equal_should_pass(assert_timeout: AssertTimeout):
    assert_timeout.are_not_equal(lambda: "value 1", "value 2", failure_message, timeout_in_seconds=1)


def test_when_are_not_equal_values_are_equal_should_fail(assert_timeout: AssertTimeout):
    with pytest.raises(AssertionError):
        assert_timeout.are_not_equal(lambda: "value", "value", failure_message, timeout_in_seconds=1)


def test_when_is_true_value_is_true_should_pass(assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: True, failure_message, timeout_in_seconds=1)


def test_when_is_true_value_is_false_should_fail(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.is_true(lambda: False, failure_message, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"is_true failed with no respect to timeout equal to {timeout}"


def test_when_is_true_value_true_with_timeout_should_pass(assert_timeout: AssertTimeout):
    global value
    value = False
    timeout = 5
    Timer(timeout, change_value, args=[True]).start()
    tmr = timer(timeout).start()
    assert_timeout.is_true(get_value, failure_message, timeout_in_seconds=6)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"is_true failed with no respect to timeout equal to {timeout}"


def test_when_is_true_value_false_with_poll_period_should_pass(assert_timeout: AssertTimeout):
    i = 0
    timeout = 3
    poll = 0.5

    def counter():
        nonlocal i
        i += 1
        return False

    with pytest.raises(AssertionError):
        assert_timeout.is_true(counter, failure_message, timeout_in_seconds=timeout, polling_period_in_seconds=poll)
    assert math.isclose(i, timeout / poll, abs_tol=1), f"is_true failed with no respect to poll period equal to {poll}"


def test_when_is_false_value_is_false_should_pass(assert_timeout: AssertTimeout):
    assert_timeout.is_false(lambda: False, failure_message, timeout_in_seconds=1)


def test_when_is_false_value_is_true_should_fail(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.is_false(lambda: True, failure_message, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"is_false failed with no respect to timeout equal to {timeout}"


def test_when_is_false_value_false_with_timeout_should_pass(assert_timeout: AssertTimeout):
    global value
    value = True
    timeout = 5
    Timer(timeout, change_value, args=[False]).start()
    tmr = timer(timeout).start()
    assert_timeout.is_false(get_value, failure_message, timeout_in_seconds=6)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"is_false failed with no respect to timeout equal to {timeout}"


def test_when_is_false_value_false_with_poll_period_should_pass(assert_timeout: AssertTimeout):
    i = 0
    timeout = 3
    poll = 0.5

    def counter():
        nonlocal i
        i += 1
        return True

    with pytest.raises(AssertionError):
        assert_timeout.is_false(counter, failure_message, timeout_in_seconds=timeout, polling_period_in_seconds=poll)
    assert math.isclose(i, timeout / poll, abs_tol=1), f"is_false failed with no respect to poll period equal to {poll}"


def test_when_value_is_within_tolerance(assert_timeout: AssertTimeout):
    assert_timeout.value_is_within_tolerance(lambda: 0.25, expected=0, tolerance=0.5, message="Test message",
                                             timeout_in_seconds=1)


def test_when_value_is_within_tolerance_should_fail(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.value_is_within_tolerance(lambda: 0.55, 0, 0.5, message="Test message", timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"is_within_tolerance failed with no respect to timeout equal to {timeout}"


def test_when_is_within_tolerance_value_true_with_timeout_should_pass(assert_timeout: AssertTimeout):
    global value
    value = 0
    timeout = 5
    Timer(timeout, change_value, args=[0.55]).start()
    tmr = timer(timeout).start()
    assert_timeout.value_is_within_tolerance(get_value, 0.55, 0.5, message="Test message", timeout_in_seconds=6)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"value_is_within_tolerance failed with no respect to timeout equal to {timeout}"


def test_when_is_within_tolerance_value_true_with_poll_should_pass(assert_timeout: AssertTimeout):
    i = 0
    poll = 0.5

    def counter():
        nonlocal i
        i += 1
        return i

    expected_increase_of_i = 6
    expected_execution_time = expected_increase_of_i * poll
    tmr = timer(10).start()
    assert_timeout.value_is_within_tolerance(counter, expected_increase_of_i, tolerance=0, timeout_in_seconds=10, polling_period_in_seconds=poll,
                                             message=failure_message)
    assert math.isclose(10 - tmr.remains(), expected_execution_time,
                        abs_tol=0.5), f"value_is_within_tolerance failed with no respect to pol period equals to {poll}"


def test_wait_for_condition_should_return_true(assert_timeout: AssertTimeout):
    assert assert_timeout.wait_for_condition(lambda: True, timeout_in_seconds=1)


def test_wait_for_condition_should_return_false(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    assert not assert_timeout.wait_for_condition(lambda: False, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"for_condition failed with no respect to timeout equal to {timeout}"


def test_when_wait_for_condition_value_true_with_timeout_should_pass(assert_timeout: AssertTimeout):
    global value
    value = False
    timeout = 3
    Timer(timeout, change_value, args=[True]).start()
    tmr = timer(timeout).start()
    assert_timeout.wait_for_condition(get_value, timeout_in_seconds=4)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"is_false failed with no respect to timeout equal to {timeout}"


def test_wait_no_exception_should_pass(assert_timeout: AssertTimeout):
    timeout = 3
    assert_timeout.wait_no_exception(lambda: True, message=failure_message, timeout_in_seconds=timeout)


def test_wait_no_exception_lambda_throws_should_fail(assert_timeout: AssertTimeout):
    timeout = 3
    global value
    value = "match"

    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.wait_no_exception(lambda: raiser("unmatch"), message=failure_message, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"wait_no_exception failed with no respect to timeout equal to {timeout}"


def test_wait_no_exception_with_timeout_should_pass(assert_timeout: AssertTimeout):
    timeout = 5

    global value
    value = "unmatch"

    tmr = timer(timeout).start()
    Timer(timeout - 0.2, change_value, args=["match"]).start()
    assert_timeout.wait_no_exception(lambda: raiser("match"), message=failure_message, timeout_in_seconds=timeout, polling_period_in_seconds=0.2)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"wait_no_exception failed with no respect to timeout equal to {timeout}"


def test_wait_no_exception_with_poll_should_pass(assert_timeout: AssertTimeout):
    poll = 0.5
    i = 0
    expected_value_of_i = 6
    expected_execution_time = expected_value_of_i * poll

    def counter():
        nonlocal i
        nonlocal expected_value_of_i
        i += 1
        if i != expected_value_of_i:
            raise ValueError("")

    tmr = timer(10).start()
    assert_timeout.wait_no_exception(counter, message=failure_message, timeout_in_seconds=10, polling_period_in_seconds=poll)
    assert math.isclose(10 - tmr.remains(), expected_execution_time, abs_tol=0.5), f"wait_no_exception failed with no respect to poll period equal to {poll}"


def test_when_value_is_not_within_tolerance(assert_timeout: AssertTimeout):
    assert_timeout.value_is_not_within_tolerance(lambda: 0.501, expected=0, tolerance=0.5, message="Test message",
                                                 timeout_in_seconds=1)


def test_when_value_is_not_within_tolerance_should_fail(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.value_is_not_within_tolerance(lambda: 0.499, 0, 0.5, message="Test message", timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"value_is_not_within_tolerance failed with no respect to timeout equal to {timeout}"


def test_when_is_not_within_tolerance_value_true_with_timeout_should_pass(assert_timeout: AssertTimeout):
    global value
    value = 0.499
    timeout = 5
    Timer(timeout, change_value, args=[0.501]).start()
    tmr = timer(timeout).start()
    assert_timeout.value_is_not_within_tolerance(get_value, 0, 0.5, message="Test message", timeout_in_seconds=6)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"value_is_not_within_tolerance failed with no respect to timeout equal to {timeout}"


def test_when_is_not_within_tolerance_value_true_with_poll_should_pass(assert_timeout: AssertTimeout):
    i = 1
    poll = 0.5

    def counter():
        nonlocal i
        i -= 0.1
        return i

    expected_execution_time = 3
    tmr = timer(10).start()
    assert_timeout.value_is_not_within_tolerance(counter, 1, tolerance=0.6, timeout_in_seconds=10, polling_period_in_seconds=poll,
                                                 message=failure_message)
    assert math.isclose(10 - tmr.remains(), expected_execution_time,
                        abs_tol=0.5), f"value_is_not_within_tolerance failed with no respect to pol period equals to {poll}"


# add poll period test
# value_remains_same


def test_value_remains_same_should_pass(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    assert_timeout.value_remains_same(lambda: True, True, failure_message, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"value_remains_same failed with no respect to timeout equal to {timeout}"


def test_value_remains_same_value_is_not_equal_should_fail(assert_timeout: AssertTimeout):
    timeout = 3
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.value_remains_same(lambda: True, False, failure_message, timeout_in_seconds=timeout)
    assert math.isclose(tmr.remains(), timeout, abs_tol=0.2), f"value_remains_same failed with no respect to timeout equal to {timeout}"


def test_value_remains_same_value_is_not_equal_with_timeout_should_fail(assert_timeout: AssertTimeout):
    global value
    value = True
    timeout = 3
    Timer(timeout, change_value, args=[False]).start()
    tmr = timer(timeout).start()
    with pytest.raises(AssertionError):
        assert_timeout.value_remains_same(get_value, True, failure_message, timeout_in_seconds=timeout + 1)
    assert math.isclose(tmr.remains(), 0, abs_tol=0.2), f"value_remains_same failed with no respect to timeout equal to {timeout}"


def test_value_remains_same_value_is_not_equal_with_poll_should_fail(assert_timeout: AssertTimeout):
    i = 0
    poll = 0.5
    expected_value_of_i = 6

    def counter():
        nonlocal i
        i += 1
        if expected_value_of_i != i:
            return True
        return False

    expected_execution_time = 2.5
    tmr = timer(10).start()
    with pytest.raises(AssertionError):
        assert_timeout.value_remains_same(counter, True, message=failure_message, timeout_in_seconds=10, polling_period_in_seconds=poll)
    assert math.isclose(10 - tmr.remains(), expected_execution_time,
                        abs_tol=0.3), f"value_is_not_within_tolerance failed with no respect to pol period equals to {poll}"
