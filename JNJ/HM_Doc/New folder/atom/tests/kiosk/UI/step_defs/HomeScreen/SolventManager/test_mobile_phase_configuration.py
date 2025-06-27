import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse

from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.prime_solvents_workflow_constants import PrimeSolventsWorkflowConstants
from web_framework.kiosk.common.Constants.UI.condition_card_constants import MobilePhaseSolventConditionCard
from web_framework.kiosk.common.Constants.UI.solvent_bottles import SolventLineColorsConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SolventManager.mobile_phase_settings_screen import MobilePhaseSettingsScreen
from web_framework.kiosk.pages.Home.SolventManager.prime_solvent_screen import PrimeSolventSetupScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.mobile_phase_configuration_settings_locators import \
    MobilePhaseConfigurationSettingsScreenLocators as MobileLocators, PrimeSolventLocators, ReplaceSolventLocators, SolventDetailsLocators
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SolventManager/mobile_phase_configuration.feature')


@pytest.fixture
def solvent_manager_home_screen_page(page_builder):
    page = page_builder(SolventManagerHomeScreen)
    return page


@pytest.fixture
def mobile_phase_settings_screen(page_builder):
    page = page_builder(MobilePhaseSettingsScreen)
    return page


@pytest.fixture
def prime_solvent_workflow_setup_screens(page_builder):
    page = page_builder(PrimeSolventSetupScreen)
    return page


@given('User sets date and time format')
def set_date_time_setting(session_dash_board_screen_page: DashBoardScreen, user_profile_hub_screen_page: UserProfileHubScreen,
                          user_profile_settings_screen_page: UserProfileSettingsScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_user_settings_icon()
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.DATE_AND_TIME_TAB)
    user_profile_settings_screen_page.set_date_and_time_format(date_format='29 February 2020')
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
    user_profile_hub_screen_page.tap_done_button()
    session_dash_board_screen_page.tap_home()
    session_dash_board_screen_page.validate_dashboard_screen()


@when(cfparse('User taps the mobile phase "{mobile_phase}" condition card'))
def open_mobile_phase_condition_card(mobile_phase: str, dashboard_screen_page: DashBoardScreen, solvent_manager_home_screen_page: SolventManagerHomeScreen):
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_solvent_bottle_icon()
    solvent_manager_home_screen_page.validate_idle_state()
    solvent_manager_home_screen_page.tap_mobile_phase_condition_card(mobile_phase)


