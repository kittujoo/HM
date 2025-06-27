from web_framework.kiosk.pages.Locators.Setup.startup_workflow_locators import StartupSummaryLocators
from web_framework.kiosk.pages.base_page import BasePage


class StartupWorkflowSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

    def validate_startup_summary_screen(self):
        locator = StartupSummaryLocators.SUMMARY_PAGE_BANNER
        screen_name = "Summary screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_startup_cycle_screen(self):
        locator = StartupSummaryLocators.STARTUP_PROGRESS_BANNER
        screen_name = "Progress cycle screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)
