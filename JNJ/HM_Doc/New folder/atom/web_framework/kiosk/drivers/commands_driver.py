"""
    File_Name: commands_driver.py
    Desc: This file contains driver specific actions on commands dashboard.
    __copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
    __author__    = "Imran Abbas Satti" Initial Check-in 03/19/2023

"""
import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import FlowControlTabScreen


class CommandsDriver(object):
    """
    Class to excecute commands workflow actions
    """

    def __init__(self, page_builder):
        self.command_screen_page = page_builder(CommandsScreen)
        self.flow_setting_screen_page = page_builder(FlowSettingsScreen)
        self.logger = Logger(self.__class__.__name__)

    def set_flow_state(self, state):
        """
        Driver to set solvent flow state.
        :param state: Solvent flow state.
        """
        self.command_screen_page.validate_command_screen()
        self.command_screen_page.tap_flow_control_card()
        self.flow_setting_screen_page.validate_flow_settings_screen()
        if state == True:
            self.flow_setting_screen_page.tap_flow_rate_button_on()
        else:
            self.flow_setting_screen_page.tap_flow_rate_button_off()

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
        time.sleep(5)

    def get_current_flow_rate_on_card(self):
        """
        Driver to get solvent flow rate on the flow state card.
        :return: string
        """
        return self.flow_setting_screen_page.wait_time_to_load_value(
            FlowControlTabScreen.FLOW_CARD_RATE_LOCATOR
        )

    def tap_done_button_on_flow_rate_page(self):
        """
        Driver to tap done button on the flow rate page.
        """
        self.flow_setting_screen_page.tap_done_button()
