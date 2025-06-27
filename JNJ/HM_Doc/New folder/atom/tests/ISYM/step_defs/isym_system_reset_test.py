import os

from pathlib import Path
from pytest_bdd import scenarios, when

from isym_test_api.rest_api.api.system.system_reset_request import generate_stopping_activity_system_reset_request, \
    generate_only_initialize_system_reset_request
from isym_test_api.rest_api.drivers.system.command.system_command_driver import SystemCommandDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_system_reset_test.feature')

# region When


@when('stopping activities is requested with system reset')
def request_system_soft_reset_stop_activity(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_reset_request(generate_stopping_activity_system_reset_request())


@when('only initialized is requested with system reset')
def request_system_soft_reset_initialize(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_reset_request(generate_only_initialize_system_reset_request())

# endregion When
