from utilities.logger import Logger
from pathlib import Path
from pytest_bdd import scenarios, when, then
from isym_test_api.rest_api.drivers.meta_setting.meta_setting_driver import MetaSettingDriver
from isym_test_api.rest_api.api.meta_setting.meta_setting_request import (generate_prerun_checks_request, generate_run_checks_request,
                                                                          generate_validate_sample_set_on_submit_request)


import os

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_sample_set_validation_test.feature')


@when('configure validation is requested')
def configure_settings(meta_setting_rest_api_driver: MetaSettingDriver):
    meta_setting_rest_api_driver.set_meta_checks(generate_prerun_checks_request())
    meta_setting_rest_api_driver.set_meta_checks(generate_run_checks_request())


@when('the sample set is validated')
def validate_sample_set_on_submit(context, meta_setting_rest_api_driver: MetaSettingDriver):
    context['api_response'] = meta_setting_rest_api_driver.set_validate_sample_set_on_submit(generate_validate_sample_set_on_submit_request())


@then('the correct validation result is received')
def verify_sample_set_data(context):
    response_body = context['api_response'].data
    actual_validation_failure_result = response_body['validationFailure']
    assert actual_validation_failure_result == False, f"Expected validation failure result to be false, but was {actual_validation_failure_result}"
