from web_framework.kiosk.pages.Locators.System.Administration.pre_run_checks_screen_locators import PreRunChecksScreenLocators
from web_framework.kiosk.pages.base_page import BasePage
from utilities.logger import Logger


class PreRunChecksScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    toggle_dictionary = {
        "eConnected Column must be installed": PreRunChecksScreenLocators.COLUMN_INSTALLED_TOGGLE,
        "eConnected Column must match method": PreRunChecksScreenLocators.COLUMN_MATCHES_TOGGLE,
        "No pending performance maintenance": PreRunChecksScreenLocators.PERFORMANCE_MAINTENANCE_TOGGLE,
        "System is qualified": PreRunChecksScreenLocators.SYSTEM_QUALIFIED_TOGGLE,
        "Mobile phase is not expired": PreRunChecksScreenLocators.MOBILE_PHASE_EXPIRED_TOGGLE,
        "Sample Plates must be installed": PreRunChecksScreenLocators.SAMPLE_PLATES_INSTALLED_TOGGLE,
        "Sample Plates must match method": PreRunChecksScreenLocators.SAMPLE_PLATES_MATCH_TOGGLE,
        "All vials present": PreRunChecksScreenLocators.VIALS_PRESENT_TOGGLE
    }

    def validate_pre_run_checks_screen(self):
        locator = PreRunChecksScreenLocators.PRE_RUN_CHECKS_MENU
        screen_name = "Pre Run Checks Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def toggle_locator_selector(self, toggle):

        if toggle in self.toggle_dictionary:
            locator = self.toggle_dictionary[toggle]
            return locator

        assert False, f"Unexpected toggle component => {toggle}"

    def set_all_toggle_buttons(self, toggle_status):

        for toggle in self.toggle_dictionary.values():
            self.set_toggle_button(toggle, toggle_status)

    def validate_all_toggle_buttons_enabled(self):

        for toggle in self.toggle_dictionary.values():
            actual_toggle_status = self.is_toggle_component_enabled(toggle)
            assert actual_toggle_status is True, f"Expected toggle status: True, Actual toggle status: {actual_toggle_status}"
