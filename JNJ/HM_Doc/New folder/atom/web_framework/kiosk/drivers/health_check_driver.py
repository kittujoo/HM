from utilities.logger import Logger
from web_framework.kiosk.pages.Health.TUV.noise_drift_workflow_results_screen import NoiseDriftWorkflowResultsScreen
from web_framework.kiosk.pages.Health.TUV.noise_drift_workflow_screen import NoiseDriftWorkflowSetupScreen
from web_framework.kiosk.pages.Health.TUV.noise_drift_workflow_summary_screen import NoiseDriftWorkflowSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen

from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators


class HealthCheckDriver(object):

    def __init__(self, page_builder):
        self.health_screen_page = page_builder(HealthHomeScreen)
        self.noise_drift_workflow_page = page_builder(NoiseDriftWorkflowSetupScreen)
        self.noise_drift_workflow_summary_page = page_builder(NoiseDriftWorkflowSummaryScreen)
        self.noise_drift_workflow_result_page = page_builder(NoiseDriftWorkflowResultsScreen)

        self.logger = Logger(self.__class__.__name__)

    def open_sample_metering_pump_panel(self):
        self.health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)
        self.health_screen_page.tap(HealthScreenLocators.SAMPLE_MANAGER_ICON)
        self.health_screen_page.tap(HealthScreenLocators.SAMPLE_METERING_PUMP_PANEL)

    def validate_health_screen(self):
        self.health_screen_page.validate_health_screen()

    def execute_default_noise_drift_test(self):
        self.health_screen_page.tap_trouble_shoot_panel()
        self.noise_drift_workflow_page.tap(HealthScreenLocators.TUV_SECTION_ICON_NEW)
        self.noise_drift_workflow_page.validate_tuv_detector_screen()
        self.noise_drift_workflow_page.tap_noise_and_drift_test_button()
        self.noise_drift_workflow_page.validate_welcome_screen()
        self.noise_drift_workflow_page.tap_next_button()
        self.noise_drift_workflow_page.tap_next_button()
        self.noise_drift_workflow_page.tap_next_button()
        self.noise_drift_workflow_page.tap_next_button()
        self.noise_drift_workflow_page.tap_next_button()
        self.noise_drift_workflow_summary_page.validate_summary_screen()
        self.noise_drift_workflow_page.tap_start_button()

    def validate_noise_drift_result_screen(self):
        self.noise_drift_workflow_result_page.validate_results_screen()
        self.noise_drift_workflow_page.tap_done_button()
