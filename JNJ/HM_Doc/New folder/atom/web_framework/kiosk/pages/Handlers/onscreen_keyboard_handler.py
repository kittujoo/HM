"""
File_Name: onscreen_keyboard_handler.py
Desc: This file contains the common shared code related to on-screen keybaord actions across all the pages
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in - 9/28/22
__modified__ = "Tyler Prada" fixed double spacing issue 10/7/22
__modified__ = "Tyler Prada" Changed quotes keys to brackets keys 8/31/23
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Handlers.touch_actions_handler import TouchActionsHandler
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators


class OnscreenKeyboardHandler:

    onscreen_keyboard_dictionary = {
        # utility buttons such as shift keys are not included in dictionary, only text-related
        # -- All layouts/default & upper -- #
        " ": BasePageLocators.KEYBOARD_SPACE_BUTTON,
        ",": BasePageLocators.KEYBOARD_COMMA_BUTTON,
        ".": BasePageLocators.KEYBOARD_PERIOD_BUTTON,

        # -- Lower case [default] -- #
            # - row 1 - #
        "q": BasePageLocators.KEYBOARD_LOWER_Q_BUTTON,
        "w": BasePageLocators.KEYBOARD_LOWER_W_BUTTON,
        "e": BasePageLocators.KEYBOARD_LOWER_E_BUTTON,
        "r": BasePageLocators.KEYBOARD_LOWER_R_BUTTON,
        "t": BasePageLocators.KEYBOARD_LOWER_T_BUTTON,
        "y": BasePageLocators.KEYBOARD_LOWER_Y_BUTTON,
        "u": BasePageLocators.KEYBOARD_LOWER_U_BUTTON,
        "i": BasePageLocators.KEYBOARD_LOWER_I_BUTTON,
        "o": BasePageLocators.KEYBOARD_LOWER_O_BUTTON,
        "p": BasePageLocators.KEYBOARD_LOWER_P_BUTTON,
            # - row 2 - #
        "a": BasePageLocators.KEYBOARD_LOWER_A_BUTTON,
        "s": BasePageLocators.KEYBOARD_LOWER_S_BUTTON,
        "d": BasePageLocators.KEYBOARD_LOWER_D_BUTTON,
        "f": BasePageLocators.KEYBOARD_LOWER_F_BUTTON,
        "g": BasePageLocators.KEYBOARD_LOWER_G_BUTTON,
        "h": BasePageLocators.KEYBOARD_LOWER_H_BUTTON,
        "j": BasePageLocators.KEYBOARD_LOWER_J_BUTTON,
        "k": BasePageLocators.KEYBOARD_LOWER_K_BUTTON,
        "l": BasePageLocators.KEYBOARD_LOWER_L_BUTTON,
            # - row 3 - #
        "z": BasePageLocators.KEYBOARD_LOWER_Z_BUTTON,
        "x": BasePageLocators.KEYBOARD_LOWER_X_BUTTON,
        "c": BasePageLocators.KEYBOARD_LOWER_C_BUTTON,
        "v": BasePageLocators.KEYBOARD_LOWER_V_BUTTON,
        "b": BasePageLocators.KEYBOARD_LOWER_B_BUTTON,
        "n": BasePageLocators.KEYBOARD_LOWER_N_BUTTON,
        "m": BasePageLocators.KEYBOARD_LOWER_M_BUTTON,

        # -- Upper case [uppercase] -- #
            # - row 1 - #
        "Q": BasePageLocators.KEYBOARD_UPPER_Q_BUTTON,
        "W": BasePageLocators.KEYBOARD_UPPER_W_BUTTON,
        "E": BasePageLocators.KEYBOARD_UPPER_E_BUTTON,
        "R": BasePageLocators.KEYBOARD_UPPER_R_BUTTON,
        "T": BasePageLocators.KEYBOARD_UPPER_T_BUTTON,
        "Y": BasePageLocators.KEYBOARD_UPPER_Y_BUTTON,
        "U": BasePageLocators.KEYBOARD_UPPER_U_BUTTON,
        "I": BasePageLocators.KEYBOARD_UPPER_I_BUTTON,
        "O": BasePageLocators.KEYBOARD_UPPER_O_BUTTON,
        "P": BasePageLocators.KEYBOARD_UPPER_P_BUTTON,
            # - row 2 - #
        "A": BasePageLocators.KEYBOARD_UPPER_A_BUTTON,
        "S": BasePageLocators.KEYBOARD_UPPER_S_BUTTON,
        "D": BasePageLocators.KEYBOARD_UPPER_D_BUTTON,
        "F": BasePageLocators.KEYBOARD_UPPER_F_BUTTON,
        "G": BasePageLocators.KEYBOARD_UPPER_G_BUTTON,
        "H": BasePageLocators.KEYBOARD_UPPER_H_BUTTON,
        "J": BasePageLocators.KEYBOARD_UPPER_J_BUTTON,
        "K": BasePageLocators.KEYBOARD_UPPER_K_BUTTON,
        "L": BasePageLocators.KEYBOARD_UPPER_L_BUTTON,
            # - row 3 - #
        "Z": BasePageLocators.KEYBOARD_UPPER_Z_BUTTON,
        "X": BasePageLocators.KEYBOARD_UPPER_X_BUTTON,
        "C": BasePageLocators.KEYBOARD_UPPER_C_BUTTON,
        "V": BasePageLocators.KEYBOARD_UPPER_V_BUTTON,
        "B": BasePageLocators.KEYBOARD_UPPER_B_BUTTON,
        "N": BasePageLocators.KEYBOARD_UPPER_N_BUTTON,
        "M": BasePageLocators.KEYBOARD_UPPER_M_BUTTON,

        # -- Alt symbols [alt] -- #
            # - row 1 - #
        "1": BasePageLocators.KEYBOARD_ONE_BUTTON,
        "2": BasePageLocators.KEYBOARD_TWO_BUTTON,
        "3": BasePageLocators.KEYBOARD_THREE_BUTTON,
        "4": BasePageLocators.KEYBOARD_FOUR_BUTTON,
        "5": BasePageLocators.KEYBOARD_FIVE_BUTTON,
        "6": BasePageLocators.KEYBOARD_SIX_BUTTON,
        "7": BasePageLocators.KEYBOARD_SEVEN_BUTTON,
        "8": BasePageLocators.KEYBOARD_EIGHT_BUTTON,
        "9": BasePageLocators.KEYBOARD_NINE_BUTTON,
        "0": BasePageLocators.KEYBOARD_ZERO_BUTTON,
            # - row 2 - #
        "@": BasePageLocators.KEYBOARD_AT_SYMBOL_BUTTON,
        "#": BasePageLocators.KEYBOARD_NUMBER_SIGN_BUTTON,
        "$": BasePageLocators.KEYBOARD_DOLLAR_SIGN_BUTTON,
        "&": BasePageLocators.KEYBOARD_AMPERSAND_BUTTON,
        "*": BasePageLocators.KEYBOARD_ASTERISK_BUTTON,
        "(": BasePageLocators.KEYBOARD_LEFT_PARENTHESIS_BUTTON,
        ")": BasePageLocators.KEYBOARD_RIGHT_PARENTHESIS_BUTTON,
        "[": BasePageLocators.KEYBOARD_LEFT_BRACKET_BUTTON,
        "]": BasePageLocators.KEYBOARD_RIGHT_BRACKET_BUTTON,
            # - row 3 - #
        "%": BasePageLocators.KEYBOARD_PERCENT_SIGN_BUTTON,
        "-": BasePageLocators.KEYBOARD_MINUS_BUTTON,
        "+": BasePageLocators.KEYBOARD_PLUS_BUTTON,
        "=": BasePageLocators.KEYBOARD_EQUAL_SIGN_BUTTON,
        "/": BasePageLocators.KEYBOARD_FORWARD_SLASH_BUTTON,
        ";": BasePageLocators.KEYBOARD_SEMICOLON_BUTTON,
        ":": BasePageLocators.KEYBOARD_COLON_BUTTON,
        "!": BasePageLocators.KEYBOARD_EXCLAMATION_MARK_BUTTON,
        "?": BasePageLocators.KEYBOARD_QUESTION_MARK_BUTTON
    }

    def __init__(self, driver):
        super().__init__()
        self.logger = Logger(self.__class__.__name__)
        self._driver = driver

    def enter_string(self, string):
        """
        This function allows the user to enter a string into a text area using the on-screen keyboard
        :@param string | ex: "The quick brown fox jumped over the something, I don't remember the rest."
        :return:
        """

        index = 0
        while index < len(string):
            if string[index] in OnscreenKeyboardHandler.onscreen_keyboard_dictionary:
                locator = OnscreenKeyboardHandler.onscreen_keyboard_dictionary[string[index]]
                self.logger.info(f"Locator value => {locator}")

                if string[index].isspace():
                    # space is non-letter and non-special character but on all layouts
                    TouchActionsHandler.tap(self._driver, locator)

                if string[index] == "," or string[index] == ".":
                    # comma and period are on the default layout so do not need to change anything
                    TouchActionsHandler.tap(self._driver, locator)

                if not string[index].isalpha() and string[index] != "," and string[index] != "." and not string[index].isspace():
                    # if character is a symbol we need to go to the alt layout, and return for the next character
                    TouchActionsHandler.tap(self._driver, BasePageLocators.KEYBOARD_LEFT_ALT_BUTTON)
                    TouchActionsHandler.tap(self._driver, locator)
                    TouchActionsHandler.tap(self._driver, BasePageLocators.KEYBOARD_LEFT_DEFAULT_BUTTON)

                if string[index].isupper():
                    # if an uppercase letter then make the upper case layout appear for the given character
                    TouchActionsHandler.tap(self._driver, BasePageLocators.KEYBOARD_LEFT_SHIFT_BUTTON)
                    TouchActionsHandler.tap(self._driver, locator)

                if string[index].islower():
                    TouchActionsHandler.tap(self._driver, locator)

            else:
                # if there's a character that isn't part of the keyboard then fill it with a noticeable replacement character
                # this should be seen during debugging, validation will not pass
                self.logger.info(f"Character {string[index]} is not supported in the on-screen keyboard, replacing with a hashtag...")
                TouchActionsHandler.tap(self._driver, BasePageLocators.KEYBOARD_LEFT_ALT_BUTTON)
                TouchActionsHandler.tap(self._driver, BasePageLocators.KEYBOARD_NUMBER_SIGN_BUTTON)
                TouchActionsHandler.tap(self._driver, BasePageLocators.KEYBOARD_LEFT_DEFAULT_BUTTON)

            index += 1

    def tap_backspace_button(self, no_of_times):
        """
        Tap backspace button for a given number of times.
        @param no_of_times
        :return: void
        """
        index = 0
        locator = BasePageLocators.KEYBOARD_BACKSPACE_BUTTON
        while index < no_of_times:
            time.sleep(.1)
            TouchActionsHandler.tap(self._driver, locator)
            index += 1

    def clear_text_area(self, text_area_locator):
        """
        This function clears the content in the numpad entry field
        @param text_area_locator | ex: //textarea
        NOTE: text field must be a text area element in order to pull the ng-reflect-model attribute value
        :return:
        """
        # entries = WebElementsHandler.get_element(self._driver, text_area_locator)
        # entries = entries.get_attribute("ng-reflect-model")
        # self.logger.info(f"*********************************entries  ====> {entries}")
        # entries_count = len(entries)
        # self.logger.info(f"**************************entries count ====> {entries_count}")

        # The above logic is commented in the case where we may have to delete characters one-by-one in a text area
        # Text areas are always highlighted so one delete tap clears the area
        self.tap_backspace_button(1)