@when('User taps the configure solvent panel')
def tap_configure_solvent(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_selection_screen()
    mobile_phase_settings_screen.tap(MobileLocators.CONFIGURE_SOLVENT_PANEL)


@when(cfparse('User selects the mobile phase "{mobile_phase}" tab'))
def tap_mobile_phase_tab(mobile_phase: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.tap_mobile_phase_tab(mobile_phase)


@when('User taps the prime solvent panel')
def tap_prime_solvent(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_selection_screen()
    mobile_phase_settings_screen.tap(MobileLocators.PRIME_SOLVENT_PANEL)


@when('User taps the replace solvent panel')
def tap_replace_solvent(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_selection_screen()
    mobile_phase_settings_screen.tap(MobileLocators.REPLACE_SOLVENT_PANEL)


@when(cfparse('User sets the solvent level "{solvent_level}"'))
def set_solvent_level(solvent_level: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.set_solvent_level(solvent_level)
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_LEVEL_SLIDER_KNOB)
    # time for solvent level animation
    time.sleep(3)


@when(cfparse('User sets the "{solvent_expire_month}", "{solvent_expire_day}", and "{solvent_expire_year}"'))
def set_solvent_expire_date(solvent_expire_month: str, solvent_expire_day: str, solvent_expire_year: str,
                            mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.EXPIRATION_PANEL)
    mobile_phase_settings_screen.set_spinner_value(ReplaceSolventLocators.MONTH_PICKER, solvent_expire_month)
    mobile_phase_settings_screen.set_spinner_value(ReplaceSolventLocators.DAY_PICKER, solvent_expire_day)
    # TODO: Commented for now due to issue
    # mobile_phase_settings_screen.set_spinner_value(ReplaceSolventLocators.YEAR_PICKER, solvent_expire_year)


@when(cfparse('User sets the prepared by name "{prepared_by_name}"'))
def set_prepared_by_name(prepared_by_name: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.PREPARED_BY_PANEL)
    mobile_phase_settings_screen.set_spinner_value(ReplaceSolventLocators.PREPARED_BY_PICKER, prepared_by_name)


@when('User taps the prepared by tab')
def set_prepared_by_name(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.PREPARED_BY_PANEL)


@when('User taps the solvent name tab')
def set_solvent_name(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NAME_PANEL)


@when('User taps the notes tab')
def set_notes(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NOTE_PANEL)


@when(cfparse('User sets the solvent name "{solvent_name}"'))
def set_solvent_name(solvent_name: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NAME_PANEL)
    mobile_phase_settings_screen.set_spinner_value(ReplaceSolventLocators.SOLVENT_NAME_PICKER, solvent_name)


@when(cfparse('User enters the solvent note "{solvent_note}"'))
def enter_solvent_note(solvent_note: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NOTE_PANEL)
    mobile_phase_settings_screen.enter_string(solvent_note)
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.NOTE_DONE_BUTTON)
    mobile_phase_settings_screen.tap_done_button()


@when('User press the - button')
def delete_entry(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.PREPARED_BY_REMOVE_BUTTON)


@when('User press the - solvent button')
def delete_solvent_entry(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NAME_REMOVE_BUTTON)


@when(cfparse('User enters "{data}"'))
def enter_solvent_note(data: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.enter_string(data)


@when('User saves the changes')
def save(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.NOTE_DONE_BUTTON)


@when('User confirms deletion')
def tap_ok(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.wait_element_to_be_clickable(ReplaceSolventLocators.OK_BUTTON, mobile_phase_settings_screen.wait_time)
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.OK_BUTTON)


@when('User confirms the changes')
def tap_done(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(MobileLocators.DONE_BUTTON)


@when('User navigates to home screen')
def tap_cancel_button(mobile_phase_settings_screen: MobilePhaseSettingsScreen, dashboard_screen_page: DashBoardScreen):
    mobile_phase_settings_screen.tap_cancel_button()
    dashboard_screen_page.validate_dashboard_screen()


@when(cfparse('User selects the "{bottle_volume}" volume for "{mobile_phase}"'))
def select_bottle_volume(bottle_volume: str, mobile_phase: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.select_bottle_volume(mobile_phase, bottle_volume)


@when(cfparse('User selects the "{line_color}" color for "{mobile_phase}"'))
def select_line_color(line_color: str, mobile_phase: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.select_line_color(mobile_phase, line_color)


@when('User navigates to home screen')
def navigate_to_home(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap_cancel_button()


@when(cfparse('User toggles the "{mobile_phase}" toggle to "{toggle_status}"'))
def set_mobile_phase_toggle_status(mobile_phase: str, toggle_status: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.set_toggle_status(mobile_phase, toggle_status)


@when(cfparse('User sets the prime duration "{prime_duration}"'))
def set_prime_duration_time(prime_duration: str, prime_solvent_workflow_setup_screens: PrimeSolventSetupScreen):
    prime_solvent_workflow_setup_screens.validate_priming_options_screen()
    if "Cycle" not in prime_duration:
        prime_solvent_workflow_setup_screens.set_time_stepper(PrimeSolventLocators.PRIME_DURATION_STEPPER, PrimeSolventsWorkflowConstants.prime_unit,
                                                              prime_duration)


@when('User starts the prime cycle')
def start_prime_cycle(prime_solvent_workflow_setup_screens: PrimeSolventSetupScreen):
    prime_solvent_workflow_setup_screens.validate_priming_options_screen()
    prime_solvent_workflow_setup_screens.tap(PrimeSolventLocators.PRIME_START_BUTTON)


@when('User stops the prime cycle')
def stop_prime_cycle(prime_solvent_workflow_setup_screens: PrimeSolventSetupScreen):
    prime_solvent_workflow_setup_screens.validate_priming_progress_screen()
    prime_solvent_workflow_setup_screens.tap_stop_button()
    prime_solvent_workflow_setup_screens.validate_stop_info()
    prime_solvent_workflow_setup_screens.validate_simple_text_wait_condition(
        PrimeSolventLocators.PRIMING_PROGRESS_STATUS_LABEL, "Stopped", MobilePhaseSolventConditionCard.TimeToTerminate)


@when('User press the edit button')
def tap_edit(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.wait_element_to_be_clickable(ReplaceSolventLocators.PREPARED_BY_EDIT_BUTTON, mobile_phase_settings_screen.wait_time)
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.PREPARED_BY_EDIT_BUTTON)
    mobile_phase_settings_screen.wait_for_element_visibility(mobile_phase_settings_screen.wait_time, ReplaceSolventLocators.MAX_CHAR)


@when('User press the edit solvent button')
def tap_edit_solvent(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.wait_element_to_be_clickable(ReplaceSolventLocators.SOLVENT_NAME_EDIT_BUTTON, mobile_phase_settings_screen.wait_time)
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NAME_EDIT_BUTTON)
    mobile_phase_settings_screen.wait_for_element_visibility(mobile_phase_settings_screen.wait_time, ReplaceSolventLocators.MAX_CHAR)


@when('User press the add button')
def tap_add(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.PREPARED_BY_ADD_BUTTON)


@when('User press the add solvent')
def tap_add_solvent(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(ReplaceSolventLocators.SOLVENT_NAME_ADD_BUTTON)


@then('User validates the status screen after aborting')
def validate_status_screen(prime_solvent_workflow_setup_screens: PrimeSolventSetupScreen,
                           mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    prime_solvent_workflow_setup_screens.validate_simple_text_wait_condition(
        PrimeSolventLocators.PRIMING_PROGRESS_STATUS_LABEL,
        MobilePhaseSolventConditionCard.StoppedTextStatus, MobilePhaseSolventConditionCard.DefaultTestTime)
    mobile_phase_settings_screen.tap_done_button()


@then(cfparse('User validates the "{mobile_phase}" and installation status "{installation_status}"'))
def validate_mobile_phase_installation_status(installation_status: str, mobile_phase: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_installation(mobile_phase, installation_status)


@then(cfparse('User validates the solvent level is set to "{solvent_level}"'))
def validate_data_is_set(solvent_level: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.wait_till_condition_met(ReplaceSolventLocators.SOLVENT_LEVEL_INFO_LABEL, solvent_level,
                                                         f"The solvent level did not change to {solvent_level}", mobile_phase_settings_screen.wait_time)


@then(cfparse('the "{add_analyst_name}" is updated'))
def validate_prepared_by(add_analyst_name: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.wait_till_condition_met(ReplaceSolventLocators.PREPARED_BY_INFO_LABEL, add_analyst_name,
                                                         f"The analyst name did not change to {add_analyst_name}", mobile_phase_settings_screen.wait_time)


@then(cfparse('User validates the "{mobile_phase}" is "{status}"'))
def validate_mobile_phase_configuration_status(mobile_phase: str, status: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_configured(mobile_phase, status)


@then(cfparse('User validates the prime cycle was completed within "{max_prime_time}"'))
def validate_prime_cycle_completed(max_prime_time: str, prime_solvent_workflow_setup_screens: PrimeSolventSetupScreen):
    prime_solvent_workflow_setup_screens.validate_priming_progress_screen()
    prime_solvent_workflow_setup_screens.validate_simple_text_wait_condition(
        PrimeSolventLocators.PRIMING_PROGRESS_STATUS_LABEL, "Complete", TypeConverter.to_float(max_prime_time))
    prime_solvent_workflow_setup_screens.tap_done_button()
    prime_solvent_workflow_setup_screens.validate_idle_state()


@then(cfparse('User verifies "{bottle_volume}" and "{line_color}" were saved for "{mobile_phase}"'))
def validate_configuration_settings_saved(bottle_volume: str, line_color: str, mobile_phase: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.validate_saved_mobile_phase_settings(mobile_phase, bottle_volume, line_color)


@then(cfparse('User verifies "{bottle_volume}" and "{line_color}" were not changed for "{mobile_phase}"'))
def validate_configuration_settings_saved(mobile_phase: str, bottle_volume: str, line_color: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.validate_saved_mobile_phase_settings(mobile_phase, bottle_volume, line_color)


@then(cfparse('User verifies "{default_bottle_volume}" and "{default_line_color}" were not changed for "{mobile_phase}"'))
def validate_changes_unsaved(mobile_phase: str, default_bottle_volume: str, default_line_color: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen,
                             dashboard_screen_page: DashBoardScreen):
    mobile_phase_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_settings_screen.validate_unsaved_mobile_phase_settings(mobile_phase, default_bottle_volume,
                                                                        default_line_color)
    mobile_phase_settings_screen.tap_done_button()
    mobile_phase_settings_screen.validate_mobile_phase_selection_screen()
    mobile_phase_settings_screen.tap_cancel_button()
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_solvent_bottle_icon()


@then('User cancels the changes')
def tap_cancel(mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.tap(MobileLocators.CANCEL_BUTTON)


@then(cfparse('User confirms the color of the "{mobile_phase}" bottle in the schematic icon home page is "{line_color}"'))
def validate_color(mobile_phase: str, line_color: str, solvent_manager_home_screen_page: SolventManagerHomeScreen):
    actual_line_color = solvent_manager_home_screen_page.get_line_color(mobile_phase)
    expected_color = getattr(SolventLineColorsConstants, line_color)
    assert actual_line_color == expected_color, f"The actual line color selected is not as expected. Expected:[{expected_color}] Actual:[{actual_line_color}]"


@then(cfparse('User validates the "{prepared_by_name}" was saved'))
def validate_replace_solvent_settings(prepared_by_name: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_selection_screen()
    actual_name = mobile_phase_settings_screen.get_text(ReplaceSolventLocators.PREPARED_BY_INFO_LABEL)
    assert prepared_by_name == actual_name, f"Prepared by name was not saved. Expected:[{prepared_by_name}] Actual:[{actual_name}]"


@then(cfparse('the "{name_change}" is displayed'))
def validate_analysts(name_change: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    assert mobile_phase_settings_screen.is_data_present(name_change), f"The new data {name_change} is not present"


@then(cfparse('User validates "{max_allowed_characters}" is the max number of the characters that can be written'))
def validate_max_length(max_allowed_characters: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    max_characters = mobile_phase_settings_screen.get_text(ReplaceSolventLocators.MAX_CHAR)
    assert max_characters == f"{max_allowed_characters}/{max_allowed_characters} characters", f"The max allowed character is incorrect. " \
                                                                                              f"Expected:[{max_allowed_characters}] Actual:[{max_characters}]"


@then(cfparse('User Confirms the "{name_change}" is deleted'))
def validate_deletion(name_change: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    assert not mobile_phase_settings_screen.is_data_present(name_change), f"The new data {name_change} is present"


@then(cfparse(
    'User validates the following were saved: "{solvent_level}", "{solvent_expire_month}", '
    '"{solvent_expire_day}", "{solvent_expire_year}", "{prepared_by_name}", "{solvent_name}", and "{solvent_note}"'))
def validate_replace_solvent_settings(solvent_level: str, solvent_expire_month: str, solvent_expire_day: str,
                                      solvent_expire_year: str, prepared_by_name: str, solvent_name: str, solvent_note: str,
                                      mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_solvent_replacement_screen()
    mobile_phase_settings_screen.validate_solvent_level(solvent_level)
    mobile_phase_settings_screen.validate_solvent_expiry(ReplaceSolventLocators.EXPIRY_INFO_LABEL, solvent_expire_month, solvent_expire_day,
                                                         solvent_expire_year)
    actual_name = mobile_phase_settings_screen.get_text(ReplaceSolventLocators.PREPARED_BY_INFO_LABEL)
    assert prepared_by_name == actual_name, f"The prepared by name is not as expected. Expected:[{prepared_by_name}] Actual:[{actual_name}]"
    actual_solvent = mobile_phase_settings_screen.get_text(ReplaceSolventLocators.SOLVENT_NAME_INFO_LABEL)
    assert solvent_name == actual_solvent, f"The solvent name is not as expected. Expected:[{solvent_name}] Actual:[{actual_solvent}]"
    actual_note = mobile_phase_settings_screen.get_text(ReplaceSolventLocators.SOLVENT_NOTE_INFO_LABEL)
    assert solvent_note == actual_note, f"The solvent name is not as expected. Expected:[{solvent_note}] Actual:[{actual_note}]"
    mobile_phase_settings_screen.tap_done_button()


@then(cfparse(
    'User validates the following in the solvent details screen: "{solvent_level}", "{solvent_expire_month}", '
    '"{solvent_expire_day}", "{solvent_expire_year}", "{prepared_by_name}", "{solvent_name}", and "{solvent_note}" for "{bottle_volume}"'))
def validate_solvent_details_screen_information(solvent_level: str,
                                                solvent_expire_month: str, solvent_expire_day: str, solvent_expire_year: str, prepared_by_name: str,
                                                solvent_name: str, solvent_note: str,
                                                bottle_volume: str, mobile_phase_settings_screen: MobilePhaseSettingsScreen):
    mobile_phase_settings_screen.validate_mobile_phase_selection_screen()
    mobile_phase_settings_screen.tap(MobileLocators.DETAILS_BUTTON)
    mobile_phase_settings_screen.validate_mobile_phase_details_screen()
    mobile_phase_settings_screen.wait_time_to_load_value(SolventDetailsLocators.SOLVENT_NOTE_INFO_LABEL)
    actual_solvent = mobile_phase_settings_screen.get_text(MobileLocators.SOLVENT_NAME)
    assert solvent_name == actual_solvent, f"The solvent name is not as expected. Expected:[{solvent_name}] " \
                                           f"Actual:[{actual_solvent}]"
    mobile_phase_settings_screen.validate_details_solvent_level(solvent_level, bottle_volume)
    mobile_phase_settings_screen.validate_solvent_expiry(SolventDetailsLocators.EXPIRY_INFO_LABEL, solvent_expire_month, solvent_expire_day,
                                                         solvent_expire_year)
    actual_name = mobile_phase_settings_screen.get_text(SolventDetailsLocators.PREPARED_BY_INFO_LABEL)
    assert prepared_by_name == actual_name, f"The prepared by name is not as expected. Expected:[{prepared_by_name}] Actual:[{actual_name}]"
    actual_note = mobile_phase_settings_screen.get_text(SolventDetailsLocators.SOLVENT_NOTE_INFO_LABEL)
    assert solvent_note == actual_note, f"The solvent name is not as expected. Expected:[{solvent_note}] Actual:[{actual_note}]"
