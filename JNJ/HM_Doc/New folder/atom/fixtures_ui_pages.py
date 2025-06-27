import os

import pytest

from utilities.logger import Logger
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_results_screen import NeedleSealReadinessResultsScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_screen import NeedleSealReadinessSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_summary_screen import NeedleSealReadinessSummaryScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_screen import SampleMeteringPumpSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_summary_screen import SampleMeteringPumpSummaryScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_setup_screen import SystemLeakTestSetupScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_summary_screen import SystemLeakTestSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Health.instrument_diagnostic_screen import InstrumentDiagnosticScreen
from web_framework.kiosk.pages.Home.ColumnManager.column_manager_home_screen import ColumnManagerHomeScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_pressure_settings_screen import SamplePressureSettingsScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_temperature_settings_screen import SampleTemperatureSettingsScreen
from web_framework.kiosk.pages.Home.SolventBottle.solvent_bottle_home_screen import SolventBottleHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.system_pressure_settings_screen import SystemPressureSettingsScreen
from web_framework.kiosk.pages.Home.TuvDetector.tuv_detector_home_screen import TUVDetectorHomeScreen
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.Maintain.ReplaceComponents.replace_components_screen import ReplaceComponentsScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen
from web_framework.kiosk.pages.Setup.setup_home_screen import SetupHomeScreen
from web_framework.kiosk.pages.System.About.about_screen import AboutScreen
from web_framework.kiosk.pages.Setup.startup_workflow_screen import StartupWorkflowSetupScreen
from web_framework.kiosk.pages.System.Administration.administration_screen import AdministrationScreen
from web_framework.kiosk.pages.System.ColumnManager.column_manager_configuration_screen import ColumnManagerConfigurationScreen
from web_framework.kiosk.pages.System.ColumnManager.column_manager_configuration_settings_screen import ColumnManagerConfigurationSettingsScreen
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import LeakSensorScreen
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen
from web_framework.kiosk.pages.System.Log.logs_settings_screen import LogSettingsScreen
from web_framework.kiosk.pages.System.SampleManager.sm_configuration_screen import SMConfigurationScreen
from web_framework.kiosk.pages.System.SampleManager.sm_configuration_settings_screen import SMConfigurationSettingsScreen
from web_framework.kiosk.pages.System.SolventManager.pump_module_configuration_screen import PumpModuleConfigurationScreen
from web_framework.kiosk.pages.System.SolventManager.pump_module_configuration_settings_screen import PumpModuleConfigurationSettingsScreen
from web_framework.kiosk.pages.System.TUVDetector.tuv_configuration_settings_screen import TUVConfigurationSettingsScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.instrument_configuration_settings_screen import InstrumentConfigurationSettingsScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen
from web_framework.kiosk.pages.lock_screen import LockScreen
from web_framework.kiosk.pages.sign_in_screen import SignInScreen

logger = Logger(os.path.basename(__file__))


@pytest.fixture
def lock_screen_page(page_builder):
    """
    Function scope fixture to construct the Lock screen page using the given function parameter (page_builder).
    :param page_builder: a fixture that gives a function to construct the page
    :return: LockScreenPage
    """
    lock_screen_page = page_builder(LockScreen)
    lock_screen_page.visit()
    # kiosk_lock_screen_page.wait_for_element_visibility(10, LockScreenPageLocators.swipe_to_unlock_component)
    return lock_screen_page


