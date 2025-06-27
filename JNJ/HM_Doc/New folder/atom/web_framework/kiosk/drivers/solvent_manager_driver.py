"""
    Filename: solvent_manager_driver.py
    Driver to control Solvent Manager screen actions
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.system_pressure_settings_screen import SystemPressureSettingsScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import FlowControlTabScreen


class SolventManagerDriver(object):
    """
    Class to control Solvent Manager screen actions
    """

    def __init__(self, page_builder):
        self.solvent_manager_home_screen_page = page_builder(SolventManagerHomeScreen)
        self.system_pressure_setting_screen_page = page_builder(SystemPressureSettingsScreen)
        self.flow_setting_screen_page = page_builder(FlowSettingsScreen)
        self.logger = Logger(self.__class__.__name__)

    def set_unit(self, unit):
        """
        Driver to set solvent pressure unit.
        :param unit: Solvent pressure unit
        """
        self.solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
        self.solvent_manager_home_screen_page.tap_system_pressure_condition_card()
        self.system_pressure_setting_screen_page.validate_system_pressure_settings_screen()
        self.system_pressure_setting_screen_page.select_unit_option(unit)
        self.system_pressure_setting_screen_page.tap_done_button()

    def check_unit(self):
        """
        Driver to check solvent pressure unit.
        :return: Solvent pressure unit
        """
        return self.solvent_manager_home_screen_page.get_system_pressure_unit()

    def set_flow_state(self, state):
        """
        Driver to set solvent flow state.
        :param state: Solvent flow state. True to turn solvent flow On, False to turn solvent flow Off
        """
        self.solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
        self.solvent_manager_home_screen_page.tap_flow_condition_card()
        if state:
            # The line below is needed because by default toggle is on
            # but the panel to enter flow rate is not displayed
            self.flow_setting_screen_page.tap_flow_rate_button_off()
            self.flow_setting_screen_page.tap_flow_rate_button_on()
        else:
            self.flow_setting_screen_page.tap_flow_rate_button_off()
        time.sleep(1)

    def set_flow_rate(self, rate):
        """
        Driver to set solvent flow rate.
        :param rate: Solvent flow rate.
        """
        self.flow_setting_screen_page.wait_time_to_load_value(FlowControlTabScreen.FLOW_RATE_EDIT_FIELD)
        self.flow_setting_screen_page.tap(FlowControlTabScreen.FLOW_RATE_EDIT_FIELD)
        self.flow_setting_screen_page.clear_num_pad_entries(FlowControlTabScreen.FLOW_RATE_EDIT_FIELD)
        self.flow_setting_screen_page.enter_flow_rate(rate)
        self.tap_done_button_on_flow_rate_page()

    def tap_done_button_on_flow_rate_page(self):
        """
        Driver to tap done button on the flow rate page.
        """
        self.flow_setting_screen_page.tap_done_button()
        time.sleep(5)
