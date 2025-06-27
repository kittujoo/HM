from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.System.PerformanceCounters.performance_counters_screen import PerformanceCounterScreenLocators
from web_framework.kiosk.pages.base_page import BasePage
from utilities.logger import Logger


class PerformanceCountersScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_performance_counters_screen(self):
        locator = PerformanceCounterScreenLocators.PERFORMANCE_COUNTERS_HEADER
        screen_name = "Performance Counters screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_more_options_button(self):
        self.tap(PerformanceCounterScreenLocators.MORE_OPTIONS_BUTTON)

    def tap_reset_button(self):
        self.tap(PerformanceCounterScreenLocators.RESET_BUTTON)

    def tap_reset_confirm_button(self):
        self.tap(PerformanceCounterScreenLocators.RESET_CONFIRM_BUTTON)

    def tap_performance_counter_back_button(self):
        self.tap(PerformanceCounterScreenLocators.BACK_BUTTON)

    def get_lamp_progress_bar(self):
        lamp_hours_progress_bar = self.get_element(PerformanceCounterScreenLocators.LAMP_PROGRESS_BAR)
        lamp_hours_progress_bar = lamp_hours_progress_bar.get_attribute("style")
        lamp_hours_progress_bar = lamp_hours_progress_bar[6:-2].strip()
        lamp_hours_progress_bar = TypeConverter.to_float(lamp_hours_progress_bar)
        return lamp_hours_progress_bar
