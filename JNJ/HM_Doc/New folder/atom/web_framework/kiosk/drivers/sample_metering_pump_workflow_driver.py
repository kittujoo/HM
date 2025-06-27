from utilities.logger import Logger

from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_metering_pump_constants import (
    SampleMeteringPumpConstants)
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_results_screen import SampleMeteringPumpResultsScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_screen import SampleMeteringPumpSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_summary_screen import SampleMeteringPumpSummaryScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_welcome_screen import SampleMeteringPumpWelcomeScreen
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import (
    SampleMeteringPumpLocators, SampleMeteringPumpSetupLocators, SampleMeteringPumpSummaryLocators)


class SampleMeteringPumpWorkflowDriver(object):

    def __init__(self, page_builder):
        self.sample_metering_welcome_page = page_builder(SampleMeteringPumpWelcomeScreen)
        self.sample_metering_setup = page_builder(SampleMeteringPumpSetupScreen)
        self.sample_metering_pump_workflow_summary_page = page_builder(SampleMeteringPumpSummaryScreen)
        self.sample_metering_pump_results_screen = page_builder(SampleMeteringPumpResultsScreen)
        self.logger = Logger(self.__class__.__name__)

    def start_sample_metering_pump_leak_test(self):
        self.sample_metering_welcome_page.validate_welcome_screen()
        self.sample_metering_welcome_page.tap_next_button()

        self.sample_metering_setup.validate_solvent_setup_screen()
        self.sample_metering_setup.tap_next_button()

        self.sample_metering_setup.validate_priming_setup_screen()

        self.sample_metering_setup.tap(SampleMeteringPumpSetupLocators.PRIME_TOGGLE)
        self.sample_metering_setup.tap_next_button()

        self.sample_metering_pump_workflow_summary_page.validate_summary_screen()
        self.sample_metering_pump_workflow_summary_page.tap(SampleMeteringPumpLocators.START_BUTTON)

    def validate_sample_metering_pump_leak_test_results(self):
        self.sample_metering_pump_workflow_summary_page.validate_element_wait_condition(
            SampleMeteringPumpSummaryLocators.IN_PROGRESS_BANNER, SampleMeteringPumpSummaryLocators.RESULTS_BANNER,
            SampleMeteringPumpConstants.SampleMeteringPumpPrimingWaitTime)
        self.sample_metering_pump_results_screen.validate_results_screen()
        self.sample_metering_pump_results_screen.tap_done_button()
