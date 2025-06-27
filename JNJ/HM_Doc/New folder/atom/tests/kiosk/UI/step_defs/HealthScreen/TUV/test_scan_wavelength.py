import time
from datetime import datetime
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.scan_wavelength_constants import ScanWavelengthConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.TUV.scan_wavelength_summary_screen import ScanWavelengthSummaryScreen
from web_framework.kiosk.pages.Health.TUV.scan_wavelength_workflow_screen import ScanWavelengthWorkflowSetupScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Locators.Health.TUV.scan_wavelength_workflow_locators import PreparationLocator, \
    ScanWavelengthFlushOptionLocators, ScanWavelengthSetupLocators
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/TUV/scan_wavelength_workflow.feature')
logger = Logger("test_scan_wavelength_workflow")


@pytest.fixture
def scan_wavelength_workflow_setup_page(page_builder):
    page = page_builder(ScanWavelengthWorkflowSetupScreen)
    return page


@pytest.fixture
def scan_wavelength_workflow_summary_page(page_builder):
    page = page_builder(ScanWavelengthSummaryScreen)
    return page


@given("User navigates to TUV section within health troubleshoot area")
def navigate_troubleshoot_tuv(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)
    health_screen_page.tap(HealthScreenLocators.TUV_SECTION_ICON)


@when('User taps the scan wavelength panel')
def start_scan_wavelength_workflow(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.SCAN_WAVELENGTH_ICON)


@when('User validates the welcome context in the welcome screen')
def validate_welcome_text(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen):
    scan_wavelength_workflow_setup_page.validate_welcome_screen()
    try:
        actual_paragraph_text = scan_wavelength_workflow_setup_page.get_welcome_paragraph_text()
        logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

        expected_paragraph_text = ScanWavelengthConstants.expected_welcome_paragraph_text
        logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    finally:
        scan_wavelength_workflow_setup_page.tap_next_button()


@when(cfparse('User selects the "{mode}"'))
def select_mode(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, mode):
    scan_wavelength_workflow_setup_page.validate_mode_screen()
    scan_wavelength_workflow_setup_page.tap_mode(mode)
    scan_wavelength_workflow_setup_page.tap_next_button()


@when(cfparse('User selects the "{delivery_method}"'))
def select_delivery_mode(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, delivery_method):
    scan_wavelength_workflow_setup_page.validate_sample_delivery_screen()
    time.sleep(1)
    scan_wavelength_workflow_setup_page.tap_sample_delivery_option(delivery_method)
    scan_wavelength_workflow_setup_page.tap_next_button()


@when(cfparse('User validates the materials needed for "{delivery_method}"'))
def validate_materials_text(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, delivery_method):
    scan_wavelength_workflow_setup_page.validate_tools_materials_screen()
    try:

        if delivery_method == "cuvettes":
            logger.info(" The recommendations for calibration test using cuvettes")
            scan_wavelength_workflow_setup_page.validate_recommended_materials_for_pm_test_using_cuvettes()

        elif delivery_method == "flow_cell":
            logger.info(" The recommendations for calibration test using flow cell")
            time.sleep(2)
            scan_wavelength_workflow_setup_page.validate_recommended_materials_for_pm_test_using_flowcell()


    finally:
        scan_wavelength_workflow_setup_page.tap_next_button()


@when('User validates the preparation text')
def validate_preparation_text(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen):
    scan_wavelength_workflow_setup_page.validate_preparations_screen()
    try:
        scan_wavelength_workflow_setup_page.validate_preparation_materials_for_pm_test()

    finally:
        scan_wavelength_workflow_setup_page.tap(PreparationLocator.CHECK_BOX)
        scan_wavelength_workflow_setup_page.tap_next_button()


