"""
File_Name: input_stepper_handler.py
Desc: This file contains the common shared code related to input stepper actions across all the pages
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in - 10/8/2021
__modified__ = "Tyler Prada" adjustements for new kiosk_utilities class 11/1/21
__modified__ = "Tyler Prada" fixed numeric stepper error (wrong method call) 11/9/21
__modified__ = "Tyler Prada" updated time stepper to take 30sec and 60sec units 9/21/22
__modified__ = "Tyler Prada" updated time stepper to take 15sec units 12/6/22
__modified__ = "Tyler Prada" Fixed unit value bug 2/23/23
"""

import time
from datetime import datetime

from utilities import logger
from utilities.logger import Logger
from web_framework.kiosk.pages.Handlers.web_elements_handler import WebElementsHandler
from web_framework.kiosk.pages.Handlers.touch_actions_handler import TouchActionsHandler
from web_framework.kiosk.pages.Utilities.kiosk_utilities import KioskUtilities


class InputStepperHandler:
    """
        Input stepper handler class that contains
            common shared code across all the pages
    """

    def __init__(self, driver):
        super().__init__()
        self.logger = Logger(self.__class__.__name__)
        self._driver = driver

    def set_time_stepper(self, stepper_locator, unit_value, desired_value):
        """
        This method is to handle the time stepper component to get it to a given/desired value
        NOTE: Currently only works for time steppers using the 30sec and 60sec units
        NOTE: When using steppers with 15sec intervals, use 1minute changes in examples
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param unit_value: the value of the stepper buttons ex: 15, 30, 60 (corresponding to seconds)
        @param desired_value: the desired time value ex: 05:30
        @return: void
        """
        unit_value = int(unit_value)
        stepper_field_locator = KioskUtilities.add_xpath_to_locator(self._driver, stepper_locator, "//input[@type='text']")
        current_stepper_value = WebElementsHandler.get_entered_value(self._driver, stepper_field_locator)
        current_stepper_value = current_stepper_value.replace(" ", "")

        self.logger.info(current_stepper_value)
        tap_amount = 0
        if desired_value == "60:00":
            desired_value = "59:30"
            tap_amount += 2
        desired_value_time = datetime.strptime(desired_value, '%M:%S')
        current_stepper_value_time = datetime.strptime(current_stepper_value, '%M:%S')

        # -- increment condition -- #
        if current_stepper_value_time.minute < desired_value_time.minute:
            difference = desired_value_time.minute - current_stepper_value_time.minute

            if unit_value == 15:
                tap_amount = difference * 4 + tap_amount
            if unit_value == 30:
                tap_amount = difference * 2 + tap_amount
            if unit_value == 60:
                tap_amount = difference + tap_amount

            if current_stepper_value_time.second < desired_value_time.second:
                tap_amount = tap_amount + 1
            self.stepper_increment(stepper_locator, tap_amount)
            return

        # -- decrement condition -- #
        if current_stepper_value_time.minute > desired_value_time.minute:
            difference = current_stepper_value_time.minute - desired_value_time.minute

            if unit_value == 15:
                tap_amount = difference * 4
            if unit_value == 30:
                tap_amount = difference * 2
            if unit_value == 60:
                tap_amount = difference

            if current_stepper_value_time.second < desired_value_time.second:
                tap_amount = tap_amount - 1
            self.stepper_decrement(stepper_locator, tap_amount)
            return

    def set_numeric_stepper(self, stepper_locator, desired_value):
        """
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param desired_value: the desired numeric value ex: 25
        @return: void
        """
        stepper_field_locator = KioskUtilities.add_xpath_to_locator(self._driver, stepper_locator, "//input[@type='text']")
        current_stepper_value = int(WebElementsHandler.get_entered_value(self._driver, stepper_field_locator))
        desired_value = int(desired_value)

        # -- increment condition -- #
        if current_stepper_value < desired_value:
            tap_amount = int((desired_value - current_stepper_value)/5)
            self.stepper_increment(stepper_locator, tap_amount)
            return

        # -- decrement condition -- #
        if current_stepper_value > desired_value:
            tap_amount = int((current_stepper_value - desired_value)/5)
            self.stepper_decrement(stepper_locator, tap_amount)
            return

    # TODO: Create the input stepper method for the float variant of the component. Currently not implemented in the KIOSK 10/4/21
    def set_float_stepper(self):
        logger.debug("")

    def stepper_increment(self, stepper_locator, tap_amount):
        """
        This method taps on the stepper component's increment button to increase value
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param tap_amount: numerical value that determines the tap() execution times
        @return: void
        """
        increment_locator = KioskUtilities.add_xpath_to_locator(self._driver, stepper_locator,
                                                                "//div[contains(@class,'input-stepper-increment')]")
        for _ in range(tap_amount):
            TouchActionsHandler.tap(self._driver, increment_locator)
            time.sleep(1)

    def stepper_decrement(self, stepper_locator, tap_amount):
        """
        This method taps on the stepper component's decrement button to decrease value
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @param tap_amount: numerical value that determines the tap() execution times
        @return: void
        """
        decrement_locator = KioskUtilities.add_xpath_to_locator(self._driver, stepper_locator,
                                                                "//div[contains(@class,'input-stepper-decrement')]")
        for _ in range(tap_amount):
            TouchActionsHandler.tap(self._driver, decrement_locator)
            time.sleep(1)

    def stepper_reset(self, stepper_locator):
        """
        This method taps on the stepper component's reset button to default value
        @param stepper_locator: main stepper element (usually ics-input-stepper, must be xpath locator)
        @return: void
        """
        reset_locator = KioskUtilities.add_xpath_to_locator(self._driver, stepper_locator,
                                                            "//div[contains(@class,'input-stepper-reset-button')]")
        TouchActionsHandler.tap(self._driver, reset_locator)
