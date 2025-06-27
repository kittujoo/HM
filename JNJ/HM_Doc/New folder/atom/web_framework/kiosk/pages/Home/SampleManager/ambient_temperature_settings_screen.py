from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.condition_card_constants import AmbientTemperatureConditionCardConstants
from web_framework.kiosk.pages.Locators.Home.SampleManager.ambient_temperature_condition_card import AmbientTemperatureSettingScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class AmbientTemperatureSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_room_temperature_settings_screen(self):
        locator = AmbientTemperatureSettingScreenLocators.HEADER
        screen_name = "Room temperature settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def is_target_edit_field_in_error_state(self):
        return self.is_edit_field_in_error_state(AmbientTemperatureSettingScreenLocators.TEMPERATURE_EDIT_FIELD_STATE)

    def is_tolerance_edit_field_in_error_state(self):
        return self.is_edit_field_in_error_state(AmbientTemperatureSettingScreenLocators.TEMPERATURE_TOLERANCE_EDIT_FIELD_STATE)

    def validate_display_info(self, expected_ambient_temp, expected_temp_range):
        display_info = self.get_text(AmbientTemperatureSettingScreenLocators.AMBIENT_TEMPERATURE_INFO)
        self.logger.info(f"display_info ====>>{display_info}")
        actual_ambient_temperature = display_info[:4]
        self.logger.info(f"actual_ambient_temperature ====>>{actual_ambient_temperature}")
        actual_temperature_range = display_info[7:11]
        self.logger.info(f"actual_temperature_range ====>>{actual_temperature_range}")
        actual_unit = display_info[11:]
        self.logger.info(f"actual_unit ====>>{actual_unit}")
        actual_ambient_temperature == expected_ambient_temp
        actual_temperature_range == expected_temp_range
        actual_unit = AmbientTemperatureConditionCardConstants.TemperatureUnits
