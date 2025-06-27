from selenium.common.exceptions import StaleElementReferenceException

from web_framework.kiosk.pages.Common.temperature_condition_card_base import TemperatureConditionCardBase
from web_framework.kiosk.pages.Locators.Home.SampleManager.sm_home_screen import SampleManagerHomeScreenLocators


class SampleManagerHomeScreen(TemperatureConditionCardBase):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.previous_ambient_temperature = None

    def tap_second_page(self):
        self.tap(SampleManagerHomeScreenLocators.HOME_PAGE_TWO)

    def tap_sample_temperature_condition_card(self):
        self.tap(SampleManagerHomeScreenLocators.SAMPLE_TEMPERATURE_CONDITIONAL_CARD)

    def get_set_point(self) -> str:
        try:
            set_temperature = self.get_text(SampleManagerHomeScreenLocators.SETPOINT_LOCATOR)
        except StaleElementReferenceException:
            set_temperature = self.get_text(SampleManagerHomeScreenLocators.SETPOINT_LOCATOR)
        self.logger.info(set_temperature)
        set_temperature = set_temperature[:4]
        return set_temperature

    def get_setpoint_status(self) -> str:
        return self.get_text(SampleManagerHomeScreenLocators.SETPOINT_STATUS)

    def get_sample_temperature(self) -> float:
        try:
            return float(
                self.get_temperature(SampleManagerHomeScreenLocators.CURRENT_TEMPERATURE, SampleManagerHomeScreenLocators.CURRENT_TEMPERATURE_AFTER_DECIMAL))
        except StaleElementReferenceException:
            return float(
                self.get_temperature(SampleManagerHomeScreenLocators.CURRENT_TEMPERATURE, SampleManagerHomeScreenLocators.CURRENT_TEMPERATURE_AFTER_DECIMAL))

    def validate_sample_manager_home_screen(self):
        locator = SampleManagerHomeScreenLocators.SAMPLE_TEMPERATURE_CONDITIONAL_CARD
        screen_name = "sample manager home screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_injector_valve_position_card(self):
        locator = SampleManagerHomeScreenLocators.VALVE_POSITION_CONDITIONAL_CARD
        screen_name = "injector valve position"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_sample_pressure_condition_card(self):
        self.tap(SampleManagerHomeScreenLocators.SAMPLE_PRESSURE_CONDITIONAL_CARD)

    def get_valve_position_conditional_card(self) -> str:
        return self.get_container_text(SampleManagerHomeScreenLocators.DISPLAYED_VALVE_POSITION_CONDITIONAL_CARD)

    def tap_room_temperature_condition_card(self):
        self.tap(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_CONDITIONAL_CARD)

    def get_room_temperature_read_back_value(self) -> str:
        return self.get_text(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_READ_BACK_MESSAGE)

    def set_current_ambient_temperature(self, current_ambient_temperature):
        self.previous_ambient_temperature = current_ambient_temperature

    def get_ambient_temperature(self) -> str:
        return self.get_temperature(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_NUMBER_VALUE,
                                    SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_DECIMAL_VALUE)

    def validate_title_icon_color(self, locator_to_validate, expected_color_code):
        """
        This function validates the title icon color in the conditional card once the set point temperature is reached
        @return: void
        """
        property_name = "color"
        actual_final_title_icon_color_code = self.get_title_icon_color_code(locator_to_validate, property_name)
        expected_final_title_icon_color_code = expected_color_code
        assert expected_final_title_icon_color_code in actual_final_title_icon_color_code, f"Expected: {expected_final_title_icon_color_code}" \
                                                                                           f"Actual: {actual_final_title_icon_color_code}"
