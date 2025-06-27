from selenium.common.exceptions import StaleElementReferenceException

from web_framework.kiosk.pages.Common.temperature_condition_card_base import TemperatureConditionCardBase
from web_framework.kiosk.pages.Locators.Home.ColumnManager.cm_home_screen import ColumnManagerHomeScreenLocators


class ColumnManagerHomeScreen(TemperatureConditionCardBase):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.locators_class = ColumnManagerHomeScreenLocators
        self.screen_name = "Column Manager home screen"

    def tap_column_temperature_condition_card(self):
        self.tap(ColumnManagerHomeScreenLocators.COLUMN_TEMPERATURE_CONDITIONAL_CARD)

    def tap_column_condition_card(self):
        self.tap(ColumnManagerHomeScreenLocators.COLUMN_CONDITIONAL_CARD)

    def validate_column_manager_home_screen(self):
        locator = ColumnManagerHomeScreenLocators.COLUMN_TEMPERATURE_CONDITIONAL_CARD
        screen_name = "home screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_column_temperature(self) -> float:
        try:
            return float(
                self.get_temperature(ColumnManagerHomeScreenLocators.CURRENT_TEMPERATURE, ColumnManagerHomeScreenLocators.CURRENT_TEMPERATURE_AFTER_DECIMAL))
        except StaleElementReferenceException:
            return float(
                self.get_temperature(ColumnManagerHomeScreenLocators.CURRENT_TEMPERATURE, ColumnManagerHomeScreenLocators.CURRENT_TEMPERATURE_AFTER_DECIMAL))

    def get_setpoint_status(self) -> str:
        return self.get_text(ColumnManagerHomeScreenLocators.SETPOINT_STATUS)

    def get_setpoint(self) -> str:
        try:
            setpoint_temperature = self.get_text(ColumnManagerHomeScreenLocators.SETPOINT_LOCATOR)
        except StaleElementReferenceException:
            setpoint_temperature = self.get_text(ColumnManagerHomeScreenLocators.SETPOINT_LOCATOR)
        setpoint_temperature = setpoint_temperature[:4]
        return setpoint_temperature
