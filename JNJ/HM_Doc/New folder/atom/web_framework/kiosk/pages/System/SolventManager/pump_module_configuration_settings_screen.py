"""
file_Name: pump_module_configuration_settings_screen.py
Desc:This file contains specific user action on the elements in the solvent manager configuration settings screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/3/2021
__modified__ = "Tyler Prada" added mixer config related methods
__modified__ = "Tyler Prada" adjusted methods based on mixer changes 1/25/22
__modified__ = "Tyler Prada" Updated methods due to UI changes 1/31/22
__modified__ = Tyler Prada" refactoring for pump module 1/4/23
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.SolventManager.pump_module_configuration_settings_screen import (PumpModuleConfigurationSettingsScreenLocators,
                                                                                                                FluidicChamberLightTabLocators,
                                                                                                                LeakDetectionTabLocators,
                                                                                                                MixerConfigurationTabLocators)
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.base_page import BasePage

toggle_dictionary = {
    "leak sensor": LeakDetectionTabLocators.LEAK_DETECTION_TOGGLE,
    "light when door is opened": FluidicChamberLightTabLocators.FLUIDIC_CHAMBER_LIGHT_TOGGLE
}
state_dict = {True: "No Leak", False: "Disabled"}


class PumpModuleConfigurationSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.previous_toggle_status = True

    def validate_pump_module_configuration_settings_screen(self):
        locator = PumpModuleConfigurationSettingsScreenLocators.SOLVENT_MANAGER_CONFIGURATION_SETTINGS_HEADER
        screen_name = "Solvent manager configuration settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)
        self.wait_time_to_load_value(LeakDetectionTabLocators.LEAK_DETECTION_STATE)

    def validate_fluidic_chamber_light_screen(self):
        return self.is_displayed(FluidicChamberLightTabLocators.FLUIDIC_CHAMBER_LABEL)

    def validate_leak_detection_screen(self):
        self.is_displayed(LeakDetectionTabLocators.LEAK_DETECTION_LABEL)

    def validate_mixer_configuration_screen(self):
        self.is_displayed(MixerConfigurationTabLocators.MIXER_VOLUME_LABEL)

    def validate_solvent_configuration_switch_saved(self, toggle):
        if toggle in toggle_dictionary:
            locator = toggle_dictionary[toggle]
            return self.previous_toggle_status != self.is_toggle_component_enabled(locator)

        assert False, f"Unexpected toggle component => {toggle}"

    def validate_solvent_configuration_switch_not_saved(self, toggle):
        if toggle in toggle_dictionary:
            locator = toggle_dictionary[toggle]
            return self.previous_toggle_status == self.is_toggle_component_enabled(locator)

        assert False, f"Unexpected toggle component => {toggle}"

    def get_solvent_configuration_switch_state(self, sensor):
        self.wait_time_to_load_value(LeakDetectionTabLocators.LEAK_DETECTION_STATE)
        if sensor in toggle_dictionary:
            locator = toggle_dictionary[sensor]
            return self.is_toggle_component_enabled(locator)

        assert False, f"Unexpected toggle component => {sensor}"

    def switch_solvent_toggle(self, toggle):
        if toggle in toggle_dictionary:
            locator = toggle_dictionary[toggle]
            current_toggle_status = self.is_toggle_component_enabled(locator)
            self.previous_toggle_status = current_toggle_status
            new_toggle_status = not current_toggle_status
            self.toggle_switch("Solvent configuration screen toggle", locator, current_toggle_status, new_toggle_status)
            return

        assert False, f"Unexpected toggle component => {toggle}"

    def switch_pump_leak_sensor_toggle_to_state(self, sensor_name, toggle_state):
        if sensor_name in toggle_dictionary:
            locator = toggle_dictionary[sensor_name]
            current_toggle_status = self.is_toggle_component_enabled(locator)
            self.wait_till_condition_met(locator=LeakDetectionTabLocators.LEAK_DETECTION_STATE, expected_condition=state_dict[current_toggle_status],
                                         wait_time=self.wait_time,
                                         error_message="Expected state not received")
            self.toggle_switch("Solvent configuration screen toggle", locator, current_toggle_status, toggle_state)
            self.wait_till_condition_met(locator=LeakDetectionTabLocators.LEAK_DETECTION_STATE, expected_condition=state_dict[toggle_state],
                                         wait_time=self.wait_time,
                                         error_message="Expected state not received")
            return

        assert False, f"Unexpected toggle component => {sensor_name}"

    def tap_done(self):
        self.tap_done_button()
        self.wait_till_element_is_invisible(BasePageLocators.DONE_BUTTON, self.long_wait_time)

    def tap_cancel(self):
        self.tap_cancel_button()

    def select_mixer_path(self, mixer_number):
        mixer_path_dictionary = {
            "1": MixerConfigurationTabLocators.PATH_ONE_MIXER,
            "2": MixerConfigurationTabLocators.PATH_TWO_MIXER
        }

        if mixer_number in mixer_path_dictionary:
            locator = mixer_path_dictionary[mixer_number]
            self.tap(locator)
            return

        assert False, (f"Unexpected mixer path => {mixer_number}")

    def select_mixer_option(self, mixer_option):
        mixer_option_dictionary = {
            "Custom": MixerConfigurationTabLocators.CUSTOM_MIXER_OPTION,
            "100MM": MixerConfigurationTabLocators.MIXER_OPTION_100MM,
            "50MM": MixerConfigurationTabLocators.MIXER_OPTION_50MM,
            "30MM": MixerConfigurationTabLocators.MIXER_OPTION_30MM,
            "None": MixerConfigurationTabLocators.MIXER_OPTION_NONE
        }

        if mixer_option in mixer_option_dictionary:
            locator = mixer_option_dictionary[mixer_option]
            self.scroll_to_view(locator)
            self.tap(locator)
            return

        assert False, (f"Unexpected mixer option => {mixer_option}")

    def get_mixer_value(self, mixer_number):
        mixer_field_dictionary = {
            "1": MixerConfigurationTabLocators.PATH_ONE_FIELD,
            "2": MixerConfigurationTabLocators.PATH_TWO_FIELD
        }

        if mixer_number in mixer_field_dictionary:
            locator = mixer_field_dictionary[mixer_number]
            self.wait_for_element_visibility(self.wait_time, locator)
            return self.get_user_input_text(locator)

        assert False, f"Unexpected mixer path => {mixer_number}"

    def enter_mixer_value(self, mixer_value):
        self.tap(MixerConfigurationTabLocators.CUSTOM_MIXER_FIELD)
        self.clear_num_pad_entries(MixerConfigurationTabLocators.CUSTOM_MIXER_FIELD)
        self.enter_value(mixer_value)
        return

    def validate_done_button_inactive(self):
        done_button = self.get_element(PumpModuleConfigurationSettingsScreenLocators.DONE_BUTTON_LABEL)
        done_button_state = done_button.get_attribute("ng-reflect-available")
        active_element_state = done_button_state.find("false")
        self.logger.info(f"The done_button_state==>>{done_button_state} ")

        if active_element_state != -1:
            return True
        return False
