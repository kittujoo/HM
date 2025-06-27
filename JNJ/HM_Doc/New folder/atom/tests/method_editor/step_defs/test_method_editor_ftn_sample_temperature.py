import os

from pathlib import Path
from pytest_bdd import given, when, scenarios, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.method_editor.pages.method_editor_main_page import MethodEditorMainPage
from web_framework.method_editor.pages.sample_manager.menu_item_sample_manager import SampleManagerMenu
from web_framework.method_editor.pages.sample_manager.sample_temperature_page import SampleTemperaturePage

if __name__ == Path(__file__).stem:
    scenarios('../features/method_editor_ftn_sample_temperature.feature')

logger = Logger(os.path.basename(__file__))


@given('the Sample Temperature menu is opened', target_fixture="sample_temperature_page")
def open_sample_temperature_menu(sample_manager_menu: SampleManagerMenu):
    sample_temperature_page = sample_manager_menu.open_sample_temperature()
    return sample_temperature_page


@given(cfparse('the Compartment Temperature selector is set to "{toggle_state:bool}"', CONVERTERS))
@when(cfparse('the Compartment Temperature selector is set to "{toggle_state:bool}"', CONVERTERS))
def set_compartment_toggle(toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_compartment_toggle(toggle_state)


@when(cfparse('the Temperature Setpoint input is set to "{value:f}"'))
@when(cfparse('the Temperature Setpoint input is set to out of range value "{value:f}"'))
def set_temperature_setpoint(value: float, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_temperature_setpoint(value)


@then("the Temperature Setpoint input is not in error")
def validate_setpoint_not_in_error(sample_temperature_page: SampleTemperaturePage):
    # TODO currently there is no possibility to determine that setpoint editbox in error state
    pass


@then("the Temperature Setpoint input is in error")
def validate_setpoint_in_error(sample_temperature_page: SampleTemperaturePage):
    # TODO currently there is no possibility to determine that setpoint editbox in error state
    pass


@then(cfparse('the Sample Temperature menu title is "{expected_title}"'))
def validate_sample_temperature_title(expected_title, sample_temperature_page: SampleTemperaturePage):
    actual_title = sample_temperature_page.get_sample_temperature_title()
    assert actual_title == expected_title, f"The Sample Temperature menu title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the setting group title text is "{expected_title}"'))
def validate_group_title(expected_title, sample_temperature_page: SampleTemperaturePage):
    actual_title = sample_temperature_page.get_settings_group_title()
    assert actual_title == expected_title, f"The setting group title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Compartment Temperature setting title is "{expected_title}"'))
def validate_setting_title(expected_title, sample_temperature_page: SampleTemperaturePage):
    actual_title = sample_temperature_page.get_set_temperature_title()
    assert actual_title == expected_title, f"The Compartment Temperature setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Compartment Temperature setting summary is "{expected_subtitle}"'))
def validate_subtitle(expected_subtitle, sample_temperature_page: SampleTemperaturePage):
    actual_subtitle = sample_temperature_page.get_compartment_temperature_subtitle()
    assert actual_subtitle == expected_subtitle, \
        f"The Compartment Temperature setting summary is incorrect. Expected: [{expected_subtitle}], Actual: [{actual_subtitle}]"


@then(cfparse('the Temperature Setpoint setting title is "{expected_title}"'))
def validate_setpoint_setting_title(expected_title, sample_temperature_page: SampleTemperaturePage):
    actual_title = sample_temperature_page.get_setpoint_setting_title()
    assert actual_title == expected_title, f"The Temperature Setpoint setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Temperature Setpoint setting input hint text is "{expected_text}"'))
def validate_setpoint_hint_text(expected_text, sample_temperature_page: SampleTemperaturePage):
    actual_text = sample_temperature_page.get_setpoint_hint_message()
    assert actual_text == expected_text, f"The Temperature Setpoint setting input hint text is incorrect. Expected: [{expected_text}], Actual: [{actual_text}]"


@then(cfparse('the Temperature Tolerance setting title is "{expected_title}"'))
def validate_tolerance_setting_title(expected_title, sample_temperature_page: SampleTemperaturePage):
    actual_title = sample_temperature_page.get_tolerance_settings_title()
    assert actual_title == expected_title, f"The Temperature Tolerance setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Temperature Tolerance setting summary is "{expected_subtitle}"'))
def validate_tolerance_setting_subtitle(expected_subtitle: str, sample_temperature_page: SampleTemperaturePage):
    actual_subtitle = sample_temperature_page.get_tolerance_setting_subtitle()
    assert actual_subtitle == expected_subtitle, \
        f"The Temperature Tolerance setting subtitle is incorrect. Expected: [{expected_subtitle}], Actual: [{actual_subtitle}]"


@when('the Sample Temperature setting group is set as Favorite')
def set_sample_temperature_favorite(sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_favorite()


@then(cfparse('the Temperature Tolerance selector is set to "{toggle_state:bool}"', CONVERTERS))
def check_tolerance_toggle(toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.validate_temperature_tolerance_toggle_state(toggle_state)


@then(cfparse('the Compartment Temperature selector is set to "{toggle_state:bool}"', CONVERTERS))
def check_sample_compartment_toggle(toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.validate_compartment_temperature_toggle_state(toggle_state)


@then(cfparse('the Temperature Setpoint input has value set to default "{setpoint_temperature_value:d}"'))
@then(cfparse('the Temperature Setpoint input has value set to "{setpoint_temperature_value:d}"'))
def validate_setpoint_temperature(setpoint_temperature_value: int, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.validate_setpoint_temperature(setpoint_temperature_value)


@when(cfparse('the Set Temperature Tolerance selector is set to "{toggle_state:bool}"', CONVERTERS))
def set_tolerance_toggle(toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_tolerance_toggle(toggle_state)


@then(cfparse('the Tolerance input has value set to default "{tolerance_temperature_value:d}"'))
@then(cfparse('the Tolerance input has value set to "{tolerance_temperature_value:d}"'))
def validate_tolerance_temperature(tolerance_temperature_value: int, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.validate_tolerance_temperature(tolerance_temperature_value)


@then(cfparse('the Sample Temperature menu summary is "{expected_subtitle}"'))
def validate_subtitle(expected_subtitle, sample_temperature_page: SampleTemperaturePage):
    actual_subtitle = sample_temperature_page.get_sample_temperature_subtitle()
    assert actual_subtitle == expected_subtitle, \
        f"The Sample Temperature menu subtitle is incorrect. Expected: [{expected_subtitle}], Actual: [{actual_subtitle}]"


@then(cfparse('the Tolerance setting title is "{expected_title}"'))
def validate_subtitle(expected_title, sample_temperature_page: SampleTemperaturePage):
    actual_title = sample_temperature_page.get_tolerance_input_title()
    assert actual_title == expected_title, f"The Tolerance setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Tolerance setting input hint text is "{expected_hint_text}"'))
def validate_hint_text(expected_hint_text, sample_temperature_page: SampleTemperaturePage):
    actual_hint_text = sample_temperature_page.get_tolerance_hint_text()
    assert actual_hint_text == expected_hint_text, f"Tolerance input hint text is incorrect. Expected: [{expected_hint_text}], Actual: [{actual_hint_text}]"


@given(cfparse('the Temperature Tolerance selector is set to "{toggle_state:bool}"', CONVERTERS))
@when(cfparse('the Temperature Tolerance selector is set to "{toggle_state:bool}"', CONVERTERS))
def set_tolerance_toggle(toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_tolerance_toggle(toggle_state)


@when(cfparse('the Tolerance input is set to out of range value "{value:f}"'))
@when(cfparse('the Tolerance input is set to "{value:f}"'))
def set_temperature_tolerance(value: float, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_tolerance(value)


@given(cfparse('the Temperature Setpoint input is in error'))
@when(cfparse('the Temperature Setpoint input is in error'))
def set_temperature_setpoint(sample_temperature_page: SampleTemperaturePage):
    temperature_out_of_range_value = 40.1
    sample_temperature_page.set_temperature_setpoint(temperature_out_of_range_value)


@given(cfparse('the Tolerance input is in error'))
@when(cfparse('the Tolerance input is in error'))
def set_temperature_tolerance(sample_temperature_page: SampleTemperaturePage):
    tolerance_out_of_range_value = 10.1
    sample_temperature_page.set_tolerance(tolerance_out_of_range_value)


@when(cfparse('the Compartment Temperature selector is set to "{initial_toggle_state:bool}" and back to "{final_toggle_state:bool}"', CONVERTERS))
def set_compartment_toggle(initial_toggle_state: bool, final_toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_compartment_toggle(initial_toggle_state)
    sample_temperature_page.set_compartment_toggle(final_toggle_state)


@when(cfparse('the Temperature Tolerance selector is set to "{initial_toggle_state:bool}" and back to "{final_toggle_state:bool}"', CONVERTERS))
def set_tolerance_toggle(initial_toggle_state: bool, final_toggle_state: bool, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_tolerance_toggle(initial_toggle_state)
    sample_temperature_page.set_tolerance_toggle(final_toggle_state)


@when(cfparse('the Temperature Setpoint input is set to valid value "{value:d}"'))
def set_temperature_setpoint(value: int, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_temperature_setpoint(value)


@when(cfparse('the Tolerance input is set to valid value "{value:d}"'))
def set_temperature_tolerance(value: int, sample_temperature_page: SampleTemperaturePage):
    sample_temperature_page.set_tolerance(value)


@then("the Tolerance input is in error")
def validate_setpoint_in_error(sample_temperature_page: SampleTemperaturePage):
    # TODO currently there is no possibility to determine that setpoint editbox in error state
    pass


@then("the Tolerance input is in error")
def validate_setpoint_in_error(sample_temperature_page: SampleTemperaturePage):
    # TODO currently there is no possibility to determine that setpoint editbox in error state
    pass


@then("the Tolerance input is not in error")
def validate_setpoint_in_error(sample_temperature_page: SampleTemperaturePage):
    # TODO currently there is no possibility to determine that setpoint editbox in error state
    pass

@then("the Temperature Setpoint input is still in error")
@then("the Temperature Setpoint input is in error")
def validate_setpoint_in_error(sample_temperature_page: SampleTemperaturePage):
    # TODO currently there is no possibility to determine that setpoint editbox in error state
    pass


@when(cfparse('the "{issue_title}" issues indicator is selected'))
def select_issue_indicator(issue_title, method_editor_main_page: MethodEditorMainPage):
    method_editor_main_page.select_issue(issue_title)


@then('the Sample Temperature setting group is displayed')
def validate_sample_temperature_setting(sample_temperature_page: SampleTemperaturePage):
    assert sample_temperature_page.is_sample_temperature_displayed()
