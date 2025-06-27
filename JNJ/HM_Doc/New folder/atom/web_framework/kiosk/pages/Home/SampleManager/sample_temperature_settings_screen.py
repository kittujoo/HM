from web_framework.kiosk.pages.Common.temperature_settings_screen_base import TemperatureSettingsScreenBase
from web_framework.kiosk.pages.Locators.Home.SampleManager.sample_temperature_condition_card import SampleTemperatureSettingScreenLocators


class SampleTemperatureSettingsScreen(TemperatureSettingsScreenBase):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.locators_class = SampleTemperatureSettingScreenLocators
        self.screen_name = "Sample Temperature settings screen"

    def validate_sample_temperature_settings_screen(self):
        locator = SampleTemperatureSettingScreenLocators.HEADER
        self.validate_screen(locator, self.screen_name, self.wait_time)

    def get_set_temperature(self):
        set_temperature_with_units = self.get_text(SampleTemperatureSettingScreenLocators.SET_TEMPERATURE_READ_BACK_MESSAGE)
        set_temperature = set_temperature_with_units[:4]
        return set_temperature
