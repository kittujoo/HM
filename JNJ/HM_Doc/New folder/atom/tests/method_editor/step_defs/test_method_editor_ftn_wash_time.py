import os

from pytest_bdd import given, when, scenarios, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.method_editor.pages.sample_manager.menu_item_sample_manager import SampleManagerMenu
from web_framework.method_editor.pages.sample_manager.wash_time_page import WashTimePage

scenarios('../features/method_editor_ftn_wash_time.feature')

logger = Logger(os.path.basename(__file__))


@given('the Wash Time menu is open', target_fixture="wash_time_page")
@when('the Wash Time menu is open', target_fixture="wash_time_page")
def open_wash_time_menu(sample_manager_menu: SampleManagerMenu):
    wash_time_page = sample_manager_menu.open_wash_time()
    return wash_time_page


@then(cfparse('the Wash Time menu title is "{expected_title}"'))
def validate_wash_time_title(expected_title, wash_time_page: WashTimePage):
    actual_title = wash_time_page.get_wash_time_title()
    assert actual_title == expected_title, f"The Sample Temperature menu title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the setting group title is "{expected_title}"'))
def validate_group_title(expected_title, wash_time_page: WashTimePage):
    actual_title = wash_time_page.get_settings_group_title()
    assert actual_title == expected_title, f"The setting group title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Wash Time setting title is "{expected_title}"'))
def validate_setting_title(expected_title, wash_time_page: WashTimePage):
    actual_title = wash_time_page.get_wash_time_settings_title()
    assert actual_title == expected_title, f"The Wash Time setting title is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Wash Time setting summary is "{expected_title}"'))
def validate_setting_summary(expected_title, wash_time_page: WashTimePage):
    actual_title = wash_time_page.get_wash_time_settings_summary()
    assert actual_title == expected_title, f"The Wash Time setting summary is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@then(cfparse('the Wash Time setting input hint text is "{expected_title}"'))
def validate_setting_hint(expected_title, wash_time_page: WashTimePage, ):
    actual_title = wash_time_page.get_wash_time_hint()
    assert actual_title == expected_title, f"The Wash Time hint is incorrect. Expected: [{expected_title}], Actual: [{actual_title}]"


@when('the Wash Time setting group is set as Favorite')
def set_wash_time_favorite(wash_time_page: WashTimePage):
    wash_time_page.set_favorite()


@then("the Wash Time setting group is displayed")
def validate_wash_time_setting_group(wash_time_page: WashTimePage):
    assert wash_time_page.is_wash_time_displayed(), "Wash Time is not displayed"


@then(cfparse('the Wash Time input has value set to "{expected_value}"'))
def validate_wash_time_editbox(expected_value, wash_time_page: WashTimePage):
    actual_value = wash_time_page.get_wash_time_editbox_value()
    assert actual_value == expected_value, f"The Wash Time editbox value is incorrect. Expected: [{expected_value}], Actual: [{actual_value}]"


@then(cfparse('the Wash Time summary menu value is "{expected_value}"'))
@then(cfparse('the Wash Time menu summary is rounded to 1 decimal place showing "{expected_value}"'))
def validate_wash_time_menu_summary(expected_value, sample_manager_menu: SampleManagerMenu, ):
    actual_value = sample_manager_menu.get_wash_time_state()
    assert actual_value == expected_value, f"The Wash Time menu summary value is incorrect. Expected: [{expected_value}], Actual: [{actual_value}]"


@when(cfparse('the Wash Time input is set to "{value}"'))
@when(cfparse('the Wash Time input is set to an out of range value "{value}"'))
@given(cfparse('the Wash Time input is set to "{value}"'))
def set_wash_time_input(value, wash_time_page: WashTimePage):
    wash_time_page.set_wash_time_editbox(value)


@then("the Wash Time input is not in error")
def validate_wash_time_not_in_error(wash_time_page: WashTimePage):
    # TODO currently there is no possibility to determine that wash time editbox not in error state
    pass


@then("the Wash Time input is in error")
def validate_wash_time_in_error(wash_time_page: WashTimePage):
    # TODO currently there is no possibility to determine that wash time editbox in error state
    pass


@given('the Wash Time input is in error')
def wash_time_in_error(wash_time_page: WashTimePage):
    wash_time_page.set_wash_time_editbox(130)


@then('the Wash Time input is empty')
def wash_time_input_empty(wash_time_page: WashTimePage):
    actual_value = wash_time_page.get_wash_time_editbox_value()
    assert actual_value == str(0), f"The Wash Time menu summary value is incorrect. Expected: [0], Actual: [{actual_value}]"
