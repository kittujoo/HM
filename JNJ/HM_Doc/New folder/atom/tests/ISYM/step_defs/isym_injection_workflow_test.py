import os

from pathlib import Path
from pytest_bdd import scenarios, when, then

from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from isym_test_api.rest_api.api.behavior.channel_configuration_response import ChannelConfigurationResponse
from isym_test_api.rest_api.api.behavior.system_inject_request import generate_default_system_injection
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_injection_workflow_test.feature')


# region When

@when('injection activity is started')
def request_start_injection(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    data_system_acquisition_rest_api_driver.start_injection(payload=generate_default_system_injection())


@when('the acquisition channels are requested')
def request_acquisition_channels(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    context['acquisition_channels'] = data_system_acquisition_rest_api_driver.get_data_channels_status()


# endregion When

# region Then


@then('the acquisition channels information is returned')
def verify_instrument_data_channels_information(context):
    received_data: ChannelConfigurationResponse = context['acquisition_channels']
    assert received_data.channels, "Expected one enabled Tuv channel. No enabled channels received."


@then('the expected acquisition channel type is returned')
def verify_instrument_data_channel_name(context):
    received_data: ChannelConfigurationResponse = context['acquisition_channels']
    device_type_list = [x.channelDescriptor.deviceType.lower() for x in received_data.channels]
    assert all(x == "tuv" for x in device_type_list), f"Expected one enabled Tuv channel. Current enabled channels: {device_type_list}"
# endregion Then
