import os

from argument_constants import METHOD_NAME
from pytest_bdd import given, then, when
from pytest_bdd.parsers import cfparse
from utilities.empower_utility import EmpowerConfiguration
from utilities.logger import Logger
from web_framework.empower.drivers.instrument_method_editor_driver import InstrumentMethodEditorDriver
from web_framework.method_editor.pages.method_editor_main_page import MethodEditorMainPage
from web_framework.method_editor.pages.favorites.menu_item_favorites import FavoritesMenu

logger = Logger(os.path.basename(__file__))


@given('an acquisition method that contains default settings is open', target_fixture="method_editor_main_page")
def start_and_login_to_method_creation(instrument_method_editor_driver: InstrumentMethodEditorDriver, empower_configuration: EmpowerConfiguration):
    project_name = "Defaults"
    method_editor_main_page = instrument_method_editor_driver.login_to_project(project_name,
                                                                               empower_configuration.username,
                                                                               empower_configuration.password,
                                                                               empower_configuration.empower_system_name)
    return method_editor_main_page


@given('the Sample Manager menu is opened', target_fixture="sample_manager_menu")
@when('the Sample Manager menu is opened', target_fixture="sample_manager_menu")
def open_sample_manager(method_editor_main_page: MethodEditorMainPage):
    sample_manager_menu = method_editor_main_page.left_panel.sample_manager
    return sample_manager_menu


@when('the method is saved')
def save_method(instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.save_method(method_name=METHOD_NAME)


@when('the Favorite Settings menu is opened', target_fixture="favorites_menu")
@given('the Favorite Settings menu is opened', target_fixture="favorites_menu")
def open_favorite_setting_menu(method_editor_main_page: MethodEditorMainPage):
    favorite_menu = method_editor_main_page.left_panel.favorite_settings
    return favorite_menu


@given('the System menu is opened', target_fixture ="system_menu")
@when('the System menu is opened', target_fixture ="system_menu")
def open_system_menu(method_editor_main_page: MethodEditorMainPage):
    system_menu = method_editor_main_page.left_panel.system
    return system_menu


@when(cfparse('"{search_text}" is entered into the search bar'))
def enter_text_to_search(search_text: str, method_editor_main_page: MethodEditorMainPage):
    method_editor_main_page.search_text(search_text)


@when('the method is closed and reopened', target_fixture="method_editor_main_page")
def close_and_reopen_method(instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.close_method()
    instrument_method_editor_driver.open_method(METHOD_NAME)
    return instrument_method_editor_driver.method_editor_page


@then('no issues are present')
@then("no issue is raised")
def validate_issue_notification_absent(method_editor_main_page: MethodEditorMainPage):
    is_issue_notification_absent = method_editor_main_page.is_issue_notification_absent()
    assert is_issue_notification_absent, "Issue notification was present in Method Editor"


@then('an issue is still raised')
@then("an issue is raised")
def validate_issue_notification_exists(method_editor_main_page: MethodEditorMainPage):
    is_issue_notification_present = method_editor_main_page.is_issue_notification_present()
    assert is_issue_notification_present, "Issue notification was not present in Method Editor"


@then(cfparse('the issue has title "{title}" and description "{description}"'))
def check_issue_notification_exists_in_issues_list(title: str, description: str, method_editor_main_page: MethodEditorMainPage):
    issues_list = method_editor_main_page.get_issues_notifications()
    assert {"title": title, "description": description} in issues_list, (
        f"Issue with title: [{title}] and description [{description}] was not found on issues list: {issues_list}")


@when(cfparse('the "{title}" issue indicator is selected'))
def select_issue_notification_in_issues_list(title: str, method_editor_main_page: MethodEditorMainPage):
    method_editor_main_page.open_issue_element(title)


@then(cfparse('only the "{favorite_setting}" menu title is displayed'))
def validate_sample_temperature_menu(favorites_menu: FavoritesMenu, favorite_setting: str):
    expected_favorite_settings = [favorite_setting]
    favorites_menu.validate_expected_favorites(expected_favorite_settings)


@then(cfparse('the "{specific_menu}" menu is highlighted'))
def check_menu_is_highlighted(specific_menu: str):
    # TODO currently there is no possibility to determine that a menu is highlighted
    pass
