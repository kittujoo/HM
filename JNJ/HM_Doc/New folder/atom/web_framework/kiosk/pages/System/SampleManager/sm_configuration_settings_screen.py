"""
file_Name: sm_configuration_settings_screen.py
Desc:This file contains specific user action on the elements in the sample manager configuration settings screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/11/2020
__modified__  ="Sharmila Vairamani" Refactor the validation function- 01/26/2021

"""
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from web_framework.kiosk.pages.base_page import BasePage
from web_framework.kiosk.pages.Locators.System.SampleManager.sm_configuration_settings_screen import OptionsTab, VolumeSettingsTab
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import state_dict


class SMConfigurationSettingsScreen(BasePage):

    def __init__(self, driver, base_url, assert_timeout: AssertTimeout, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.assert_timeout = assert_timeout


    def validate_sm_configuration_settings_screen(self, locator, screen_name):
        self.validate_screen(locator, screen_name, self.wait_time)


    def select_sm_configuration(self, configuration_option, configuration_option_locators_dict):
        if configuration_option in configuration_option_locators_dict:
            locator = configuration_option_locators_dict[configuration_option]
            self.tap(locator)
            return
        assert False, f"Unexpected configuration {configuration_option}"


    def validate_sm_configuration(self, configuration_options, configuration_option_locators_dict):
        if configuration_options in configuration_option_locators_dict:
            locator = configuration_option_locators_dict[configuration_options]
            return self.is_active(locator)
        assert False, f"Unexpected draw volume value => {configuration_options}"


    def get_current_sm_configuration_settings(self, configuration_option_locators_dict):
        for volume_locators in configuration_option_locators_dict.values():
            if self.is_active(volume_locators):
                return self.get_text(volume_locators)
        assert False, "No volume settings options is enabled"


    def switch_sm_config_setting_leak_sensor_toggle(self, toggle_state):
        locator = OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON
        current_toggle_status = self.is_toggle_component_enabled(locator)
        self.wait_till_condition_met(locator=OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS, expected_condition=state_dict[current_toggle_status],
                                     wait_time=self.wait_time,
                                     error_message="Expected condition not met for SM leak sensor toggle status")
        self.toggle_switch("SM configuration setting screen toggle", locator, current_toggle_status, toggle_state)
        self.wait_till_condition_met(locator=OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS, expected_condition=state_dict[toggle_state], wait_time=self.wait_time,
                                     error_message="Expected condition not met for SM leak sensor toggle status")


    def disable_extension_loop(self):
        locator = VolumeSettingsTab.EXTENSION_LOOP_TOGGLE
        if self.is_toggle_component_enabled(locator):
            self.tap(locator)
        else:
            self.logger.info("Extension loop toggle is already disabled")


    def wait_for_extension_loop_active(self):
        result = self.assert_timeout.wait_for_condition(lambda: self.is_active(VolumeSettingsTab.HUNDRED_MICRO_LITRE_OPTION),
                                                        timeout_in_seconds=self.long_wait_time, polling_period_in_seconds=1)
        assert result, f"Extension loop did not activate in the allotted time or got interrupted. Expected result: {not result}. Actual result: {result}"
