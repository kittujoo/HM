import time
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_screen import NeedleSealReadinessSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_summary_screen import NeedleSealReadinessSummaryScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_screen import SampleMeteringPumpSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_summary_screen import SampleMeteringPumpSummaryScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_setup_screen import SystemLeakTestSetupScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_summary_screen import SystemLeakTestSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.system_pressure_settings_screen import SystemPressureSettingsScreen
from web_framework.kiosk.pages.Locators.Health.SampleManager.needle_seal_readiness_workflow_locators import \
    NeedleSealReadinessLocators, NeedleSealReadinessSummaryLocators
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import \
    SampleMeteringPumpLocators, SampleMeteringPumpSummaryLocators, SampleMeteringPumpSetupLocators
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import SystemLeakTestLocators, \
    SystemLeakTestWorkflowLocators, SystemLeakTestWorkFlowSummaryLocators
from web_framework.kiosk.pages.Locators.System.instrument_configuration_screen import \
    InstrumentConfigurationScreenLocators
from web_framework.kiosk.pages.Locators.System.instrument_configuration_settings_screen import \
    InstrumentConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.System.instrument_configuration_settings_screen import InstrumentConfigurationSettingsScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SolventManager/system_pressure_condition_card.feature')

logger = Logger("test_system_pressure_condition_card")


@given('User navigates to the system pressure settings screen')
def navigate_system_pressure_card(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                                  system_pressure_setting_screen_page: SystemPressureSettingsScreen):
    logger.info("**************************The system pressure condition card test starts**********************")
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap_system_pressure_condition_card()
    system_pressure_setting_screen_page.validate_system_pressure_settings_screen()


@when('User goes back to the system pressure settings screen')
def tap_system_pressure_card(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                             system_pressure_setting_screen_page: SystemPressureSettingsScreen):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap_system_pressure_condition_card()
    system_pressure_setting_screen_page.validate_system_pressure_settings_screen()


@when(cfparse('User changes the unit to "{system_pressure_unit}"'))
def select_unit_option(system_pressure_setting_screen_page: SystemPressureSettingsScreen,
                       system_pressure_unit):
    system_pressure_setting_screen_page.validate_system_pressure_settings_screen()
    logger.info(f"Selecting the following pressure unit========>>>>>>{system_pressure_unit}")
    system_pressure_setting_screen_page.select_unit_option(system_pressure_unit)


@then(cfparse('User validates "{expected_system_pressure_unit}" in the system pressure conditional card'))
def validate_system_pressure_pressure_card(dashboard_screen_page: DashBoardScreen,
                                           solvent_manager_home_screen_page: SolventManagerHomeScreen,
                                           expected_system_pressure_unit):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    try:
        actual_system_pressure_unit = solvent_manager_home_screen_page.get_system_pressure_unit()
        assert actual_system_pressure_unit == expected_system_pressure_unit, f"The system pressure unit on system pressure conditional card is incorrect. \
        Expected: [{expected_system_pressure_unit}]. Actual: [{actual_system_pressure_unit}]"
    finally:
        dashboard_screen_page.tap_home()


