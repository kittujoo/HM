import os
import re

from pathlib import Path
from pytest_bdd import scenarios, when, then

from isym_test_api.rest_api.drivers.system.system_state_driver import SystemStateDriver
from isym_test_api.rest_api.api.system.about_response import (AboutResponse, DeviceModelEnum, DeviceVariantEnum, DeviceFamilyEnum)
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_about_validation.feature')


@when('the about information is requested')
def get_about_details(context, system_state_rest_api_driver: SystemStateDriver):
    context['api_response']: AboutResponse = system_state_rest_api_driver.get_about_info().data


@then('the about information is available')
def validate_details(context):
    response = context['api_response']
    assert response.hardware.productModel == DeviceModelEnum.ProductModel_ALLIANCEIS, f"Unexpected productModel: {response.hardware.productModel}"
    assert response.hardware.productVariant in [DeviceVariantEnum.ProductVariant_TUV, DeviceVariantEnum.ProductVariant_PDA], \
        f"Unexpected productVariant: {response.hardware.productVariant} "
    assert isinstance(response.hardware.productFamily,
                      DeviceFamilyEnum) and response.hardware.productFamily == DeviceFamilyEnum.ProductFamily_UNKNOWN, f"Unexpected productFamily: {response.hardware.productFamily}"
    assert response.hardware.serial, f"Unexpected serial: {response.hardware.serial}"
    assert re.match(r"^[A-Za-z0-9_]+\.[0-9]+\.[A-Za-z0-9-_.]+$", response.software.version), f"Unexpected version: {response.software.version}"
    assert response.support.companyName == "Waters Corporation", f"Unexpected companyName: {response.support.companyName}"
    assert response.support.companyAddress1, "support.companyAddress1 is empty"
    assert response.support.companyAddress2, "support.companyAddress2 is empty"
    assert response.support.companyAddress3, "support.companyAddress3 is empty"
    assert response.support.supportUrl, "support.supportUrl is empty"
    assert response.eula[0].language in ['en-US', 'ja', 'zh-CHS'], f"Unexpected language: {response.eula[0].language}"
    assert response.eula[0].content, "eula[0].content is empty"
    assert response.terms[0].language in ['en-US', 'ja', 'zh-CHS'], f"Unexpected Terms language: {response.terms[0].language}"
    assert response.terms[0].content, "terms[0].content is empty"
    assert response.hardware.productVersion, "hardware.productVersion is empty"
    assert response.software.buildDate, "hardware.buildDate is empty"