@pytest.fixture
def signin_screen_page(page_builder):
    page = page_builder(SignInScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def dash_board_screen_page(page_builder):
    """
    Function scope fixture to construct the Dashboard screen page using the given function parameter (page_builder).
    :param page_builder: a fixture that gives a function to construct the page
    :return: DashBoardScreenPage
    """
    logger.debug("From function_dash_board_screen_page fixture")
    dash_board_page = page_builder(DashBoardScreen)
    return dash_board_page


@pytest.fixture
def sample_pressure_setting_screen_page(page_builder):
    """
    Function scope fixture to construct the Sample Pressure Setting screen page
    using the given function parameter (page_retriever).
    :param page_builder: a fixture that gives a function to construct the page
    :return: SamplePressureSettingsScreen
    """
    page = page_builder(SamplePressureSettingsScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def sample_manager_home_screen_page(session_dash_board_screen_page, page_builder) -> SampleManagerHomeScreen:
    """
    Function scope fixture to construct the Sample Manager home screen page using
    the given function parameters (session_dash_board_screen_page and page_retriever).
    :param session_dash_board_screen_page: a fixture that gives a function to construct Session Dash Board screen page
    :param page_builder: a fixture that gives a function to construct the page
    :return: SampleManagerHomeScreen
    """
    session_dash_board_screen_page.tap_home()
    session_dash_board_screen_page.tap_sample_manager_schematic_icon()
    page = page_builder(SampleManagerHomeScreen)
    return page


@pytest.fixture
def sample_temperature_settings_screen_page(page_builder):
    """
    Function scope fixture to construct the Sample Temperature Settings screen page using
    the given function parameters (page_retriever).
    :param page_builder: a fixture that gives a function to construct the page
    :return: SampleTemperatureSettingsScreen
    """
    page = page_builder(SampleTemperatureSettingsScreen)
    return page


@pytest.fixture
def solvent_manager_home_screen_page(session_dash_board_screen_page, page_builder):
    """
    Function scope fixture to construct the Solvent Manager home screen page using the given
    function parameters (session_dash_board_screen_page and page_retriever).
    :param session_dash_board_screen_page: fixture that gives a function to construct Session Dash Board screen page
    :param page_builder: a fixture that gives a function to construct the page
    :return: SolventManagerHomeScreen
    """
    session_dash_board_screen_page.tap_home()
    session_dash_board_screen_page.tap_solvent_manager_schematic_icon()
    page = page_builder(SolventManagerHomeScreen)
    return page


@pytest.fixture
def system_pressure_setting_screen_page(page_builder):
    """
    Function scope fixture to construct the System Pressure Setting screen page using the given
    function parameters (page_retriever).
    :param page_builder: a fixture that gives a function to construct the page
    :return: SystemPressureSettingsScreen
    """
    page = page_builder(SystemPressureSettingsScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def session_kiosk_lock_screen_page(page_builder):
    """
    Session scope fixture to construct the Lock screen page using the given function parameter (page_retriever).
    :param page_builder:
    :return: LockScreenPage
    """
    kiosk_lock_screen_page = page_builder(LockScreen)
    # kiosk_lock_screen_page.visit()
    # kiosk_lock_screen_page.press_esc_key()
    # kiosk_lock_screen_page.wait_for_element_visibility(10, LockScreenPageLocators.swipe_to_unlock_component)
    return kiosk_lock_screen_page


# This is commented out as the sign in screen is not a part of the requirement
# PIN access to the App is no longer a requirement.
# Do not delete from code base, this screen will be used elsewhere in the App.
# @pytest.fixture(scope='session')
# def session_sign_in_screen(session_kiosk_lock_screen_page, page_retriever):
#     """
#     Session scope fixture to construct the SignIn screen page using the given lock screen page and
#             given function parameter (page_retriever).
#         :param session_kiosk_lock_screen_page: LockScreenPage
#         :param page_retriever: a fixture that gives a function to construct the page
#         :return: SignInScreenPage
#         """
#     session_kiosk_lock_screen_page.press_esc_key()
#     sign_in_page = page_retriever(SignInScreen)
#     sign_in_page.enter_pin("1234")
#     sign_in_page.tap_unlock_button()
#     logger.info("after getting sign_in_screen_page by calling page_builder fixture")
#     return sign_in_page


@pytest.fixture
def session_dash_board_screen_page(session_kiosk_lock_screen_page, page_builder):
    """
    Session scope fixture to construct the Dashboard screen page using the given SignIn screen page and
            given function parameter (page_retriever).
    :param session_kiosk_lock_screen_page:
    :param page_builder:
    :return: DashBoardScreenPage
    """
    logger.debug("From test_command_screen::command_screen_page")
    session_kiosk_lock_screen_page.press_esc_key()
    session_kiosk_lock_screen_page.wait_time_to_load_value(DashBoardsScreenPageLocators.LAMP_STATE)
    dash_board_page = page_builder(DashBoardScreen)
    dash_board_page.implicitly_wait()
    return dash_board_page


@pytest.fixture
def session_system_settings_screen_page(session_dash_board_screen_page, page_builder):
    """
    Session scope fixture to construct the system settings screen page using the given dashboard screen page and
            given function parameter (page_retriever).
    :param session_dash_board_screen_page:
    :param page_builder:
    :return: system_settings_page
    """
    logger.debug("From session_system_settings_screen_page fixture")
    session_dash_board_screen_page.tap_system()
    system_settings_page = page_builder(SystemSettingsScreen)
    return system_settings_page


@pytest.fixture
def system_settings_screen(session_dash_board_screen_page: DashBoardScreen, page_builder):
    page = page_builder(SystemSettingsScreen)
    return page


@pytest.fixture
def session_instrument_configuration_screen_page(session_system_settings_screen_page, page_builder):
    """
    Session scope fixture to construct the instrument configuration screen page using the given system settings screen page and
            given function parameter (page_retriever).
    :param session_system_settings_screen_page:
    :param page_builder:
    :return: instrument_configuration_page
    """
    logger.debug("From session_instrument_configuration_screen_page")
    session_system_settings_screen_page.tap_configuration_tab()
    instrument_configuration_page = page_builder(InstrumentConfigurationScreen)
    return instrument_configuration_page


@pytest.fixture
def instrument_configuration_screen(page_builder):
    page = page_builder(InstrumentConfigurationScreen)
    return page


@pytest.fixture
def leak_sensor_configuration_screen(page_builder):
    page = page_builder(LeakSensorScreen)
    return page


@pytest.fixture
def dashboard_screen_page(page_builder):
    page = page_builder(DashBoardScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def pump_module_configuration_settings_screen(page_builder):
    page = page_builder(PumpModuleConfigurationSettingsScreen)
    return page


@pytest.fixture
def pump_module_configuration_screen(page_builder):
    page = page_builder(PumpModuleConfigurationScreen)
    return page


@pytest.fixture
def sm_configuration_settings_screen_page(page_builder):
    page = page_builder(SMConfigurationSettingsScreen)
    return page


@pytest.fixture
def sm_module_config_screen(page_builder):
    page = page_builder(SMConfigurationScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def user_profile_hub_screen_page(page_builder):
    page = page_builder(UserProfileHubScreen)
    return page


@pytest.fixture
def user_profile_settings_screen_page(page_builder):
    page = page_builder(UserProfileSettingsScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def system_logs_screen(page_builder):
    page = page_builder(LogsScreen)
    return page


@pytest.fixture
def log_settings_screen(page_builder):
    page = page_builder(LogSettingsScreen)
    return page


@pytest.fixture
def flow_setting_screen_page(page_builder):
    """
    Function scope fixture to construct the Flow Setting screen page using the given function
    parameters (page_retriever).
    :param page_builder: a fixture that gives a function to construct the page
    :return: FlowSettingScreen
    """
    page = page_builder(FlowSettingsScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def tuv_detector_home_screen_page(page_builder):
    # tuv_detector_home_screen_page
    page = page_builder(TUVDetectorHomeScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def maintain_screen_page(session_dash_board_screen_page: DashBoardScreen, page_builder):
    session_dash_board_screen_page.tap_maintain()
    page = page_builder(MaintainScreen)
    return page


@pytest.fixture
def instrument_configuration_settings_screen_page(page_builder):
    page = page_builder(InstrumentConfigurationSettingsScreen)
    return page


@pytest.fixture
def health_screen_page(session_dash_board_screen_page: DashBoardScreen, page_builder):
    session_dash_board_screen_page.tap_diagnose()
    page = page_builder(HealthHomeScreen)
    return page


@pytest.fixture
def setup_screen_page(session_dash_board_screen_page: DashBoardScreen, page_builder):
    session_dash_board_screen_page.tap_setup()
    page = page_builder(SetupHomeScreen)
    return page


@pytest.fixture
def instrument_diagnostic_page(page_builder):
    page = page_builder(InstrumentDiagnosticScreen)
    return page


@pytest.fixture
def sample_metering_pump_workflow_setup_page(page_builder):
    page = page_builder(SampleMeteringPumpSetupScreen)
    return page


@pytest.fixture
def sample_metering_pump_workflow_summary_page(page_builder):
    page = page_builder(SampleMeteringPumpSummaryScreen)
    return page


@pytest.fixture
def leak_test_setup_screen_page(page_builder):
    page = page_builder(SystemLeakTestSetupScreen)
    return page


@pytest.fixture
def dynamic_leak_test_summary_screen_page(page_builder):
    page = page_builder(SystemLeakTestSummaryScreen)
    return page


@pytest.fixture
def needle_seal_readiness_workflow_setup_page(page_builder):
    page = page_builder(NeedleSealReadinessSetupScreen)
    return page


@pytest.fixture
def needle_seal_readiness_workflow_summary_page(page_builder):
    page = page_builder(NeedleSealReadinessSummaryScreen)
    return page


@pytest.fixture
def replace_components_hub_screen(page_builder):
    page = page_builder(ReplaceComponentsScreen)
    return page


@pytest.fixture
def column_manager_home_screen_page(dashboard_screen_page: DashBoardScreen, page_builder):
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_column_manager_schematic_icon()
    page = page_builder(ColumnManagerHomeScreen)
    return page


@pytest.fixture
def tuv_configuration_tuv_configuration_screen(page_builder):
    page = page_builder(TUVConfigurationSettingsScreen)
    return page


@pytest.fixture
def needle_test_result_page(page_builder):
    page = page_builder(NeedleSealReadinessResultsScreen)
    return page


@pytest.fixture
def command_screen_page(page_builder):
    page = page_builder(CommandsScreen)
    return page


@pytest.fixture
def column_manager_configuration_settings_screen(page_builder):
    page = page_builder(ColumnManagerConfigurationSettingsScreen)
    return page


@pytest.fixture
def column_manager_configuration_screen(page_builder):    
    page = page_builder(ColumnManagerConfigurationScreen)
    return page


@pytest.fixture
def about_screen(page_builder):
    page = page_builder(AboutScreen)
    return page


@pytest.fixture
def startup_workflow_setup_page(page_builder):
    page = page_builder(StartupWorkflowSetupScreen)
    return page


@pytest.fixture
def system_settings_screen(page_builder):
    page = page_builder(SystemSettingsScreen)
    return page


@pytest.fixture
def administration_configuration_screen(page_builder):
    page = page_builder(AdministrationScreen)
    return page

@pytest.fixture
def solvent_bottles_home_screen(page_builder):
    page = page_builder(SolventBottleHomeScreen)
    return page
