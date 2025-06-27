import os

from pathlib import Path
from pytest_bdd import scenarios, when, then

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorState
from isym_test_api.rest_api.api.behavior.prime_fluidics.system_prime_fluidics_request import generate_default_prime_fluidics_request
from isym_test_api.rest_api.drivers.system.system_prime_fluidics_driver import PrimeFluidicsDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_system_prime_fluidics_test.feature')


# region When


@when('system prime fluidics test is started')
def system_prime_fluidics(prime_fluidics_rest_api_driver: PrimeFluidicsDriver):
    prime_fluidics_rest_api_driver.prime_fluidics_test_setup(payload=generate_default_prime_fluidics_request())


# endregion When
# region Then


@then('system prime fluidics test completes')
def system_prime_fluidics_status(context, prime_fluidics_rest_api_driver: PrimeFluidicsDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: prime_fluidics_rest_api_driver.get_prime_fluidics_test_status().state,
                             BehaviorState.BehaviorState_INACTIVE,
                             "Unexpected behaviour state", WaitTimeConstants.MidWait, 2)
# endregion Then
