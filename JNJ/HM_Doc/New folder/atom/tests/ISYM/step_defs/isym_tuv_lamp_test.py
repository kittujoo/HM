import os
from datetime import datetime

from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.detection.lamp_history_response import TuvLampHistory
from isym_test_api.rest_api.api.detection.lamp_hours_response import UsageCounter
from isym_test_api.rest_api.api.detection.lamp_intensity_response import TuvLampIntensityTestResult
from isym_test_api.rest_api.api.detection.tuv_lamp_response import LampStateEnum
from isym_test_api.rest_api.drivers.detection.tuv_lamp_driver import TuvLampDriver, LampRequest
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_tuv_lamp_test.feature')


# region Given

@given('the lamp is ON')
def set_lamp_status_on(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    if not tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampOn:
        tuv_lamp_rest_api_driver.set_tuv_lamp_status(payload=LampRequest(lampOn=True))
    assert_timeout.are_equal(lambda: tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampState,
                             LampStateEnum.LampState_READY, "The lamp status did not change to the expected state")


@given('the lamp is OFF')
def set_lamp_status_off(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    if tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampOn:
        tuv_lamp_rest_api_driver.set_tuv_lamp_status(payload=LampRequest(lampOn=False))
    assert_timeout.are_equal(lambda: tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampState,
                             LampStateEnum.LampState_OFF, "The lamp status did not change to the expected state")


# endregion Given


# region When

@when('the tuv lamp history is requested')
def request_tuv_lamp_history(context, tuv_lamp_rest_api_driver: TuvLampDriver):
    context['lamp_history'] = tuv_lamp_rest_api_driver.get_lamp_history()


@when('the lamp is requested to turn ON')
def configure_lamp_on(tuv_lamp_rest_api_driver: TuvLampDriver):
    tuv_lamp_rest_api_driver.set_tuv_lamp_status(payload=LampRequest(lampOn=True))


@when('the lamp is requested to turn OFF')
def configure_lamp_off(tuv_lamp_rest_api_driver: TuvLampDriver):
    tuv_lamp_rest_api_driver.set_tuv_lamp_status(payload=LampRequest(lampOn=False))


@when('the tuv lamp intensity is requested')
def request_tuv_lamp_indensity(context, tuv_lamp_rest_api_driver: TuvLampDriver):
    context['lamp_intensity'] = tuv_lamp_rest_api_driver.get_lamp_intensity()


@when('the tuv lamp hours is requested')
def request_tuv_lamp_hours(context, tuv_lamp_rest_api_driver: TuvLampDriver):
    context['lamp_hours'] = tuv_lamp_rest_api_driver.get_lamp_hours()


@when('the tuv replace lamp is requested')
def request_tuv_replace_lamp(tuv_lamp_rest_api_driver: TuvLampDriver):
    tuv_lamp_rest_api_driver.set_replace_lamp()


@when('the tuv lamp replacement complete confirmation requested')
def request_tuv_replace_lamp_completed(tuv_lamp_rest_api_driver: TuvLampDriver):
    tuv_lamp_rest_api_driver.set_replace_lamp_completed()


# endregion When


# region Then

@then('the tuv lamp replacement complete activity started')
def verify_tuv_replace_lamp_completed_status_started(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: tuv_lamp_rest_api_driver.is_replace_lamp_completed_status_started(),
                           "Tuv replace lamp completed activity start failed.", WaitTimeConstants.SmallWait)


@then('the tuv lamp replacement complete activity completed')
def verify_tuv_replace_lamp_completed_status_completed(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: tuv_lamp_rest_api_driver.is_replace_lamp_completed_status_completed(),
                           "Tuv replace lamp completed activity complete failed.", WaitTimeConstants.MidWait)


@then('the tuv lamp replacement activity started')
def verify_tuv_replace_lamp_status_started(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: tuv_lamp_rest_api_driver.is_replace_lamp_status_started(),
                           "Tuv replace lamp status activity start failed.", WaitTimeConstants.SmallWait, 0.05)


@then('the tuv lamp replacement activity completed')
def verify_tuv_replace_lamp_status_completed(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: tuv_lamp_rest_api_driver.is_replace_lamp_status_complete(),
                           "Tuv replace lamp status activity complete failed.", WaitTimeConstants.MidWait)


@then('the tuv lamp history with serial number, installation date, lamp minutes and ignitions counts is available')
def verify_tuv_lamp_history_info(context):
    response: TuvLampHistory = context['lamp_history'].data
    assert len(response.lamps[0].serialNumber.strip()) > 0, f"Unexpected serialNumber: {response.lamps[0].serialNumber}"
    install_date = type(datetime.strptime(response.lamps[0].installationDate, '%Y-%m-%dT%H:%M:%SZ'))
    assert install_date is datetime, f"Unexpected installationDate: {response.lamps[0].installationDate}"
    assert response.lamps[0].lampMinutes >= 0, f"Unexpected lampMinutes: {response.lamps[0].lampMinutes}"
    assert response.lamps[0].successfulIgnitions >= 0, f"Unexpected successfulIgnitions: {response.lamps[0].successfulIgnitions}"
    assert response.lamps[0].failedIgnitions >= 0, f"Unexpected failedIgnitions: {response.lamps[0].failedIgnitions}"


@then('the tuv lamp intensity with lamp intensity lamp usage is available')
def verify_tuv_lamp_intensity_info(context):
    response: TuvLampIntensityTestResult = context['lamp_intensity'].data
    assert response.lampIntensityPct >= 0.0, f"Unexpected Lamp Intensity Pct: {response.lampIntensityPct}"
    assert response.lampUsageThresholdPerc >= 0.0, f"Unexpected Lamp Usage Threshold: {response.lampUsageThresholdPerc}"


@then('the tuv lamp hours information is available')
def verify_tuv_lamp_hours_info(context):
    response: UsageCounter = context['lamp_hours'].data
    assert len(response.counterName.strip()) > 0, f"Unexpected counterName: {response.counterName}"
    assert response.counterValue.valueInt >= 0, f"Unexpected Lamp hours: {response.counterValue.valueInt}"


@then(cfparse('the state of the lamp changes to "{lamp_state}"'))
def validate_lamp_state(lamp_state, tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampState,
                             getattr(LampStateEnum, lamp_state), "The lamp status did not change to the expected state")


@then('the lamp status is ON')
def validate_lamp_status_ON(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampOn, "The lamp status did not change to the expected state")


@then('the lamp status is OFF')
def validate_lamp_status_OFF(tuv_lamp_rest_api_driver: TuvLampDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_false(lambda: tuv_lamp_rest_api_driver.get_tuv_lamp_status().data.lampOn, "The lamp status did not change to the expected state")

# endregion Then
