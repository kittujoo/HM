import os

from pathlib import Path
from pytest_bdd import scenarios, then, when

from isym_test_api.rest_api.drivers.system.ambient_temperature_driver import AmbientTemperatureDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_ambient_temperature_test.feature')


@when('the system ambient temperature is requested')
def get_ambient_temperature_test(context, ambient_temperature_rest_api_driver: AmbientTemperatureDriver):
    context['api_response'] = ambient_temperature_rest_api_driver.get_ambient_temperature()


@then('the current ambient temperature in Celsius degrees is returned')
def verify_ambient_temperature_test_results(context):
    assert context['api_response'].data.currentAmbientTemperatureDegC != 0.0, "Ambient Temperature value is not retrieved"
