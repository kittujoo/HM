"""
File_Name: commands_screen.py
Desc: This file contains specific user action on the web elements in the commands screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/15/2020
__modified__ = "Sharmila Vairamani" Changed the logging implementation - 04/27/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
__modified__ = "Sharmila Vairamani" Added turn_lamp_off and check_lamp_off functions - 05/10/2021
__modified__ "Sharmila Vairamani" Added get_current_lamp_state - 05/20/2021
__modified__ "Sharmila Vairamani" Added LampWarmingTime constant -06/04/2021
__modified__ "Tyler Prada" Added is_flow_active, hold_autozero, and hold_reset 7/2/21
__modified__ "Tyler Prada" Made prime seal common validate method 7/16/21
__modified__ = "Tyler Prada" added validate system_state_transition 9/10/2021
__modified__ = "Sharmila Vairamani" Added tap_leak_test_panel 09/21/2021
__modified__ = "Tyler Prada" Adjustments for leak test moving to health screen 2/21/22
__modified__ = "Sharmila Vairamani" Added tap_home function 04/06/2022
__modified__ = "Sharmila Vairmaani" Update the script to new command card implememntations - 10/21/2022
__modified__ = "Sharmila Vairamani" Removed tap_and_hold function - 02/27/2023

"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.commands import CommandsConstants
from web_framework.kiosk.common.Constants.dashboard_constants import SystemStateConstants
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.commands_screen_locators import CommandsScreenPageLocators
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.base_page import BasePage

logger = Logger("commands_screen_page")


class CommandsScreen(BasePage):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 300
        self.current_lamp_state = True

    def validate_command_screen(self):
        locator = CommandsScreenPageLocators.COMMAND_FLY_MENU
        screen_name = "command screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def turn_on_lamp(self):
        self.logger.info(f"lAMP IS TURNING ON")
        locator = CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT
        lamp_action_text = self.wait_time_to_load_value(locator)

        if lamp_action_text == CommandsConstants.TurnOnCommandActionText:
            self.wait_time_to_load_value(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT, self.wait_time)
            self.tap(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON)
            self.wait_till_element_is_invisible(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON, self.wait_time)
            self.tap(DashBoardsScreenPageLocators.COMMANDS)

            # NOTE: Warming process may fail since it is quick to turn on within simulation
            expected_condition = CommandsConstants.LampWarmReadBackMessage
            error_message = "The lamp is not in warming state"
            self.wait_till_condition_met(locator, expected_condition, error_message, CommandsConstants.LampWarmingTime)

            expected_condition = CommandsConstants.LampOnReadBackMessage
            error_message = "The lamp did not turn on"
            self.wait_till_condition_met(locator, expected_condition, error_message, CommandsConstants.LampWarmingTime)

            start_time = time.time()
            while time.time() - start_time < self.wait_time:
                locator = CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT
                transition_action_text = self.get_text(locator)
                if transition_action_text == CommandsConstants.LampOnReadBackMessage:
                    break
                time.sleep(1)
            assert transition_action_text == CommandsConstants.LampOnReadBackMessage, f"transition_action_text= {transition_action_text}"

    def turn_off_lamp(self):
        self.logger.info(f"lAMP IS TURNING OFF")
        locator = CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT

        lamp_action_text = self.wait_time_to_load_value(locator)

        if lamp_action_text == CommandsConstants.LampOnReadBackMessage or lamp_action_text == CommandsConstants.LampWarmReadBackMessage:
            self.wait_time_to_load_value(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT, self.wait_time)
            self.tap(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON)
            self.wait_till_element_is_invisible(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON, self.wait_time)
            self.tap(DashBoardsScreenPageLocators.COMMANDS)

            start_time = time.time()
            while time.time() - start_time < self.wait_time:
                locator = CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT
                transition_action_text = self.get_text(locator)
                if transition_action_text == CommandsConstants.LampOffReadBackMessage:
                    break
                time.sleep(1)
            assert transition_action_text == CommandsConstants.LampOffReadBackMessage, f"transition_action_text= {transition_action_text}"

    def select_lamp(self, lamp_request):
        lamp_request = lamp_request.lower()
        if lamp_request == CommandsConstants.LampOnRequest:
            self.turn_on_lamp()
        elif lamp_request == CommandsConstants.LampOffRequest:
            self.turn_off_lamp()

    def start_emergency_stop(self):
        self.logger.info(f"Emergency stop starts")
        locator = CommandsScreenPageLocators.STOP_TEXT
        stop_action_text = self.wait_time_to_load_value(locator)

        if stop_action_text == CommandsConstants.EmergencyStopText:
            self.tap(CommandsScreenPageLocators.STOP_SYSTEM)

            start_time = time.time()
            while time.time() - start_time < self.wait_time:
                locator = BasePageLocators.MACHINE_STATE
                system_state_text = self.get_text(locator)
                if system_state_text == SystemStateConstants.HaltedSystemState:
                    break
                time.sleep(1)
            assert system_state_text == SystemStateConstants.HaltedSystemState, f"system_state_text= {system_state_text}"

    def hold_reset(self):
        self.logger.info(f"System reset starts")
        locator = CommandsScreenPageLocators.RESET_TEXT
        reset_action_text = self.wait_time_to_load_value(locator)

        if reset_action_text == CommandsConstants.ResetText:
            self.tap(CommandsScreenPageLocators.RESET_SYSTEM)

            reset_action_text = self.get_text(locator)
            logger.info(f" The text displayed after the tap  on the icon {reset_action_text}")
            assert reset_action_text == CommandsConstants.HoldToResetText

            self.tap(CommandsScreenPageLocators.RESET_SYSTEM_BUTTON)

            expected_condition = CommandsConstants.ResetTransitionText
            error_message = "The reset is not initiated"
            self.wait_till_condition_met(locator, expected_condition, error_message, self.wait_time)

            expected_condition = CommandsConstants.ResetText
            error_message = "The system does not reset"
            self.wait_till_condition_met(locator, expected_condition, error_message, self.wait_time)

    def tap_reset(self):
        self.tap(CommandsScreenPageLocators.RESET_SYSTEM)

    def turn_flow_on(self):
        self.logger.info(f"Turning the flow ON")
        locator_state = CommandsScreenPageLocators.FLOW_COMMAND_BUTTON_TEXT
        flow_action_text = self.wait_time_to_load_value(locator_state)
        self.logger.info(f"flow_action_text ===>>> {flow_action_text}")

        if flow_action_text == CommandsConstants.FlowTurnOnCommandActionText:
            self.logger.info(f"flow_action_text====>>>>>>{CommandsConstants.FlowTurnOnCommandActionText}")

            self.tap(CommandsScreenPageLocators.FLOW_COMMAND_BUTTON)
            time.sleep(10)
            self.tap(DashBoardsScreenPageLocators.COMMANDS)

            expected_condition = CommandsConstants.FlowRateUnit
            error_message = "The flow is not initiated"
            actual_condition = self.get_text(CommandsScreenPageLocators.FLOW_RATE_UNITS)

            self.logger.info(f"actual_condition ===>>> {actual_condition}")

            actual_condition = actual_condition[-6:]
            self.logger.info(f"actual_condition_trim====>>>>>>{actual_condition}")
            self.validate_condition(actual_condition, expected_condition, error_message, self.wait_time)
            current_flow_rate = self.get_text(CommandsScreenPageLocators.FLOWRATE_INFO)
            current_flow_rate = TypeConverter.to_float(current_flow_rate)
            assert CommandsConstants.MinFlowRate <= current_flow_rate <= CommandsConstants.MaxFlowRate, f" current_flow_rate ==>>>{current_flow_rate}"

    def turn_flow_off(self):
        self.logger.info(f"Turning the flow OFF")
        locator_state = CommandsScreenPageLocators.FLOW_RATE_UNITS

        flow_action_text = self.wait_time_to_load_value(locator_state)
        self.logger.info(f"flow_action_text====>>>>>>{flow_action_text}")

        if flow_action_text == CommandsConstants.FlowRateUnit:
            self.logger.info(f"transition_action_text before  tapping the button====>>>>>>{CommandsConstants.FlowTurnOnCommandActionText}")
            self.tap(CommandsScreenPageLocators.FLOW_COMMAND_BUTTON)
            # animation for fly-out menu & flow shut-off
            time.sleep(3)
            self.tap(DashBoardsScreenPageLocators.COMMANDS)

            start_time = time.time()
            while time.time() - start_time < self.wait_time:
                self.logger.info("The first while loop")
                locator = CommandsScreenPageLocators.FLOW_COMMAND_BUTTON_TEXT
                transition_action_text = self.get_text(locator)
                self.logger.info(f"transition_action_text ===>>> {transition_action_text}")
                # current_flow_rate = self.get_text(CommandsScreenPageLocators.FLOWRATE_INFO)
                # current_flow_rate = TypeConverter.to_float(current_flow_rate)
                # self.logger.info(f"transition_action_text====>>>>>>{transition_action_text}")
                # self.logger.info(f"current_flow_rate====>>>>>>{current_flow_rate}")
                if transition_action_text == CommandsConstants.FlowTurnOnCommandActionText:
                    break
                time.sleep(1)
            assert transition_action_text == CommandsConstants.FlowTurnOnCommandActionText, f"transition_action_text= {transition_action_text}"

    def select_flow(self, flow_request):
        flow_request = flow_request.lower()
        if flow_request == CommandsConstants.FlowOnRequest:
            self.turn_flow_on()
        elif flow_request == CommandsConstants.FlowOffRequest:
            self.turn_flow_off()

    def validate_flow_control(self, flow_control):
        locator = CommandsScreenPageLocators.FLOW_COMMAND_BUTTON_TEXT
        flow_action_text = self.get_text(locator)
        flow_action_text = flow_action_text.lower()
        flow_control = flow_control.lower()
        if flow_control == CommandsConstants.FlowOnRequest:
            assert flow_action_text != CommandsConstants.FlowOffRequest, f"Flow control is off when flow control should be {flow_control}"
        else:
            assert flow_action_text == CommandsConstants.FlowOffRequest, f"Flow control is on when flow control should be {flow_control}"

    def tap_flow_control_card(self):
        self.tap(CommandsScreenPageLocators.FLOW_COMMAND_BUTTON_TEXT)

    def tap_on_commands_card(self):
        self.tap(CommandsScreenPageLocators.COMMAND_FLY_MENU)

    def Validate_state_busy_state(self):
        current_state = self.get_text(BasePageLocators.MACHINE_STATE)
        self.logger.info(f"The current_state state is ==>>>{current_state}")
        expected_state = SystemStateConstants.BusySystemState
        self.logger.info(f"The expected_state state is ==>>>{expected_state}")