@when('User confirms the preconditions')
def validate_preconditions(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen):
    time.sleep(1)
    scan_wavelength_workflow_setup_page.tap(PreparationLocator.PRECONDITIONS_CHECK_BOX)
    scan_wavelength_workflow_setup_page.tap_next_button()

    # Preconditions screens are being reworked
    # scan_wavelength_workflow_setup_page.validate_preconditions_screen()
    # is_condition_lamp_met = scan_wavelength_workflow_setup_page.is_condition_met(
    #     PreparationLocator.LAMP_CONDITION_LABEL)
    # is_condition_cuvette_met = scan_wavelength_workflow_setup_page.is_condition_met(
    #     PreparationLocator.CUVETTE_CONDITION_LABEL)
    # is_current_tuv_door_met = scan_wavelength_workflow_setup_page.is_condition_met(
    #     PreparationLocator.TUV_DOOR_CONDITION_LABEL)
    #
    # if is_condition_lamp_met and is_current_tuv_door_met and is_condition_cuvette_met:
    #     logger.info(f"All the condition are met")
    #     time.sleep(1)
    #     scan_wavelength_workflow_setup_page.tap(PreparationLocator.PRECONDITIONS_CHECK_BOX)
    #     scan_wavelength_workflow_setup_page.tap_next_button()

    # else:
    #     assert False, "The test cannot be continued as the conditions were not met"


@then(cfparse('User validates the "{min_wavelength}", "{maxi_wavelength}" and "{date_rate}" in the summary screen'))
def validate_summary_screen(scan_wavelength_workflow_summary_page: ScanWavelengthSummaryScreen, min_wavelength,
                            maxi_wavelength, date_rate, dashboard_screen_page: DashBoardScreen):
    try:
        current = scan_wavelength_workflow_summary_page.get_current_summary_details()
        logger.info(f" current=={current}")
        expected = scan_wavelength_workflow_summary_page.expected_summary_details(min_wavelength, maxi_wavelength,
                                                                                  date_rate)
        logger.info(f" expected=={expected}")
        assert current == expected, f'The wavelength summary details are incorrect. Current: '

    finally:
        scan_wavelength_workflow_summary_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_diagnose()


@when(cfparse('User sets the first flush with "{flow_rate}" and "{flush_duration}"'))
def set_flush_option_values(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen,
                            flow_rate, flush_duration):
    scan_wavelength_workflow_setup_page.validate_flow_options_screen()
    scan_wavelength_workflow_setup_page.set_toggle_button(ScanWavelengthFlushOptionLocators.FLUSH_DETECTOR_TOGGLE, True)
    scan_wavelength_workflow_setup_page.enter_value(flow_rate)
    scan_wavelength_workflow_setup_page.set_time_stepper(ScanWavelengthFlushOptionLocators.FLUSH_DURATION_STEPPER, 30,
                                                         flush_duration)
    scan_wavelength_workflow_setup_page.tap_next_button()


@when(cfparse('User validates the stepper icon when the "{flush_duration}" is set'))
def validate_stepper_icon(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, flush_duration,
                          dashboard_screen_page: DashBoardScreen):
    try:
        scan_wavelength_workflow_setup_page.set_toggle_button(ScanWavelengthFlushOptionLocators.FLUSH_DETECTOR_TOGGLE,
                                                              True)
        current_stepper_value = scan_wavelength_workflow_setup_page.get_user_input_text(
            ScanWavelengthFlushOptionLocators.FLUSH_DETECTOR_VALUE)
        logger.info(f" is_stepper_disabled=={current_stepper_value}")

        current_stepper_value = datetime.strptime(current_stepper_value, '%M : %S').time()
        flush_duration_value = datetime.strptime(flush_duration, '%M:%S').time()

        logger.info(f" current_stepper_value=={current_stepper_value}")
        logger.info(f" flush_duration {flush_duration}")
        if current_stepper_value >= flush_duration_value:
            logger.info(" current_stepper_value >= flush_duration===")

            scan_wavelength_workflow_setup_page.set_time_stepper(
                ScanWavelengthFlushOptionLocators.FLUSH_DURATION_STEPPER,
                30,
                flush_duration)

            start_time = time.time()
            while time.time() - start_time < 5:
                logger.info(" current_stepper_value >= flush_duration===")
                is_stepper_disabled = scan_wavelength_workflow_setup_page.is_default_value_button_disabled(
                    ScanWavelengthFlushOptionLocators.DECREMENT_INPUT_STEPPER)
                logger.info(f" is_stepper_disabled>= {is_stepper_disabled}")
                if is_stepper_disabled:
                    break
                time.sleep(1)

            assert is_stepper_disabled is True

        else:
            logger.info(" current_stepper_valu lesser flush_duration===")
            scan_wavelength_workflow_setup_page.set_time_stepper(
                ScanWavelengthFlushOptionLocators.FLUSH_DURATION_STEPPER,
                30,
                flush_duration)
            start_time = time.time()
            while time.time() - start_time < 5:
                is_stepper_disabled = scan_wavelength_workflow_setup_page.is_default_value_button_disabled(
                    ScanWavelengthFlushOptionLocators.INCREMENT_INPUT_STEPPER)
                logger.info(" current_stepper_valu lesser flush_duration===")
                logger.info(f" is_stepper_disabled>= {is_stepper_disabled}")
                if is_stepper_disabled:
                    break
                time.sleep(1)

            assert is_stepper_disabled is True

    finally:
        scan_wavelength_workflow_setup_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_diagnose()