@then(cfparse('User validates the "{expected_system_pressure_unit}" in the system leak test'))
def validate_system_leak_test_pressure_unit(expected_system_pressure_unit,
                                            dashboard_screen_page: DashBoardScreen,
                                            health_screen_page: HealthHomeScreen,
                                            leak_test_setup_screen_page: SystemLeakTestSetupScreen,
                                            dynamic_leak_test_summary_screen_page: SystemLeakTestSummaryScreen):
    try:
        dashboard_screen_page.tap_diagnose()
        health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)
        health_screen_page.validate_idle_state()
        health_screen_page.tap(SystemLeakTestLocators.DYNAMIC_LEAK_TEST_PANEL)
        leak_test_setup_screen_page.validate_welcome_screen()
        leak_test_setup_screen_page.tap_next_button()
        leak_test_setup_screen_page.validate_solvent_selection_screen()
        leak_test_setup_screen_page.tap_next_button()
        time.sleep(1)
        actual_system_leak_accumulator_pressure_unit = leak_test_setup_screen_page.get_accumulator_target_pressure_unit()
        actual_system_leak_accumulator_hint_pressure_unit = leak_test_setup_screen_page.get_accumulator_target_pressure_hint_unit()
        actual_system_leak_primary_pressure_unit = leak_test_setup_screen_page.get_primary_target_pressure_unit()
        assert expected_system_pressure_unit == actual_system_leak_accumulator_pressure_unit, f"The accumulator target pressure unit in the system leak test \
               is incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_system_leak_accumulator_pressure_unit}]"
        assert expected_system_pressure_unit == actual_system_leak_accumulator_hint_pressure_unit, f"The accumulator hint target pressure unit in the system \
               leak test is incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_system_leak_accumulator_hint_pressure_unit}]"
        assert expected_system_pressure_unit == actual_system_leak_primary_pressure_unit, f"The primary target pressure unit in the system leak test is \
               incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_system_leak_primary_pressure_unit}]"

        leak_test_setup_screen_page.tap_next_button()
        leak_test_setup_screen_page.validate_custom_options_screen()
        leak_test_setup_screen_page.tap_next_button()
        dynamic_leak_test_summary_screen_page.validate_summary_screen()
        dynamic_leak_test_summary_screen_page.wait_time_to_load_value \
            (SystemLeakTestWorkFlowSummaryLocators.ACCUMULATOR_TARGET_INFO_LABEL, "")

        actual_dynamic_leak_accumulator_pressure_unit = dynamic_leak_test_summary_screen_page.get_accumulator_target_pressure_unit()
        actual_dynamic_leak_primary_pressure_unit = dynamic_leak_test_summary_screen_page.get_primary_target_pressure_unit()
        assert expected_system_pressure_unit == actual_dynamic_leak_accumulator_pressure_unit, f"The accumulator target pressure unit in the dynamic leak test \
        is incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_dynamic_leak_accumulator_pressure_unit}]"
        assert expected_system_pressure_unit == actual_dynamic_leak_primary_pressure_unit, f"The primary target pressure unit in the dynamic leak test is \
        incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_dynamic_leak_primary_pressure_unit}]"

    finally:
        dynamic_leak_test_summary_screen_page.tap(SystemLeakTestWorkflowLocators.CANCEL_BUTTON)


@then(cfparse('User validates the "{expected_system_pressure_unit}" in the sample metering pump leak test'))
def validate_sample_metering_pressure_unit(expected_system_pressure_unit,
                                           health_screen_page: HealthHomeScreen,
                                           sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen,
                                           sample_metering_pump_workflow_summary_page: SampleMeteringPumpSummaryScreen):
    try:
        health_screen_page.validate_idle_state()
        health_screen_page.tap(HealthScreenLocators.SAMPLE_MANAGER_ICON)
        health_screen_page.tap(HealthScreenLocators.SAMPLE_METERING_PUMP_PANEL)
        sample_metering_pump_workflow_setup_page.validate_welcome_screen()
        sample_metering_pump_workflow_setup_page.tap_next_button()
        sample_metering_pump_workflow_setup_page.validate_solvent_setup_screen()
        sample_metering_pump_workflow_setup_page.tap_next_button()
        sample_metering_pump_workflow_setup_page.validate_priming_setup_screen()

        actual_sample_metering_setup_page_pressure_unit = sample_metering_pump_workflow_setup_page.get_target_pressure_unit()
        assert expected_system_pressure_unit == actual_sample_metering_setup_page_pressure_unit, f"The sample metering pressure unit on setup screen is \
        incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_sample_metering_setup_page_pressure_unit}]"
        sample_metering_pump_workflow_setup_page.wait_time_to_load_value(SampleMeteringPumpSetupLocators.TARGET_PRESSURE_HINT, "")
        actual_sample_metering_hint_setup_page_pressure_unit = sample_metering_pump_workflow_setup_page.get_target_pressure_hint_unit()
        assert expected_system_pressure_unit == actual_sample_metering_hint_setup_page_pressure_unit, f"The sample metering hint pressure unit on setup screen \
        is incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_sample_metering_hint_setup_page_pressure_unit}]"

        sample_metering_pump_workflow_setup_page.tap_next_button()
        sample_metering_pump_workflow_summary_page.wait_time_to_load_value(SampleMeteringPumpSummaryLocators.TARGET_PRESSURE_INFO_LABEL, "")
        actual_sample_metering_summary_page_pressure_unit = sample_metering_pump_workflow_summary_page.get_target_pressure_unit()
        assert expected_system_pressure_unit == actual_sample_metering_summary_page_pressure_unit, f"The sample metering pressure unit on summary screen is \
        incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_sample_metering_summary_page_pressure_unit}]"
    finally:
        sample_metering_pump_workflow_summary_page.tap(SampleMeteringPumpLocators.CANCEL_BUTTON)


