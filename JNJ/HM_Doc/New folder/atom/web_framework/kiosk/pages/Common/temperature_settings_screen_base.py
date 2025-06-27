"""
File_Name: temperature_settings_screen_base.py
Desc: This file contains common user specific function on any temperature settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 03/29/2021
__author__ = "Sharmila Vairamani" Added assertion for tap_toggle_button_off  and tap_toggle_button_on - 04/08/2021
__author__ = "sharmila Vairamani " Updated the toggle button locator - 04/09/2021

"""

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.base_page import BasePage


class TemperatureSettingsScreenBase(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.locators_class = None

    def tap_toggle_button_off(self):
        is_toggle_button_enabled = self.is_toggle_button_enabled()

        if not is_toggle_button_enabled:
            self.logger.info("*** Toggle button is not enabled")

        else:
            self.logger.info("*** Toggle button is enabled")
            self.tap_toggle_button()

    def tap_toggle_button_on(self):
        is_toggle_button_enabled = self.is_toggle_button_enabled()

        if not is_toggle_button_enabled:
            self.logger.info("*** Toggle button is not enabled")
            self.tap_toggle_button()

        else:
            self.logger.info("*** Toggle button is enabled")
        assert self.is_toggle_button_enabled(), 'Toggle button is switched off'

    def tap_toggle_button(self):
        self.tap(self.locators_class.TOGGLE_BUTTON_ACTION)

    def enter_temperature(self, temperature):
        self.enter_value(temperature)

    def is_toggle_button_enabled(self):
        toggle_button = self.get_element(self.locators_class.TOGGLE_BUTTON)
        is_toggle_button_on = toggle_button.get_attribute("ng-reflect-checked")
        is_toggle_button_on = TypeConverter.to_bool(is_toggle_button_on)
        return is_toggle_button_on

    def is_toggle_button_displayed(self):
        return self.is_displayed(self.locators_class.TOGGLE_BUTTON)

    def validate_column_temperature_settings_screen(self):
        locator = self.locators_class.HEADER
        # wait_time = 10
        screen_name = "column temperature settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_entered_value(self):
        edit_field_component = self.get_element(self.locators_class.TEMPERATURE_EDIT_FIELD_COMPONENT)
        get_edit_field_value = edit_field_component.get_attribute("ng-reflect-value")
        return get_edit_field_value

    def validate_temperature_setpoint_header(self):
        locator = self.locators_class.SETPOINT_TEMPERATURE_HEADER
        self.validate_screen(locator, self.screen_name, self.wait_time)
