from selenium.common.exceptions import StaleElementReferenceException

from utilities.logger import Logger
from web_framework.kiosk.pages.Common.temperature_settings_screen_base import TemperatureSettingsScreenBase
from web_framework.kiosk.pages.Locators.Home.ColumnManager.cm_home_screen import ColumnManagerHomeScreenLocators
from web_framework.kiosk.pages.Locators.Home.ColumnManager.column_temperature_condition_card import ColumnTemperatureSettingScreenLocators


class ColumnTemperatureSettingsScreen(TemperatureSettingsScreenBase):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.locators_class = ColumnTemperatureSettingScreenLocators
        self.screen_name = "Column Temperature settings screen"

    def get_set_point(self) -> str:
        try:
            set_temperature = self.get_text(ColumnManagerHomeScreenLocators.SETPOINT_LOCATOR)
        except StaleElementReferenceException:
            set_temperature = self.get_text(ColumnManagerHomeScreenLocators.SETPOINT_LOCATOR)
        self.logger.info(set_temperature)
        set_temperature = set_temperature[:4]
        return set_temperature
