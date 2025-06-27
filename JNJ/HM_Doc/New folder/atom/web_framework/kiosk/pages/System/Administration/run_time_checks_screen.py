from web_framework.kiosk.pages.Locators.System.Administration.run_time_checks_screen_locators import RunTimeChecksScreenLocators
from web_framework.kiosk.pages.base_page import BasePage
from utilities.logger import Logger


class RunTimeChecksScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.wash_solvent_low_toggle = None
        self.mobile_phase_low_toggle = None
        self.logger = Logger(self.__class__.__name__)

    def validate_run_time_checks_screen(self):
        locator = RunTimeChecksScreenLocators.RUN_TIME_CHECKS_MENU
        screen_name = "Run Time Checks Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_run_time_checks_toggle_defaults(self):
        assert self.is_toggle_component_enabled(
            RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE) is True, "Mobile Phase Low toggle is not enabled by default"
        assert self.is_toggle_component_enabled(
            RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE) is True, "Wash Solvent Low toggle is not enabled by default"
        assert self.is_toggle_component_enabled(RunTimeChecksScreenLocators.LEAK_DETECTED_TOGGLE) is True, "Leak Detected toggle is not enabled by default"
        assert self.is_toggle_component_enabled(RunTimeChecksScreenLocators.VIAL_MISSING_TOGGLE) is True, "Vial Missing toggle is not enabled by default"

    def store_mobile_phase_state(self):
        self.mobile_phase_low_toggle = self.is_toggle_component_enabled(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE)
        return self.mobile_phase_low_toggle

    def store_wash_solvent_state(self):
        self.wash_solvent_low_toggle = self.is_toggle_component_enabled(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE)
        return self.wash_solvent_low_toggle

    def get_stored_mobile_phase_state(self):
        return self.mobile_phase_low_toggle

    def get_stored_wash_solvent_state(self):
        return self.wash_solvent_low_toggle
