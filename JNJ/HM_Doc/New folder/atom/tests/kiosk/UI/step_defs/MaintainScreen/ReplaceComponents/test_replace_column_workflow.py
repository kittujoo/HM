import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_column_workflow_constants import ReplaceColumnWorkflowConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_column_workflow_locators import ReplaceColumnWorkflowLocators, \
    ReplaceColumnNewColumnScreenLocators
from web_framework.kiosk.pages.Locators.Maintain.replace_components_locators import ReplaceComponentsScreenPageLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.ReplaceColumn.replace_column_workflow_setup_screen import ReplaceColumnWorkflowSetupScreen
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/MaintainScreen/ReplaceComponents/replace_column_workflow.feature')

logger = Logger(__name__)


def build_solvent_composition_data(line_1, line_2, line_3, line_4):
    """
    This function builds and returns a list using the input data from the feature file
    :param line_1: Test data from the feature file
    :param line_2: Test data from the feature file
    :param line_3: Test data from the feature file
    :param line_4: Test data from the feature file
    :return: solvent_composition
    """
    solvent_line_1 = SolventLine.parse(line_1)
    solvent_line_2 = SolventLine.parse(line_2)
    solvent_line_3 = SolventLine.parse(line_3)
    solvent_line_4 = SolventLine.parse(line_4)
    return build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4)


def build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4):
    """
    This function builds solvent composition for the given solvent line
    :param solvent_line_1: parsed data from the feature file
    :param solvent_line_2: parsed data from the feature file
    :param solvent_line_3: parsed data from the feature file
    :param solvent_line_4: parsed data from the feature file
    :return: solvent_composition
    """
    solvent_composition = SolventComposition()
    solvent_composition.add(solvent_line_1)
    solvent_composition.add(solvent_line_2)
    solvent_composition.add(solvent_line_3)
    solvent_composition.add(solvent_line_4)
    return solvent_composition


@pytest.fixture
def replace_column_setup_screen(page_builder):
    page = page_builder(ReplaceColumnWorkflowSetupScreen)
    return page


