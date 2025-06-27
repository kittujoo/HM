from pathlib import Path
from pytest_bdd import when, scenarios
import os


from isym_test_api.rest_api.api.system.monitor_baseline_request import generate_default_system_monitor_baseline
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_monitor_baseline_test.feature')


@when('the monitor baseline operation is started')
def request_monitor_baseline_operation(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    data_system_acquisition_rest_api_driver.start_monitor_baseline(payload=generate_default_system_monitor_baseline())
