import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.prime_solvents_workflow_constants import PrimeSolventsWorkflowConstants
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import SystemLeakTestWorkFlowSummaryLocators
from web_framework.kiosk.pages.Locators.Setup.prime_solvents_workflow_locators import (PrimeSolventsWorkflowLocators,
                                                                                       SolventLinesOptionLocators,
                                                                                       CompositionOptionLocators,
                                                                                       FinalOptionsLocators,
                                                                                       PrimeSolventsWelcomeScreenLocators,
                                                                                       PrimeSummaryLocators)
from web_framework.kiosk.pages.Locators.Setup.setup_screen_locators import SetupScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Setup.prime_solvents_workflow_screen import PrimeMultiSolventWorkflowSetupScreen
from web_framework.kiosk.pages.Setup.prime_workflow_results_screen import PrimeResultScreen
from web_framework.kiosk.pages.Setup.prime_workflow_summary_screen import PrimeSummaryScreen
from web_framework.kiosk.pages.Setup.setup_home_screen import SetupHomeScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SetupScreen/prime_solvents_workflow.feature')
logger = Logger("test_prime_solvents_workflow")


@pytest.fixture
def prime_solvents_setup_page(page_builder):
    page = page_builder(PrimeMultiSolventWorkflowSetupScreen)
    return page


