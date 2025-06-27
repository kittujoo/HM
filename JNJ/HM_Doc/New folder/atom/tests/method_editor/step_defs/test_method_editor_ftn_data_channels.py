import os

from pathlib import Path
from pytest_bdd import given, when, scenarios, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.method_editor.pages.sample_manager.data_channels_page import DataChannelsSampleManagerPage
from web_framework.method_editor.pages.sample_manager.menu_item_sample_manager import SampleManagerMenu

if __name__ == Path(__file__).stem:
    scenarios('../features/method_editor_ftn_data_channels.feature')

logger = Logger(os.path.basename(__file__))


@when('the Data Channels: Sample Manager menu is opened', target_fixture="data_channels_page")
@given('the Data Channels: Sample Manager menu is opened', target_fixture="data_channels_page")
def start_and_login_to_method_creation(sample_manager_menu: SampleManagerMenu):
    data_channels_page = sample_manager_menu.open_data_channels_sample_manager()
    return data_channels_page


@then(cfparse('the Data Channels: Sample Manager menu title is "{expected_title}"'))
def validate_data_channels_title(expected_title, data_channels_page: DataChannelsSampleManagerPage):
    actual_title = data_channels_page.get_data_channels_title()
    assert actual_title == expected_title, f"The Data Channels Sample Manager menu title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Sample Temperature setting has title "{expected_title}" and description "{expected_subtitle}"'))
def validate_sample_temperature_title(expected_title, expected_subtitle, data_channels_page: DataChannelsSampleManagerPage):
    actual_title = data_channels_page.get_temperature_title()
    actual_subtitle = data_channels_page.get_temperature_subtitle()
    assert actual_title == expected_title, f"The Sample Temperature setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]."
    assert actual_subtitle == expected_subtitle, f"The Sample Temperature subtitle is incorrect. Expected: [{expected_subtitle}], Actual: [{actual_subtitle}]."


@then(cfparse('the Sample Pressure setting has title "{expected_title}" and description "{expected_subtitle}"'))
def validate_sample_pressure_title(data_channels_page: DataChannelsSampleManagerPage, expected_title, expected_subtitle):
    actual_title = data_channels_page.get_pressure_title()
    actual_subtitle = data_channels_page.get_pressure_subtitle()
    assert actual_title == expected_title, f"The Sample Pressure setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]."
    assert actual_subtitle == expected_subtitle, f"The Sample Pressure subtitle is incorrect. Expected: [{expected_subtitle}], Actual: [{actual_subtitle}]."


@given(cfparse('the Sample Temperature selector is turned "{toggle_state:bool}"', CONVERTERS))
def open_method_editor_data_channels_sample_temperature_setting(toggle_state: bool, data_channels_page: DataChannelsSampleManagerPage):
    data_channels_page.set_temperature_toggle(toggle_state)


@given(cfparse('the Sample Pressure selector is turned "{toggle_state:bool}"', CONVERTERS))
def open_method_editor_data_channels_sample_temperature_setting(toggle_state: bool, data_channels_page: DataChannelsSampleManagerPage):
    data_channels_page.set_pressure_toggle(toggle_state)


@then(cfparse('the Sample Temperature selector is set to "{toggle_state:bool}"', CONVERTERS))
def open_method_editor_data_channels_sample_temperature_setting(toggle_state: bool, data_channels_page: DataChannelsSampleManagerPage):
    actual_state = data_channels_page.get_temperature_toggle()
    assert actual_state == toggle_state, f"Default Sample Temperature toggle state is incorrect. Expected: [{toggle_state}], Actual: [{actual_state}]."


@then(cfparse('the Sample Pressure selector is set to "{toggle_state:bool}"', CONVERTERS))
def open_method_editor_data_channels_sample_pressure_setting(toggle_state: bool, data_channels_page: DataChannelsSampleManagerPage):
    actual_toggle_state = data_channels_page.get_pressure_toggle()
    assert actual_toggle_state == toggle_state, f"The Sample Pressure toggle state is incorrect. Expected: [{toggle_state}], Actual: [{actual_toggle_state}]."


@when('the Data Channels: Sample Manager setting group is set as Favorite')
def set_data_channels_favorite(data_channels_page: DataChannelsSampleManagerPage):
    data_channels_page.set_favorite()


@then("the Data Channels: Sample Manager setting group is displayed")
def validate_data_channels_setting_group(sample_manager_menu: SampleManagerMenu):
    assert sample_manager_menu.is_data_channels_sample_manager_displayed(), "Data Channels: Sample Manager is not displayed"