@given('User navigates to the replace components HUB area')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen, maintain_screen: MaintainScreen):
    logger.info("The user profile settings screen test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_maintain()
    maintain_screen.tap(MaintainScreenPageLocators.REPLACE_PANEL)


@when('User taps the replace column panel')
def tap_replace_column_panel(replace_components_hub_screen: ReplaceComponentsScreen):
    replace_components_hub_screen.tap(ReplaceComponentsScreenPageLocators.REPLACE_COLUMN)


@when('User validates the context in the welcome screen')
def validate_welcome_screen_information(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_welcome_screen()

    actual_paragraph_text = replace_column_setup_screen.get_welcome_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceColumnWorkflowConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_column_setup_screen.tap_next_button()


@when('User validates the context in the caution screen')
def validate_caution_screen_information(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_caution_screen()

    actual_paragraph_text = replace_column_setup_screen.get_caution_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ReplaceColumnWorkflowConstants.expected_caution_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    replace_column_setup_screen.tap_next_button()


@when(cfparse('User toggles the flush column option to "{flush_option}"'))
def toggle_flush_column_option(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen, flush_option):
    replace_column_setup_screen.validate_flush_column_screen()
    current_toggle_status = replace_column_setup_screen.is_toggle_button_enabled(ReplaceColumnWorkflowLocators.FLUSH_COLUMN_TOGGLE)
    desired_flush_option = TypeConverter.to_bool(flush_option)

    if not current_toggle_status and desired_flush_option:
        replace_column_setup_screen.tap(ReplaceColumnWorkflowLocators.FLUSH_COLUMN_TOGGLE)


@when(cfparse('User sets the "{flow_rate}"'))
def set_flow_rate(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen, flow_rate):
    replace_column_setup_screen.validate_flush_column_screen()
    replace_column_setup_screen.enter_value(flow_rate)


@when(cfparse('User sets the "{flow_duration}"'))
def set_flow_duration(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen, flow_duration):
    replace_column_setup_screen.validate_flush_column_screen()

    replace_column_setup_screen.set_time_stepper(ReplaceColumnWorkflowLocators.FLUSH_DURATION_STEPPER, 60, flow_duration)

    replace_column_setup_screen.tap_next_button()


@when('User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"')
@when(cfparse('User adds the solvent composition for solvent line "{line_1}", "{line_2}", "{line_3}", "{line_4}"'))
def set_solvent_composition(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen,
                            line_1, line_2, line_3, line_4):
    replace_column_setup_screen.validate_flush_column_composition_screen()
    # takes time for text to show up on this page
    time.sleep(1)
    solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    replace_column_setup_screen.enter_composition(solvent_composition)
    replace_column_setup_screen.tap_next_button()


@when(cfparse('User validates the flush column summary screen details, "{flow_rate}" "{expected_line_1}" "{expected_line_2}" "{expected_line_3}" "{expected_line_4}"'))
def validate_flush_column_summary_screen_details(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen,
                                                 flow_rate, expected_line_1, expected_line_2, expected_line_3,
                                                 expected_line_4):
    replace_column_setup_screen.validate_flush_column_summary_screen()
    replace_column_setup_screen.validate_summary_composition(flow_rate, expected_line_1, expected_line_2, expected_line_3, expected_line_4)


@when('User runs and validates the flush column test is completed')
def validate_flush_column_test(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_flush_column_summary_screen()
    replace_column_setup_screen.tap(ReplaceColumnWorkflowLocators.START_BUTTON)
    replace_column_setup_screen.validate_flush_column_status_screen()
    replace_column_setup_screen.validate_simple_text_wait_condition(ReplaceColumnWorkflowLocators.FLUSH_COLUMN_STATUS_LABEL, "Complete",
                                                                    WaitTimeConstants.MidWait)
    replace_column_setup_screen.tap_next_button()


@when('User checks the conditions within the preconditions screen')
def validate_preconditions_conditions(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_preconditions_screen()

    assert replace_column_setup_screen.is_condition_met(ReplaceColumnWorkflowLocators.COMPARTMENT_TEMPERATURE_STATUS_ICON)
    assert replace_column_setup_screen.is_condition_met(ReplaceColumnWorkflowLocators.FLOW_CONTROL_STATUS_ICON)

    replace_column_setup_screen.tap_next_button()


@when('User validates the context in the remove screen')
def validate_remove_screen_context(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_removal_screen()
    # validate context
    replace_column_setup_screen.tap_next_button()


@when('User validates the context in the install screen')
def validate_install_screen_context(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_installation_screen()
    # validate context
    replace_column_setup_screen.tap_next_button()


@when('User validates the new column information')
def validate_new_column_information(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_simple_text_wait_condition(ReplaceColumnNewColumnScreenLocators.SERIAL_NUMBER_INFO_LABEL,
                                                                    ReplaceColumnWorkflowConstants.NewSerialNumber, WaitTimeConstants.SmallWait)
    replace_column_setup_screen.tap_next_button()


@when(cfparse('User toggles the condition flow option to "{condition_flow_option}"'))
def toggle_condition_flow_option(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen, condition_flow_option):
    replace_column_setup_screen.validate_condition_column_screen()
    current_toggle_status = replace_column_setup_screen.is_toggle_button_enabled(ReplaceColumnWorkflowLocators.CONDITION_COLUMN_TOGGLE)
    desired_flush_option = TypeConverter.to_bool(condition_flow_option)

    if not current_toggle_status and desired_flush_option:
        replace_column_setup_screen.tap(ReplaceColumnWorkflowLocators.CONDITION_COLUMN_TOGGLE)


@when(cfparse('User sets the "{condition_flow_rate}"'))
def set_flow_rate(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen, condition_flow_rate):
    replace_column_setup_screen.validate_condition_column_screen()
    replace_column_setup_screen.enter_value(condition_flow_rate)
    replace_column_setup_screen.tap_next_button()


@when(cfparse('User adds the condition solvent composition for solvent line "{line_1}", "{line_2}", "{line_3"}, "{line_4}"'))
def set_condition_solvent_composition(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen,
                                      line_1, line_2, line_3, line_4):
    replace_column_setup_screen.validate_condition_solvents_column_screen()
    time.sleep(1)
    solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    replace_column_setup_screen.enter_composition(solvent_composition)
    replace_column_setup_screen.tap_next_button()


@when(cfparse('User sets the "{condition_duration}"'))
def set_condition_duration(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen, condition_duration):
    replace_column_setup_screen.validate_condition_duration_column_screen()

    replace_column_setup_screen.set_time_stepper(ReplaceColumnWorkflowLocators.CONDITION_DURATION_STEPPER, 30, condition_duration)

    replace_column_setup_screen.tap_next_button()


@when('User validates the information in the summary screen')
def validate_summary_screen_information(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_column_summary_screen()

    replace_column_setup_screen.tap(ReplaceColumnWorkflowLocators.START_BUTTON)


@when('User taps next')
def tap_next(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.tap_next_button()


@then('User validates the column condition process')
def validate_column_condition_process(replace_column_setup_screen: ReplaceColumnWorkflowSetupScreen):
    replace_column_setup_screen.validate_column_status_screen()
    replace_column_setup_screen.validate_simple_text_wait_condition(ReplaceColumnWorkflowLocators.CONDITION_COLUMN_STATUS_LABEL, "Complete",
                                                                    WaitTimeConstants.LongWait)
