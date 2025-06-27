"""
File_Name: picker_spinner_handler.py
Desc: This file contains the common shared code related to picker/spinner component within the KIOSK
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in - 11/1/2021
__modified__ = "Tyler Prada" Rework for new picker component structure - 2/20/23
__modified__ = "Tyler Prada" Fixed select_spinner_text and added another temporary function 9/19/23
"""

import time
from utilities.logger import Logger
from web_framework.kiosk.pages.Handlers.web_elements_handler import WebElementsHandler
from web_framework.kiosk.pages.Handlers.touch_actions_handler import TouchActionsHandler
from web_framework.kiosk.pages.Utilities.kiosk_utilities import KioskUtilities
from web_framework.web_driver_common.element import get_text


class PickerSpinnerHandler:
    """
        picker/spinner component handler class that contains
            common shared code across all the pages
    """

    def __init__(self, driver):
        super().__init__()
        self.logger = Logger(self.__class__.__name__)
        self._driver = driver

    def set_spinner_value(self, spinner_locator, desired_value):
        """
        This method takes in a desired value and selects that value within a spinner/picker component
        :param spinner_locator: xpath locator for the spinner/picker list. This must be an ics-picker-base, and a ul element within that base
        example: //ics-picker-base[@ng-reflect-id='ispp-id-instrument-startup-sam']//div//div//div[1]//ul
        :param desired_value: the value to be selected. this should match the format of what is within the spinner/picker list
        example: 25.0 or 10
        :return: void
        """
        # get element list of all options within spinner
        list_numbers_locator = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//li//div")

        full_numbers_list = WebElementsHandler.get_elements(self._driver, list_numbers_locator)

        # get value of all options within spinner
        full_numbers_list_text = []
        for i in range(len(full_numbers_list)):
            full_numbers_list_text.append(full_numbers_list[i].get_attribute('innerHTML').replace(" ", ""))

        # get the position of the desired value
        # NOTE: the "-1" was added due to a picker rework found in the startup workflow
        # If this causes issues in other locations, then an adjustment MUST be made either in KIOSK or in this method
        desired_value_position = str(full_numbers_list_text.index(desired_value)-1)

        # create xpath based on desired selection's location
        desired_selection = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//li["+desired_value_position+"]")

        # execute JS to scroll to the desired element using the generated xpath
        self._driver.execute_script("var element = document.evaluate(\""+ desired_selection[1] +"\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; element.scrollIntoView(true);")

        # # -- increment condition -- #
        # if float(currently_selected_value) < float(desired_value):
        #     self.increment_spinner_value(spinner_locator, currently_selected_position, desired_value_position)
        #     return
        #
        # # -- decrement condition -- #
        # if float(currently_selected_value) > float(desired_value):
        #     self.decrement_spinner_value(spinner_locator, currently_selected_position, desired_value_position)
        #     return

    def increment_spinner_value(self, spinner_locator, current_pos, desired_pos):
        time.sleep(5) ##TODO picker component issue INS-26326
        for i in range(current_pos + 2, desired_pos + 2):
            time.sleep(1)
            TouchActionsHandler.tap(self._driver, KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator,
                                                                                      "//li[" + str(i) + "]//div"))
            time.sleep(0.5)

    def decrement_spinner_value(self, spinner_locator, current_pos, desired_pos):
        time.sleep(5) ##TODO picker component issue INS-26326
        for i in reversed(range(desired_pos + 1, current_pos + 1)):
            time.sleep(1)
            TouchActionsHandler.tap(self._driver, KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator,
                                                                                      "//li[" + str(i) + "]//div"))
            time.sleep(0.5)

    # This is a temporary function where the logic within should be used to replace the logic of select_spinner_text once picker components are able to take the scroll action
    # Specifically this issue is seen in the date & time user settings within the KIOSK
    def select_spinner_text_EXP(self, spinner_locator, desired_value):
        # get element list of all options within spinner
        list_numbers_locator = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//li//div")
        full_numbers_list = WebElementsHandler.get_elements(self._driver, list_numbers_locator)

        # get value of all options within spinner
        full_numbers_list_text = []
        for i in range(len(full_numbers_list)):
            full_numbers_list_text.append(full_numbers_list[i].get_attribute('innerHTML').strip())
            
        desired_value_position = str(full_numbers_list_text.index(desired_value)+1)
        
         # create xpath based on desired selection's location
        desired_selection = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//li["+desired_value_position+"]")

        # execute JS to scroll to the desired element using the generated xpath
        self._driver.execute_script("var element = document.evaluate(\""+ desired_selection[1] +"\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; element.scrollIntoView(true);")

    # TODO: refactor the text method like the number one to accommodate the new picker component structure
    # There is a working refactor above this method, the _EXP one. However, the picker component in the application is not taking the scroll action
    # This method can be replaced with the logic within the _EXP one once picker component is able to take the scroll action
    def select_spinner_text(self, spinner_locator, desired_value):
        """
        This method takes in a desired value and selects that value within a spinner/picker component
        :param spinner_locator: xpath locator for the spinner/picker list. This must be an ics-picker-base, and a ul element within that base
        example: //ics-picker-base[@ng-reflect-id='ispp-id-instrument-startup-sam']//div//div//div[1]//ul
        :param desired_value: the value to be selected. this should match the format of what is within the spinner/picker list
        example: 25.0 or 10
        :return: void
        """
        # get the current selection
        # TODO: when at the top of the list, there is no rotationX style
        # INS-23818
        currently_selected_locator = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator,
                                                                         "//li[contains(@class,'selected')]//div")
        currently_selected_value = get_text(self._driver, currently_selected_locator)
        self.logger.info(f" The first before formating currently selected value >>> {currently_selected_value}")
        currently_selected_value = currently_selected_value.replace(" ", "")

        # get element list of all options within spinner
        list_numbers_locator = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//li//div")
        full_numbers_list = WebElementsHandler.get_elements(self._driver, list_numbers_locator)

        # get value of all options within spinner
        full_numbers_list_text = []
        for i in range(len(full_numbers_list)):
            full_numbers_list_text.append(full_numbers_list[i].get_attribute('innerHTML').replace(" ", ""))

        # get the position of the values within the spinner list
        self.logger.info(f"currently_selected_value====>>>{currently_selected_value}")
        currently_selected_position = full_numbers_list_text.index(currently_selected_value)
        self.logger.info(f"currently_selected_position===>>>> {currently_selected_position}")
        desired_value = desired_value.replace(" ", "")
        desired_value_position = full_numbers_list_text.index(desired_value)+1  # 1
        self.logger.info(f"desired_value_position===>>>> {desired_value_position}")  # 3

        # -- increment condition -- #
        if float(currently_selected_position) < float(desired_value_position):
            self.increment_spinner_value(spinner_locator, currently_selected_position, desired_value_position)
            return

        # -- decrement condition -- #
        if float(currently_selected_position) > float(desired_value_position):
            self.decrement_spinner_value(spinner_locator, currently_selected_position, desired_value_position)
            return

    def select_spinner_text_plots(self, spinner_locator, desired_value):
            # get element list of all options within spinner
            list_numbers_locator = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//ics-vertical-selector-item//li")
            full_numbers_list = WebElementsHandler.get_elements(self._driver, list_numbers_locator)
            self.logger.info(f"The plots list====>>>>{full_numbers_list}")

            # get value of all options within spinner
            full_numbers_list_text = []
            for i in range(len(full_numbers_list)):
                full_numbers_list_text.append(full_numbers_list[i].get_attribute('innerHTML').strip())
                
            desired_value_position = str(full_numbers_list_text.index(desired_value)+1)
            
            # create xpath based on desired selection's location  
            desired_selection = KioskUtilities.add_xpath_to_locator(self._driver, spinner_locator, "//ics-vertical-selector-item["+desired_value_position+"]//li")


            # execute JS to scroll to the desired element using the generated xpath
            self._driver.execute_script("var element = document.evaluate(\""+ desired_selection[1] +"\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; element.scrollIntoView(true);")
            time.sleep(3) # Time required for the scroll animation to complete
            TouchActionsHandler.tap(self._driver,desired_selection)
            
            