import re
import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from utilities.datatables.converters import CONVERTERS
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.startup_constants import StartupConstants
from web_framework.kiosk.pages.Locators.Setup.setup_screen_locators import SetupScreenLocators
from web_framework.kiosk.pages.Locators.Setup.startup_workflow_locators import (StartupWorkflowLocators,
                                                                                StartupAdditionalPrimeSolventsLocators,
                                                                                StartupEquilibrationLocators,
                                                                                StartupDetectorLampLocators,
                                                                                StartupPrimeSolventsLocators,
                                                                                StartupWelcomeLocators,
                                                                                StartupTemperatureControlLocators,
                                                                                StartupSummaryLocators,
                                                                                SolventLinesOptionLocators)
from web_framework.kiosk.pages.Setup.setup_home_screen import SetupHomeScreen
from web_framework.kiosk.pages.Setup.startup_workflow_screen import StartupWorkflowSetupScreen
from web_framework.kiosk.pages.Setup.startup_workflow_summary_screen import StartupWorkflowSummaryScreen
from utilities.date_utilities import time_convertor

if __name__ == Path(__file__).stem:
    scenarios('../../features/SetupScreen/startup_workflow.feature')


@pytest.fixture
def startup_workflow_setup_page(page_builder):
    page = page_builder(StartupWorkflowSetupScreen)
    return page


@pytest.fixture
def startup_workflow_summary_page(page_builder):
    page = page_builder(StartupWorkflowSummaryScreen)
    return page


