"""
File_Name: column_settings_screen.py
Desc: This file contains specific user action on the elements in the column setting screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 03/26/2020
__modified__ = "Sharmila Vairamani" changed the tap settings icon - 06/16/
__modified__ = "Sharmila vairamani" changed column1 to column- 09/03/2020
__modified__ = "Sharmila Vairamani" changed attribute for the toggle button element 10/20/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 12/17/2020
__modified__ = "Sharmila Vairmani" Added is_injection_edit_field_in_error_state function - 03/09/2021
"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.Home.ColumnManager.column_condition_card import ColumnSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class ColumnSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def tap_settings_icon(self):
        start_time = time.time()
        is_settings_icon_selected = None
        while time.time() - start_time < self.wait_time:
            self.tap(ColumnSettingsScreenLocators.SETTINGS_ICON)
            is_settings_icon_selected = self.is_settings_icon_selected()
            if is_settings_icon_selected:
                break
            time.sleep(.5)
        assert is_settings_icon_selected is True, f"Failed to select the settings icon "

    def is_settings_icon_selected(self):
        settings_icon_element = self.get_element(ColumnSettingsScreenLocators.SETTINGS_ICON)
        is_settings_icon_selected = settings_icon_element.get_attribute("ng-reflect-selected")
        is_settings_icon_selected = TypeConverter.to_bool(is_settings_icon_selected)
        return is_settings_icon_selected

    def select_column_position(self, column_position):

        column_position_text_dictionary = {
            "Column": ColumnSettingsScreenLocators.COLUMN_COLUMN_POSITION,
            "Bypass": ColumnSettingsScreenLocators.BYPASS_COLUMN_POSITION,
            "Waste": ColumnSettingsScreenLocators.WASTE_COLUMN_POSITION}

        if column_position in column_position_text_dictionary:
            locator = column_position_text_dictionary[column_position]
            self.tap_text_field(locator)

            return

        assert False, f"Unexpected column position => {column_position}"

    def is_injection_edit_field_component_exists(self):
        return self.is_displayed(ColumnSettingsScreenLocators.INJECTION_COUNT_ENTRY_FIELD)

    def get_column_position(self):
        column_position_info = self.get_text(ColumnSettingsScreenLocators.COLUMN_POSITION_INFO)
        return column_position_info

    def validate_column_settings_screen(self):
        locator = ColumnSettingsScreenLocators.MONITOR_INJECTION_COUNT_TAB
        screen_name = "column settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_monitor_injection_count_tab(self):
        self.tap_text_field(ColumnSettingsScreenLocators.MONITOR_INJECTION_COUNT_TAB)

    def is_toggle_button_enabled(self):
        toggle_button = self.get_element(ColumnSettingsScreenLocators.TOGGLE_BUTTON)
        is_toggle_button_on = toggle_button.get_attribute("ng-reflect-checked")
        self.logger.info(f" The value of toggle button {is_toggle_button_on}")
        is_toggle_button_on = TypeConverter.to_bool(is_toggle_button_on)
        return is_toggle_button_on

    def enter_maximum_injection(self, injection_count):
        self.enter_value(injection_count)

    def tap_toggle_button(self):
        self.tap(ColumnSettingsScreenLocators.TOGGLE_BUTTON)

    def is_injection_edit_field_in_error_state(self):
        return self.is_edit_field_in_error_state(ColumnSettingsScreenLocators.INJECTION_COUNT_EDIT_FIELD_STATE)

    def get_instruction_text(self):
        return [self.get_text(ColumnSettingsScreenLocators.INSTRUCTION_HEADER),
                self.get_text(ColumnSettingsScreenLocators.INSTRUCTION_ONE),
                self.get_text(ColumnSettingsScreenLocators.INSTRUCTION_TWO)
                ]
