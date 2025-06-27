import os
from pathlib import Path
from pytest_bdd import scenarios, when

from isym_test_api.rest_api.drivers.system.command.system_command_driver import SystemCommandDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_system_initialize_test.feature')

# region When


@when('the system software initialize is requested')
def request_system_initialize(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_initialize()
# endregion When