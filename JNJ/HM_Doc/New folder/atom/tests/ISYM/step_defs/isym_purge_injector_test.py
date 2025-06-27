import os
from pathlib import Path
from pytest_bdd import scenarios, when, then

from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from isym_test_api.rest_api.api.behavior.system_meta_method_request import generate_default_system_meta_method_request
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_purge_injector_test.feature')


@when('purge injector operation is started')
def start_purge_injector(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    data_system_acquisition_rest_api_driver.start_purge_injector(payload=generate_default_system_meta_method_request())