@when('User taps the startup workflow panel')
def begin_startup_workflow(setup_screen_page: SetupHomeScreen, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    setup_screen_page.validate_setup_screen()
    setup_screen_page.tap(SetupScreenLocators.STARTUP_WORKFLOW_START)
    startup_workflow_setup_page.validate_welcome_screen()
    startup_workflow_setup_page.tap_next_button()


@when('User navigates to the summary screen')
def navigate_summary_screen(startup_workflow_setup_page: StartupWorkflowSetupScreen):
    while not startup_workflow_setup_page.is_displayed(StartupSummaryLocators.SUMMARY_PAGE_BANNER):
        startup_workflow_setup_page.tap_next_button()


@when('User taps start button')
def tap_start(startup_workflow_setup_page: StartupWorkflowSetupScreen):
    startup_workflow_setup_page.tap(StartupWorkflowLocators.START_BUTTON)


@when('User aborts the workflow')
def abort_workflow(startup_workflow_summary_page: StartupWorkflowSummaryScreen):
    startup_workflow_summary_page.validate_simple_text_wait_condition(StartupSummaryLocators.STATUS_LABEL,
                                                                      StartupConstants.InProgressText,
                                                                      StartupConstants.DefaultTestTime)
    startup_workflow_summary_page.tap(StartupSummaryLocators.STOP_BUTTON)


@when('User navigates to startup workflow welcome screen')
def navigate_welcome_screen(setup_screen_page: SetupHomeScreen):
    setup_screen_page.validate_setup_screen()
    setup_screen_page.tap(SetupScreenLocators.STARTUP_WORKFLOW_START)


@when(cfparse('User enables set final conditions and set a "{flow_rate}"'))
def set_final_condition(context, flow_rate: str, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_set_final_conditions'] = flow_rate
    startup_workflow_setup_page.validate_equilibration_flow_screen()
    startup_workflow_setup_page.enable_toggle(StartupEquilibrationLocators.FLOW_RATE_TOGGLE)
    startup_workflow_setup_page.enter_value_for_specific_module(StartupEquilibrationLocators.FLOW_RATE_FIELD, flow_rate)
    startup_workflow_setup_page.tap_next_button()


@when(cfparse('User selects the solvent line "{solvent_line}"'))
def select_solvent_line(context, solvent_line: str, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_prime_solvents'] = solvent_line
    solvent_lines = solvent_line.split(",")
    startup_workflow_setup_page.wait_time_to_load_value(SolventLinesOptionLocators.SOLVENT_LINE_A)
    solvent_line_mapping = {"A": SolventLinesOptionLocators.SOLVENT_LINE_A,
                            "B": SolventLinesOptionLocators.SOLVENT_LINE_B,
                            "C": SolventLinesOptionLocators.SOLVENT_LINE_C,
                            "D": SolventLinesOptionLocators.SOLVENT_LINE_D}
    for solvent in solvent_line_mapping.keys():
        if solvent in solvent_lines:
            startup_workflow_setup_page.select_check_box(solvent_line_mapping[solvent])
        else:
            startup_workflow_setup_page.deselect_check_box(solvent_line_mapping[solvent])


@when('User deselect all lines on the prime solvents section')
def deselect_prime_solvent_lines(context, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_prime_seal_wash'] = 'Not selected'
    solvent_lines = [SolventLinesOptionLocators.SOLVENT_LINE_A, SolventLinesOptionLocators.SOLVENT_LINE_B,
                     SolventLinesOptionLocators.SOLVENT_LINE_C, SolventLinesOptionLocators.SOLVENT_LINE_D]

    for solvent_line in solvent_lines:
        startup_workflow_setup_page.wait_time_to_load_value(solvent_line)
        startup_workflow_setup_page.deselect_check_box(solvent_line)
    startup_workflow_setup_page.tap_next_button()


@when('User select disable on the prime seal wash solvent section')
@when('User select disable on the prime needle wash solvent section')
@when('User select disable on the prime sample metering solvent section')
def deselect_toggle(context, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_prime_seal_wash'] = context['expected_needle_wash_duration'] = context[
        'expected_meter_pump_duration'] = 'Not selected'
    startup_workflow_setup_page.wait_time_to_load_value(StartupAdditionalPrimeSolventsLocators.PRIME_TOGGLE)
    startup_workflow_setup_page.tap_toggle_button_off(StartupAdditionalPrimeSolventsLocators.PRIME_TOGGLE)
    startup_workflow_setup_page.tap_next_button()


@when('User set to off the sample temperature in the temperature control section')
def deselect_sample_temperature_toggle(context, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    startup_workflow_setup_page.wait_element_to_be_clickable(
        StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_TOGGLE, startup_workflow_setup_page.wait_time)
    context['expected_sample_temperature'] = 'Off'
    startup_workflow_setup_page.wait_time_to_load_value(StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.tap_toggle_button_off(StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_TOGGLE)


@when('User set to off the column temperature in the temperature control section')
def deselect_column_temperature_toggle(context, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_column_temperature'] = 'Off'
    startup_workflow_setup_page.wait_time_to_load_value(StartupTemperatureControlLocators.COLUMN_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.tap_toggle_button_off(StartupTemperatureControlLocators.COLUMN_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.tap_next_button()


@when('User disables set final conditions')
def deselect_final_conditions(context, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_set_final_conditions'] = 'Not selected'
    startup_workflow_setup_page.wait_time_to_load_value(StartupEquilibrationLocators.FLOW_RATE_TOGGLE)
    startup_workflow_setup_page.tap_toggle_button_off(StartupEquilibrationLocators.FLOW_RATE_TOGGLE)
    startup_workflow_setup_page.tap_next_button()


@when(cfparse('User sets the "{time_stepper}" using "{unit}" to "{desired_time}"'))
def set_priming_stepper_time(context, time_stepper: str, unit: str, desired_time: str,
                             startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_mobile_phase_duration'] = desired_time
    startup_workflow_setup_page.set_time_stepper(startup_workflow_setup_page.get_stepper_locator(time_stepper), unit,
                                                 desired_time)


@when(cfparse(
    'User sets the prime seal wash settings based upon "{prime_seal_toggle: bool}", "{unit}", and "{desired_time}"',
    CONVERTERS))
def set_prime_seal_wash_settings(context, prime_seal_toggle: bool, unit: str, desired_time: str,
                                 startup_workflow_setup_page: StartupWorkflowSetupScreen):
    startup_workflow_setup_page.tap_next_button()
    startup_workflow_setup_page.validate_seal_wash()
    context['expected_prime_seal_wash'] = desired_time if prime_seal_toggle is True else 'Not selected'
    startup_workflow_setup_page.wait_time_to_load_value(StartupAdditionalPrimeSolventsLocators.PRIME_TOGGLE)
    toggle_button_enabled = startup_workflow_setup_page.is_toggle_button_enabled(
        StartupAdditionalPrimeSolventsLocators.PRIME_TOGGLE)
    startup_workflow_setup_page.tap(
        StartupAdditionalPrimeSolventsLocators.PRIME_TOGGLE) if prime_seal_toggle != toggle_button_enabled else None
    startup_workflow_setup_page.set_time_stepper(StartupAdditionalPrimeSolventsLocators.PRIME_SEAL_STEPPER, unit,
                                                 desired_time) if prime_seal_toggle else None
    startup_workflow_setup_page.tap_next_button()


@when(cfparse(
    'User enables the prime needle wash solvent stepper components with "{prime_needle_toggle: bool}" and "{cycles_number}"',
    CONVERTERS))
def set_prime_seal_wash_solvent(context, prime_needle_toggle: bool, cycles_number: str,
                                startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_needle_wash_duration'] = cycles_number if prime_needle_toggle is True else "Not selected"
    startup_workflow_setup_page.wait_time_to_load_value(StartupAdditionalPrimeSolventsLocators.PRIME_NEEDLE_TOGGLE)
    startup_workflow_setup_page.validate_needle_wash()
    toggle_button_enabled = startup_workflow_setup_page.is_toggle_button_enabled(
        StartupAdditionalPrimeSolventsLocators.PRIME_NEEDLE_TOGGLE)
    startup_workflow_setup_page.tap(
        StartupAdditionalPrimeSolventsLocators.PRIME_NEEDLE_TOGGLE) if prime_needle_toggle != toggle_button_enabled else None
    startup_workflow_setup_page.set_numeric_stepper(StartupAdditionalPrimeSolventsLocators.PRIME_NEEDLE_STEPPER,
                                                    cycles_number) if prime_needle_toggle else None
    startup_workflow_setup_page.tap_next_button()


@when(cfparse(
    'User enables the prime sample metering solvent section with "{sample_metering_toggle: bool}" and "{number_of_cycles}"',
    CONVERTERS))
def select_prime_sample_metering_pump(context, sample_metering_toggle: bool, number_of_cycles: str,
                                      startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_meter_pump_duration'] = number_of_cycles if sample_metering_toggle is True else "Not selected"
    startup_workflow_setup_page.wait_time_to_load_value(
        StartupAdditionalPrimeSolventsLocators.PRIME_SAMPLE_METERING_TOGGLE)
    startup_workflow_setup_page.validate_sample_metering_pump_duration()
    toggle_button_enabled = startup_workflow_setup_page.is_toggle_button_enabled(
        StartupAdditionalPrimeSolventsLocators.PRIME_SAMPLE_METERING_TOGGLE)
    startup_workflow_setup_page.tap(StartupAdditionalPrimeSolventsLocators.PRIME_SAMPLE_METERING_TOGGLE) \
        if sample_metering_toggle != toggle_button_enabled else None
    startup_workflow_setup_page.set_numeric_stepper(
        StartupAdditionalPrimeSolventsLocators.PRIME_SAMPLE_METERING_STEPPER, number_of_cycles) \
        if sample_metering_toggle else None
    startup_workflow_setup_page.tap_next_button()


@when(cfparse('User sets the sample temperature based upon "{samp_temp_toggle:bool}" and "{desired_sample_temp_value}"',
              CONVERTERS))
def set_sample_temperature_settings(context, startup_workflow_setup_page, samp_temp_toggle: bool,
                                    desired_sample_temp_value: str):
    context['expected_sample_temperature'] = desired_sample_temp_value if samp_temp_toggle is True else "Off"
    startup_workflow_setup_page.wait_time_to_load_value(StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.validate_temperature_control_screen()
    toggle_button_enabled = startup_workflow_setup_page.is_toggle_button_enabled(
        StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.tap(
        StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_TOGGLE) if samp_temp_toggle != toggle_button_enabled else None
    startup_workflow_setup_page.set_spinner_value(StartupTemperatureControlLocators.SAMPLE_TEMPERATURE_LIST,
                                                  desired_sample_temp_value) \
        if samp_temp_toggle else None


@when(cfparse(
    'User sets the column temperature based upon "{col_temp_toggle: bool}" and "{desired_column_number_temp_value}"',
    CONVERTERS))
def set_column_temperature_settings(context, startup_workflow_setup_page, col_temp_toggle: bool,
                                    desired_column_number_temp_value: str):
    context['expected_column_temperature'] = desired_column_number_temp_value if col_temp_toggle is True else "Off"
    startup_workflow_setup_page.wait_time_to_load_value(StartupTemperatureControlLocators.COLUMN_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.validate_temperature_control_screen()
    toggle_button_enabled = startup_workflow_setup_page.is_toggle_button_enabled(
        StartupTemperatureControlLocators.COLUMN_TEMPERATURE_TOGGLE)
    startup_workflow_setup_page.tap(
        StartupTemperatureControlLocators.COLUMN_TEMPERATURE_TOGGLE) if col_temp_toggle != toggle_button_enabled else None
    if col_temp_toggle:
        startup_workflow_setup_page.tap(StartupTemperatureControlLocators.COLUMN_TEMPERATURE_PANEL)
        startup_workflow_setup_page.set_spinner_value(StartupTemperatureControlLocators.COLUMN_TEMPERATURE_NUMBER_LIST,
                                                      desired_column_number_temp_value)
    startup_workflow_setup_page.tap_next_button()


@when(cfparse('User sets the equilibrate volume to "{equilibration_time}"'))
def set_stepper_value(context, equilibration_time: str, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_equilibrate_duration'] = equilibration_time
    unit_value = "30"
    startup_workflow_setup_page.tap_next_button()
    startup_workflow_setup_page.wait_time_to_load_value(StartupEquilibrationLocators.EQUILIBRATE_TOGGLE_BUTTON)
    startup_workflow_setup_page.enable_toggle(StartupEquilibrationLocators.EQUILIBRATE_TOGGLE_BUTTON)
    startup_workflow_setup_page.set_time_stepper(StartupEquilibrationLocators.WAIT_MINUTES_STEPPER, unit_value,
                                                 equilibration_time)
    startup_workflow_setup_page.tap_next_button()


@when(cfparse('User turns the uv lamp to "{uv_lamp_toggle: bool}" state', CONVERTERS))
def select_tap_detector_toggle(context, uv_lamp_toggle: bool, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    context['expected_lamp_control'] = "On" if uv_lamp_toggle is True else "Off"
    startup_workflow_setup_page.wait_time_to_load_value(StartupDetectorLampLocators.UV_LAMP_TOGGLE)
    startup_workflow_setup_page.validate_detector_screen()
    toggle_button_enabled = startup_workflow_setup_page.is_toggle_button_enabled(
        StartupDetectorLampLocators.UV_LAMP_TOGGLE)
    startup_workflow_setup_page.tap(
        StartupDetectorLampLocators.UV_LAMP_TOGGLE) if uv_lamp_toggle != toggle_button_enabled else None
    startup_workflow_setup_page.tap_next_button()


@when(cfparse('User enters the solvent "{line_1}", "{line_2}", "{line_3}", "{line_4}" for sample metering pump'))
def set_sample_meter_composition(context, line_1: str, line_2: str, line_3: str, line_4: str,
                                 startup_workflow_setup_page: StartupWorkflowSetupScreen):
    lines = [line_1, line_2, line_3, line_4]
    startup_workflow_setup_page.validate_sample_metering_pump_composition()
    context['expected_sample_meter_composition'] = [line.split(',')[2] for line in lines if 'True' in line]
    startup_workflow_setup_page.selected_and_get_solvent_details(line_1, line_2, line_3, line_4)
    startup_workflow_setup_page.tap_next_button()


@when(cfparse(
    'User enters the solvent "{comp_line_1}", "{comp_line_2}", "{comp_line_3}", "{comp_line_4}" for equilibration'))
def set_equilibration_composition(context, comp_line_1: str, comp_line_2: str, comp_line_3: str, comp_line_4: str,
                                  startup_workflow_setup_page: StartupWorkflowSetupScreen):
    startup_workflow_setup_page.validate_equilibration_composition_screen()
    lines = [comp_line_1, comp_line_2, comp_line_3, comp_line_4]
    context['expected_equilibration_composition'] = [line.split(',')[2] for line in lines if 'True' in line]
    context['equilibration_solvent_composition'] = startup_workflow_setup_page.selected_and_get_solvent_details(
        comp_line_1, comp_line_2,
        comp_line_3, comp_line_4)


@when(cfparse('User stops the start up workflow at different "{stop_time_minutes:d}"'))
def abort_start_up_workflow(stop_time_minutes: int, startup_workflow_summary_page: StartupWorkflowSummaryScreen):
    stop_time_in_seconds = stop_time_minutes * StartupConstants.MinutesToSeconds
    time.sleep(stop_time_in_seconds)
    startup_workflow_summary_page.tap(StartupSummaryLocators.STOP_BUTTON)


@then('User verify that the start conditions set have been executed')
def validate_startup_completion(startup_workflow_summary_page: StartupWorkflowSummaryScreen):
    startup_workflow_summary_page.validate_startup_cycle_screen()
    startup_workflow_summary_page.validate_element_wait_condition(StartupSummaryLocators.STARTUP_PROGRESS_BANNER,
                                                                  StartupSummaryLocators.STARTUP_COMPLETE_BANNER,
                                                                  StartupConstants.ConfiguredTestTime)


@then('User validates the status screen for the startup workflow')
def validate_stop_workflow(startup_workflow_summary_page):
    startup_workflow_summary_page.validate_abort_status_screen()


@then('User validates the welcome context in the welcome screen')
def validate_text(startup_workflow_setup_page: StartupWorkflowSetupScreen):
    startup_workflow_setup_page.validate_welcome_screen()
    actual_paragraph_text = startup_workflow_setup_page.get_welcome_paragraph_text()
    expected_paragraph_text = StartupConstants.expected_welcome_paragraph_text
    assert actual_paragraph_text == expected_paragraph_text, f"Paragraph text was not as expected. " \
                                                             f"Expected paragraph text: {actual_paragraph_text}, " \
                                                             f"Actual paragraph text: {actual_paragraph_text}"


@then('User validates the usage list text in the welcome screen')
def validate_usage_list_test(startup_workflow_setup_page: StartupWorkflowSetupScreen):
    actual_usage_list_text = startup_workflow_setup_page.get_welcome_list_text()
    expected_usage_list_text = StartupConstants.expected_list_text
    assert actual_usage_list_text == expected_usage_list_text, f"Usage list text was not as expected. " \
                                                               f"Expected: {expected_usage_list_text}" \
                                                               f"Actual: {actual_usage_list_text}"


@then('User validates the recommendation text in the welcome screen')
def validate_recommendation_text(startup_workflow_setup_page: StartupWorkflowSetupScreen):
    actual_recommendation_text = startup_workflow_setup_page.get_text(StartupWelcomeLocators.RECOMMENDATION_TEXT)
    expected_recommendation_text = StartupConstants.WelcomeRecommendationText
    assert actual_recommendation_text == expected_recommendation_text, f"Recommendation text was not as expected. " \
                                                                       f"Expected:{expected_recommendation_text}" \
                                                                       f"Actual:{actual_recommendation_text}"


@then(cfparse('User validates the time was changed to "{desired_time}"'))
def validate_prime_time(desired_time: str, startup_workflow_setup_page: StartupWorkflowSetupScreen):
    prime_time = startup_workflow_setup_page.get_entered_value(StartupPrimeSolventsLocators.PRIMING_DURATION_FIELD)
    prime_time = prime_time.replace(" ", "")
    assert prime_time == desired_time, f"The time was not changed in the stepper component. " \
                                       f"Expected: {desired_time} Actual: {prime_time}"


@then('User validates the status stopped for the startup workflow')
def validate_status_screen(startup_workflow_summary_page: StartupWorkflowSummaryScreen):
    startup_workflow_summary_page.validate_abort_status_screen()


@then(cfparse('User validates the total composition is "{total_composition:f}"'))
def validate_total_composition(context, total_composition: float):
    current_composition = StartupConstants.Initial_composition
    for solvent in context['equilibration_solvent_composition'].get_solvent_lines():
        solvent = float(solvent)
        current_composition += solvent
    assert current_composition == total_composition, f"Composition was not as expected. " \
                                                     f"Expected: [{total_composition}], Actual: [{current_composition}]"


@then('User validates that all settings are presented on the summary page')
def validate_summary_screen(context, startup_workflow_summary_page: StartupWorkflowSummaryScreen):
    startup_workflow_summary_page.validate_startup_summary_screen()
    current_prime_mobile_phase_solvents = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.PRIME_MOBILE_PHASE_SOLVENTS)
    if current_prime_mobile_phase_solvents != 'Not selected':
        current_mobile_phase_prime_duration = startup_workflow_summary_page.get_container_text(
            StartupSummaryLocators.MOBILE_PHASE_PRIME_DURATION)
        expected_prime_solvents = re.sub(r"[^A-D]", "", context['expected_prime_solvents'])
        actual_prime_solvents = re.sub(r"[^A-D]", "", current_prime_mobile_phase_solvents)
        assert expected_prime_solvents == actual_prime_solvents, f"Mobile phase solvent was not as expected. Expected: {expected_prime_solvents} " \
                                                                 f"Actual: {actual_prime_solvents} "
        expected_mobile_phase_prime_duration, actual_mobile_phase_prime_duration = time_convertor(context['expected_mobile_phase_duration'],
                                                                                                  current_mobile_phase_prime_duration)

        assert expected_mobile_phase_prime_duration == actual_mobile_phase_prime_duration, f"Mobile phase prime_duration was not as expecetd. " \
                                                                                           f"Expected: {expected_mobile_phase_prime_duration} " \
                                                                                           f"Actual: {actual_mobile_phase_prime_duration}"

    current_prime_seal_wash = startup_workflow_summary_page.get_container_text(StartupSummaryLocators.PRIME_SEAL_WASH)
    current_needle_wash_duration = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.PRIME_NEEDLE_WASH)
    current_meter_pump_duration = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.SAMPLE_METER_PUMP)
    if current_meter_pump_duration != 'Not selected':
        current_sample_meter_composition = startup_workflow_summary_page.get_container_text(
            StartupSummaryLocators.SAMPLE_METER_PUMP_COMPOSITION)
        current_sample_meter_composition_list = [value.split('%')[0].strip() for value in
                                                 current_sample_meter_composition.split(',')]
        assert context[
                   'expected_sample_meter_composition'] == current_sample_meter_composition_list, f"Sample meter composition was not as expected. " \
                                                                                                  f"Expected: {context['expected_sample_meter_composition']} " \
                                                                                                  f"Actual: {current_sample_meter_composition_list}"

    current_sample_temperature = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.SAMPLE_TEMPERATURE)
    current_column_temperature = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.COLUMN_TEMPERATURE)
    current_lamp_control = startup_workflow_summary_page.get_container_text(StartupSummaryLocators.LAMP_CONTROL)
    current_set_final_conditions = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.SET_FINAL_CONDITIONS)
    current_equilibration_composition = startup_workflow_summary_page.get_container_text(
        StartupSummaryLocators.EQUILIBRATION_COMPOSITION)
    current_equilibrate_duration = startup_workflow_summary_page.get_container_text(StartupSummaryLocators.EQUILIBRATE)

    if context['expected_prime_seal_wash'] != 'Not selected':
        expected_prime_seal_wash_duration, actual_prime_seal_wash_duration = time_convertor(
            context['expected_prime_seal_wash'], current_prime_seal_wash)
        assert expected_prime_seal_wash_duration == actual_prime_seal_wash_duration, f"Prime seal wash duration was not as expected. Expected: " \
                                                                                     f"{expected_prime_seal_wash_duration} " \
                                                                                     f"Actual: {actual_prime_seal_wash_duration}"
    else:
        assert context[
                   'expected_prime_seal_wash'] == current_prime_seal_wash, f"Prime seal wash duration was not as expected. Expected: " \
                                                                           f"{context['expected_prime_seal_wash']} " \
                                                                           f"Actual: {current_prime_seal_wash}"

    assert context[
               'expected_needle_wash_duration'] in current_needle_wash_duration, f"Prime needle_wash duration was not as expected. " \
                                                                                 f"Expected: {context['expected_needle_wash_duration']} " \
                                                                                 f"Actual: {current_needle_wash_duration}"

    assert context[
               'expected_meter_pump_duration'] in current_meter_pump_duration, f"Sample meter pump duration was not as expected. " \
                                                                               f"Expected: {context['expected_meter_pump_duration']} " \
                                                                               f"Actual: {current_meter_pump_duration}"

    assert context[
               'expected_sample_temperature'] in current_sample_temperature, f"Sample temperature was not as expected. " \
                                                                             f"Expected: {context['expected_sample_temperature']} " \
                                                                             f"Actual: {current_sample_temperature}"

    assert context[
               'expected_column_temperature'] in current_column_temperature, f"Column temperature was not as expected. " \
                                                                             f"Expected: {context['expected_column_temperature']} " \
                                                                             f"Actual: {current_column_temperature}"
    assert context[
               'expected_lamp_control'] in current_lamp_control, f"UV Lamp control was not as expected. Expected: {context['expected_lamp_control']} " \
                                                                 f"Actual: {current_lamp_control}"
    assert context[
               'expected_set_final_conditions'] in current_set_final_conditions, f"Final condition flow rate was not as expected. " \
                                                                                 f"Expected: {context['expected_set_final_conditions']} " \
                                                                                 f"Actual: {current_set_final_conditions}"

    if current_set_final_conditions != "Not selected":
        expected_equilibrate_duration, actual_equilibrate_duration = time_convertor(context['expected_equilibrate_duration'], current_equilibrate_duration)
        assert expected_equilibrate_duration == actual_equilibrate_duration, f"Equilibrate duration was not as expected. " \
                                                                              f"Expected: {expected_equilibrate_duration} " \
                                                                              f"Actual: {actual_equilibrate_duration}"
        current_equilibration_composition_list = [value.split('%')[0].strip() for value in
                                                  current_equilibration_composition.split(',')]
        assert context[
                   'expected_equilibration_composition'] == current_equilibration_composition_list, f"Equilibration composition was not as expected. " \
                                                                                                    f"Expected: {context['expected_equilibration_composition']} " \
                                                                                                    f"Actual: {current_equilibration_composition_list}"
    else:
        assert "Not selected" in current_equilibration_composition, f"Equilibration composition was not as expected. " \
                                                                    f"Expected: Not selected " \
                                                                    f"Actual: {current_equilibration_composition}"
        assert "Not selected" in current_equilibrate_duration, f"Equilibrate duration was not as expected. " \
                                                               f"Expected: Not selected " \
                                                               f"Actual: {current_equilibrate_duration}"
