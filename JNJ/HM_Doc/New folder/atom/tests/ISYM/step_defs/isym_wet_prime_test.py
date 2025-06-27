import os
from pathlib import Path
from pytest_bdd import scenarios, when

from isym_test_api.rest_api.api.behavior.wet_prime.system_meta_wet_prime_request import generate_default_system_wet_prime_request
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_wet_prime_test.feature')


@when('the wet prime operation is started')
def start_wet_prime_operation(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    data_system_acquisition_rest_api_driver.start_wet_prime(payload=generate_default_system_wet_prime_request())
