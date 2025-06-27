import pytest

from isym_test_api.rest_api.asserts.assert_system_state import AssertSystemState
from utilities.assert_timeout import AssertTimeout


# object sharing context example for Driver/Assert model


@pytest.fixture(scope='session')
def assert_system_state(system_state_rest_api_driver, assert_timeout: AssertTimeout):
    return AssertSystemState(system_state_rest_api_driver, assert_timeout)