@when(cfparse('User selects for the solvent "{line}" for the first flush'))
def select_solvent_line(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, line):
    scan_wavelength_workflow_setup_page.validate_first_solvent_selection_screen()
    # TODO: Radio group is making an interception error
    time.sleep(1)
    scan_wavelength_workflow_setup_page.select_solvent_line(line)
    scan_wavelength_workflow_setup_page.tap_next_button()


@when(cfparse('User sets the second flush with "{flow_rate}" and "{flush_duration}"'))
def set_flush_option_values(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen,
                            flow_rate, flush_duration):
    scan_wavelength_workflow_setup_page.validate_second_flow_options_screen()
    scan_wavelength_workflow_setup_page.set_toggle_button(ScanWavelengthFlushOptionLocators.FLUSH_DETECTOR_TOGGLE, True)
    scan_wavelength_workflow_setup_page.enter_value(flow_rate)
    scan_wavelength_workflow_setup_page.set_time_stepper(ScanWavelengthFlushOptionLocators.FLUSH_DURATION_STEPPER, 30,
                                                         flush_duration)
    scan_wavelength_workflow_setup_page.tap_next_button()


@when('User selects for the solvent "{line}" for the second flush')
def select_solvent_line(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, line):
    scan_wavelength_workflow_setup_page.validate_second_solvent_selection_screen()
    time.sleep(1)
    scan_wavelength_workflow_setup_page.select_solvent_line(line)
    scan_wavelength_workflow_setup_page.tap_next_button()


@when(cfparse('User sets the wavelength range "{min_wavelength}", "{maxi_wavelength}" and "{date_rate}"'))
def set_wavelength_values(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen,
                          min_wavelength, maxi_wavelength, date_rate):
    try:
        scan_wavelength_workflow_setup_page.select_and_get_wavelength_range(min_wavelength, maxi_wavelength)
        scan_wavelength_workflow_setup_page.tap(ScanWavelengthSetupLocators.SCAN_RATE_PANEL)
        scan_wavelength_workflow_setup_page.set_spinner_value(ScanWavelengthSetupLocators.SCAN_RATE_PICKER_COMPONENT,
                                                              date_rate)

    finally:
        scan_wavelength_workflow_setup_page.tap_next_button()


@then(cfparse('User validates the reset icon "{is_disable}" when the "{flush_duration}" is set'))
def validate_reset_icon(scan_wavelength_workflow_setup_page: ScanWavelengthWorkflowSetupScreen, flush_duration,
                        is_disable, dashboard_screen_page: DashBoardScreen):
    try:
        scan_wavelength_workflow_setup_page.set_toggle_button(ScanWavelengthFlushOptionLocators.FLUSH_DETECTOR_TOGGLE,
                                                              True)
        scan_wavelength_workflow_setup_page.set_time_stepper(ScanWavelengthFlushOptionLocators.FLUSH_DURATION_STEPPER,
                                                             30,
                                                             flush_duration)

        start_time = time.time()
        while time.time() - start_time < 5:
            is_disabled = TypeConverter.to_bool(is_disable)
            is_reset_disabled = scan_wavelength_workflow_setup_page.is_default_value_button_disabled(
                ScanWavelengthFlushOptionLocators.RESET_STEPPER)

            if is_reset_disabled == is_disabled:
                break
            time.sleep(1)

        logger.info(f" is_stepper_disabled=={is_reset_disabled}")
        assert is_reset_disabled == is_disabled


    finally:
        scan_wavelength_workflow_setup_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_diagnose()