@then(cfparse('User validates the "{expected_system_pressure_unit}" in the needle seal readiness test'))
def validate_needle_seal_pressure_unit(expected_system_pressure_unit,
                                       health_screen_page: HealthHomeScreen,
                                       needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen,
                                       needle_seal_readiness_workflow_summary_page: NeedleSealReadinessSummaryScreen):
    try:
        health_screen_page.validate_idle_state()
        health_screen_page.tap(HealthScreenLocators.NEEDLE_SEAL_READINESS_PANEL)
        needle_seal_readiness_workflow_setup_page.validate_welcome_screen()
        needle_seal_readiness_workflow_setup_page.tap_next_button()
        needle_seal_readiness_workflow_setup_page.validate_setup_screen()
        needle_seal_readiness_workflow_setup_page.tap_next_button()
        needle_seal_readiness_workflow_setup_page.validate_composition_screen()
        needle_seal_readiness_workflow_setup_page.tap_next_button()
        needle_seal_readiness_workflow_summary_page.validate_summary_screen()
        needle_seal_readiness_workflow_summary_page.wait_time_to_load_value(NeedleSealReadinessSummaryLocators.SYSTEM_PRESSURE_INFO_LABEL, "")

        actual_needle_seal_readiness_pressure_unit = needle_seal_readiness_workflow_summary_page.get_target_pressure_unit()
        assert expected_system_pressure_unit == actual_needle_seal_readiness_pressure_unit, f"The expected system settings pressure unit in the needle seal \
                readiness test is incorrect. Expected: [{expected_system_pressure_unit}]. Actual: [{actual_needle_seal_readiness_pressure_unit}]"
    finally:
        needle_seal_readiness_workflow_summary_page.tap(NeedleSealReadinessLocators.CANCEL_BUTTON)


@then(cfparse('User validates the "{expected_system_pressure_unit}" in the system settings'))
def validate_system_setting_pressure_unit(expected_system_pressure_unit,
                                          dashboard_screen_page: DashBoardScreen,
                                          system_settings_screen: SystemSettingsScreen,
                                          instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    try:
        dashboard_screen_page.tap_system()
        system_settings_screen.tap(SystemSettingsScreenLocators.CONFIGURATION_TAB)
        system_settings_screen.tap(InstrumentConfigurationScreenLocators.OPTIONS_PANEL)
        instrument_configuration_settings_screen_page.tap(InstrumentConfigurationScreenLocators.PRESSURE_UNITS)

        actual_instrument_configuration_pressure_unit = instrument_configuration_settings_screen_page.get_text(InstrumentConfigurationSettingsScreenLocators.\
                                                                                                               ACTIVE_PRESSURE_UNIT)
        assert expected_system_pressure_unit == actual_instrument_configuration_pressure_unit, f"The expected system settings pressure unit is incorrect. \
        Expected: [{expected_system_pressure_unit}]. Actual: [{actual_instrument_configuration_pressure_unit}]"
    finally:
        instrument_configuration_settings_screen_page.tap(InstrumentConfigurationSettingsScreenLocators.CANCEL_BUTTON)
        dashboard_screen_page.tap_home()
        dashboard_screen_page.tap_solvent_manager_schematic_icon()


@then(cfparse('User validates "{expected_system_pressure_unit}" in the solvent manager card reader'))
def validate_pressure_value_solvent_card(dashboard_screen_page: DashBoardScreen,
                                         expected_system_pressure_unit):
    dashboard_screen_page.validate_dashboard_screen()
    try:
        actual_system_pressure_unit = dashboard_screen_page.get_system_pressure_card_reader_unit()

        assert actual_system_pressure_unit == expected_system_pressure_unit, f"The expected system settings pressure unit on the \
        solvent manager card reader is incorrect. Expected: [{expected_system_pressure_unit}]. \
        Actual: [{actual_system_pressure_unit}]"
    finally:
        dashboard_screen_page.tap_solvent_manager_schematic_icon()


@when('User checks the currently selected unit')
def check_current_unit(system_pressure_setting_screen_page: SystemPressureSettingsScreen):
    assert system_pressure_setting_screen_page.find_active_unit()


@when('User confirms the unit change')
def tap_done_button(system_pressure_setting_screen_page: SystemPressureSettingsScreen):
    system_pressure_setting_screen_page.tap_done_button()


@when('User cancels the unit change')
def tap_cancel_button(system_pressure_setting_screen_page: SystemPressureSettingsScreen):
    system_pressure_setting_screen_page.tap_cancel_button()
