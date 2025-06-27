from pathlib import Path
from pytest_bdd import when, scenarios
import os

from isym_test_api.rest_api.api.system.wash_needle_request import generate_default_system_wash_needle
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_wash_needle_test.feature')


@when('the Wash Needle operation is requested to perform')
def request_to_wash_needle(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    data_system_acquisition_rest_api_driver.start_wash_needle(payload=generate_default_system_wash_needle())
