"""
Desc: Step Definition to validate iSym Equilibrate Test Workflow.

"""
from pathlib import Path
from pytest_bdd import scenarios, when
import os

from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from utilities.logger import Logger
from isym_test_api.rest_api.api.system.equilibrate_request import generate_default_equilibrating_request

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_equilibrate_test.feature')


@when('a equilibrating test is started')
def start_equilibrating_test(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    data_system_acquisition_rest_api_driver.start_equilibrate(generate_default_equilibrating_request())