@pytest.fixture
def prime_summary_screen_page(page_builder):
    page = page_builder(PrimeSummaryScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def prime_result_screen_page(page_builder):
    page = page_builder(PrimeResultScreen)
    page.implicitly_wait()
    return page


@when('User starts the workflow')
def begin_prime_solvents_workflow(setup_screen_page: SetupHomeScreen, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    setup_screen_page.validate_setup_screen()
    setup_screen_page.validate_idle_state()
    setup_screen_page.tap(SetupScreenLocators.SOLVENTS_PANEL)
    prime_solvents_setup_page.validate_setup_selection_screen()
    prime_solvents_setup_page.tap(PrimeSolventsWorkflowLocators.START_PANEL)
    prime_solvents_setup_page.validate_welcome_screen()


@when('User validates the welcome context in the welcome screen')
def validate_text(prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen, prime_result_screen_page: PrimeResultScreen):
    prime_solvents_setup_page.validate_welcome_screen()
    actual_paragraph_text = prime_solvents_setup_page.get_welcome_paragraph_text()
    expected_paragraph_text = PrimeSolventsWorkflowConstants.expected_welcome_paragraph_text
    if actual_paragraph_text != expected_paragraph_text:
        prime_solvents_setup_page.tap(PrimeSolventsWorkflowLocators.CANCEL_BUTTON)
        prime_result_screen_page.tap(BasePageLocators.BACK_BUTTON)


@when('User validates the Caution text in the caution screen')
def validate_caution_text(prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen,
                          prime_result_screen_page: PrimeResultScreen):
    prime_solvents_setup_page.wait_time_to_load_value(PrimeSolventsWelcomeScreenLocators.SECOND_CAUTION_TEXT, "")
    actual_usage_list_text = prime_solvents_setup_page.get_caution_list_text()
    expected_usage_list_text = PrimeSolventsWorkflowConstants.expected_caution_list_text
    if actual_usage_list_text != expected_usage_list_text:
        prime_solvents_setup_page.tap(PrimeSolventsWorkflowLocators.CANCEL_BUTTON)
        prime_result_screen_page.tap(BasePageLocators.BACK_BUTTON)


@when(cfparse('User sets the solvent toggle "{solvent_toggle:bool}"', CONVERTERS))
def toggle_solvent_selection(solvent_toggle: bool, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.validate_line_selection_screen()
    prime_solvents_setup_page.set_toggle_button(SolventLinesOptionLocators.SOLVENT_LINE_TOGGLE, solvent_toggle)


@when(cfparse('User sets the composition toggle "{comp_toggle:bool}"', CONVERTERS))
def toggle_solvent_selection(comp_toggle: bool, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.validate_comp_selection_screen()
    prime_solvents_setup_page.set_toggle_button(CompositionOptionLocators.COMPOSITION_TOGGLE, comp_toggle)


@when(cfparse('User sets "{prime_duration}" in "{unit}" for the "{solvent_lines}"'))
def select_prime_solvent_lines(solvent_lines: str, prime_duration: str, unit: str, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.select_prime_solvent_lines(solvent_lines)
    prime_solvents_setup_page.tap_next_button()
    prime_solvents_setup_page.validate_prime_by_line_duration_screen()
    prime_solvents_setup_page.validate_stepper_button_appeared()
    prime_solvents_setup_page.set_time_stepper(SolventLinesOptionLocators.PRIMING_STEPPER_COMPONENT, unit, prime_duration)


@when(cfparse('User sets "{line_1}", "{line_2}", "{line_3}", "{line_4}" composition solvent lines'))
def select_prime_by_composition(line_1: str, line_2: str, line_3: str, line_4: str, flow_setting_screen_page: FlowSettingsScreen):
    solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    flow_setting_screen_page.enter_composition(solvent_composition)


@when(cfparse('User sets the "{com_duration}" for prime by composition'))
def set_composition_prime_duration(com_duration: str, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.validate_prime_by_comp_duration_screen()
    prime_solvents_setup_page.validate_time_edit_field_appeared()
    prime_solvents_setup_page.clear_num_pad_entries(CompositionOptionLocators.TIME_EDIT_FIELD)
    prime_solvents_setup_page.enter_value(com_duration)


@when(cfparse('User enters the "{flow_rate}" for "{eq_duration}" for composition "{line_1}" "{line_2}" "{line_3}" "{line_4}"'))
def set_final_conditions(flow_rate: str, eq_duration: str, line_1: str, line_2: str, line_3: str, line_4: str,
                         prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen, flow_setting_screen_page: FlowSettingsScreen):
    prime_solvents_setup_page.validate_final_flow_screen()
    prime_solvents_setup_page.enter_value(flow_rate)
    prime_solvents_setup_page.tap(FinalOptionsLocators.EQ_FIELD)
    prime_solvents_setup_page.enter_value(eq_duration)
    prime_solvents_setup_page.tap_next_button()
    solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    flow_setting_screen_page.enter_composition(solvent_composition)


@when(cfparse('User enters the flow rate to "{flow_rate}"'))
def set_flow_rate(flow_rate: str, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.validate_final_flow_screen()
    prime_solvents_setup_page.validate_flow_rate_edit_field_appeared()
    prime_solvents_setup_page.enter_value(flow_rate)


@when(cfparse('User enters the equilibration duration to "{eq_duration}"'))
def set_final_conditions(eq_duration: str, prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.validate_final_flow_screen()
    prime_solvents_setup_page.validate_eq_duration_edit_field_appeared()
    prime_solvents_setup_page.tap(FinalOptionsLocators.EQ_FIELD)
    prime_solvents_setup_page.enter_value(eq_duration)


@then(cfparse('User validate the summary screen details for solvent by line "{solvent_lines}", "{prime_duration}"'))
def validate_summary_screen(solvent_lines: str, prime_duration: str, prime_summary_screen_page: PrimeSummaryScreen):
    current_line_details = prime_summary_screen_page.get_solvent_by_line_details(solvent_lines, prime_duration)
    prime_summary_screen_page.validate_prime_summary_screen()
    actual_line_details = prime_summary_screen_page.get_text(PrimeSummaryLocators.PRIME_BY_LINE_DETAILS)
    assert current_line_details == actual_line_details, f"Solvent by line summary details are not as expected. " \
                                                        f"Expected: {current_line_details}. Actual: {actual_line_details}"


@then("User validate the solvent by line is not enabled")
def validate_summary_screen_not_selected_option(prime_summary_screen_page: PrimeSummaryScreen):
    prime_summary_screen_page.validate_prime_summary_screen()
    prime_summary_screen_page.wait_time_to_load_value(PrimeSummaryLocators.PRIME_BY_LINE_DETAILS)
    actual_line_details = prime_summary_screen_page.get_text(PrimeSummaryLocators.PRIME_BY_LINE_DETAILS)
    expected_line_details = PrimeSolventsWorkflowConstants.prime_by_line_not_selected
    assert actual_line_details == expected_line_details, f"Solvent by line status is not as expected. Expected: {expected_line_details}. " \
                                                         f"Actual: {actual_line_details}"


@then("User validate the solvent by composition is not enabled")
def validate_summary_screen_not_selected_option(prime_summary_screen_page: PrimeSummaryScreen):
    prime_summary_screen_page.validate_prime_summary_screen()
    prime_summary_screen_page.wait_time_to_load_value(PrimeSummaryLocators.PRIME_BY_COMPOSITION_DETAILS, "")
    actual_comp_details = prime_summary_screen_page.get_text(PrimeSummaryLocators.PRIME_BY_COMPOSITION_DETAILS)
    expected_comp_details = PrimeSolventsWorkflowConstants.prime_by_composition_not_selected
    assert actual_comp_details == expected_comp_details, f"Solvent by composition status is not as expected. Expected: {expected_comp_details}. " \
                                                         f"Actual: {actual_comp_details}"


@then(cfparse('User validate the solvent by composition "{line_1}" "{line_2}" "{line_3}" "{line_4}", "{com_duration}"'))
def validate_by_composition(line_1: str, line_2: str, line_3: str, line_4: str, com_duration: str, prime_summary_screen_page: PrimeSummaryScreen):
    current_comp_details = prime_summary_screen_page.get_solvent_by_composition_details(line_1, line_2, line_3, line_4, com_duration)
    actual_comp_details = prime_summary_screen_page.get_text(PrimeSummaryLocators.PRIME_BY_COMPOSITION_DETAILS)
    assert current_comp_details == actual_comp_details, f"Solvent by composition summary details are not as expected. " \
                                                        f"Expected: {current_comp_details}. Actual: {actual_comp_details}"


@then(cfparse('User validates the final condition for "{line_1}" "{line_2}" "{line_3}" "{line_4}", "{flow_rate}", "{eq_duration}"'))
def validate_final_condition(line_1: str, line_2: str, line_3: str, line_4: str, flow_rate: str, eq_duration: str,
                             prime_summary_screen_page: PrimeSummaryScreen):
    current_final_details = prime_summary_screen_page.get_solvent_by_final_details(line_1, line_2, line_3, line_4, flow_rate, eq_duration)
    actual_final_details = prime_summary_screen_page.get_text(PrimeSummaryLocators.FINAL_CONDITION_DETAILS)
    assert current_final_details == actual_final_details, f"Final conditions for Lines are not as expected. Expected: {current_final_details}" \
                                                          f"Actual: {actual_final_details}"


@then("User validates the workflow is completed successfully")
def validate_workflow_completion(prime_result_screen_page: PrimeResultScreen):
    prime_result_screen_page.tap(SystemLeakTestWorkFlowSummaryLocators.START_BUTTON)
    locator = PrimeSummaryLocators.WORKFLOW_COMPLETE_STATE
    expected_condition = PrimeSolventsWorkflowConstants.WorkFlowCompleteState
    error_message = PrimeSolventsWorkflowConstants.error_message
    wait_time = PrimeSolventsWorkflowConstants.TimeToComplete
    prime_result_screen_page.wait_till_condition_met(locator, expected_condition, error_message, wait_time)


@when('User taps next')
def navigate_next(prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.tap_next_button()


@then('User returns to setup')
def navigate_setup(prime_solvents_setup_page: PrimeMultiSolventWorkflowSetupScreen):
    prime_solvents_setup_page.tap(PrimeSolventsWorkflowLocators.CANCEL_BUTTON)
    prime_solvents_setup_page.validate_setup_selection_screen()
    prime_solvents_setup_page.tap(PrimeSolventsWorkflowLocators.SELECTIONS_BACK)


@then('User aborts the prime workflow')
def stop_workflow(prime_summary_screen_page: PrimeSummaryScreen):
    prime_summary_screen_page.tap(SystemLeakTestWorkFlowSummaryLocators.START_BUTTON)
    time.sleep(3)  # not condition involved, physically wait for 3 sec before aborting the workflow
    prime_summary_screen_page.validate_status_screen()
    prime_summary_screen_page.tap_stop_button()


@then('User validates the stopped status screen for the prime workflow')
def validate_workflow_summary(prime_summary_screen_page: PrimeSummaryScreen):
    prime_summary_screen_page.validate_abort_status_screen()


@then('User taps close button')
def home_page_navigation(prime_summary_screen_page: PrimeSummaryScreen):
    prime_summary_screen_page.tap(BasePageLocators.CLOSE_BUTTON)


@then(cfparse('User validates the "{minus_button:bool}" "{plus_button:bool}" "{reset_button:bool}" status', CONVERTERS))
def home_page_navigation(minus_button: bool, plus_button: bool, reset_button: bool, prime_summary_screen_page: PrimeSummaryScreen):
    prime_summary_screen_page.validate_stepper_button_minus_state(minus_button)
    prime_summary_screen_page.validate_stepper_button_plus_state(plus_button)
    prime_summary_screen_page.validate_stepper_button_reset_state(reset_button)


@then(cfparse('User validates the "{next_button:bool}" status', CONVERTERS))
def home_page_navigation(next_button: bool, prime_summary_screen_page: PrimeSummaryScreen):
    if next_button:
        assert prime_summary_screen_page.is_enabled(BasePageLocators.NEXT_BUTTON), "Next button state is not as expected. Expected : Enabled, Actual: Disabled"
    else:
        assert prime_summary_screen_page.is_disabled(BasePageLocators.NEXT_BUTTON), "Next button state is not as expected. Expected : Disabled. Actual: Enabled"


def build_solvent_composition_data(line_1: str, line_2: str, line_3: str, line_4: str) -> SolventComposition:
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


def build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4) -> SolventComposition:
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
