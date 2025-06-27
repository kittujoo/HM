"""
File_Name:  base_page_locators.py
Desc: This file contains locator object that is commonly used across the kiosk
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/05/2020
__modified__ = "Sharmila Vairamani changed the locator  - 06/11/2020
__modified__ = "Sharmila Vairamani Added the back button locator - 02/23/2021
__modified__ = "Sharmila Vairamani " updated the apply button locator" - 03/19/2021
__modified__ "Sharmila Vairamani" Changed locator for done_button - 03/22/2021
__modified__ = "Tyler Prada" Changed Done button locator 1/31/22
__modified__ = "Tyler Prada" small clean-up and on-screen keyboard locators 9/28/22
"""

from selenium.webdriver.common.by import By


class BasePageLocators:
    ##########################
    # -- General Locators -- #
    ##########################

    DONE_BUTTON = (By.XPATH, "//ics-primary-action//ics-tray[@ng-reflect-icon='ics-img-done']")
    CANCEL_BUTTON = (By.XPATH, "//ics-primary-action//ics-tray[@ng-reflect-icon='ics-img-cancel']")
    BACK_BUTTON = (By.XPATH, "//ics-tray[@ng-reflect-icon='ics-img-back']")
    NEXT_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-next']")
    START_BUTTON = (By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-tray[@ng-reflect-icon='ics-img-startup']")
    STOP_BUTTON = (By.XPATH, "//ics-primary-action//ics-tray[@ng-reflect-icon='ics-img-stop']")
    CLOSE_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray")
    NEXT_BUTTON_LABEL = (By.XPATH, "//ics-primary-action[@id='navigation-next']//ics-tray")
    STOP_BUTTON_STATE = (
        By.XPATH, "//ics-primary-action//ics-tray[@ng-reflect-text='Close']//div[@class ='tray-container']//div")

    #############################
    # -- Number Pad Locators -- #
    #############################

    NUM_PAD_1_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad1')]")
    NUM_PAD_2_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad2')]")
    NUM_PAD_3_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad3')]")
    NUM_PAD_4_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad4')]")
    NUM_PAD_5_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad5')]")
    NUM_PAD_6_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad6')]")
    NUM_PAD_7_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad7')]")
    NUM_PAD_8_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad8')]")
    NUM_PAD_9_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad9')]")
    NUM_PAD_0_BUTTON = (By.XPATH, "//button[contains(@class,'hg-button hg-functionBtn hg-button-numpad0')]")
    NUM_PAD_DELETE_BUTTON = (By.XPATH, "//button[contains(@data-skbtn,'{bksp}')]")
    NUM_PAD_DECIMAL = (By.XPATH, "//button[@data-skbtn='{decimalpoint}']")
    NUM_PAD_CONTAINER = (By.XPATH, "//div[contains(@class,'settings-keypad-container')]")

    ####################################
    # -- Onscreen Keyboard Locators -- #
    ####################################

    # -- Static Buttons (all layouts) -- #
    KEYBOARD_BACKSPACE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{backspace}']")
    KEYBOARD_ENTER_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{enter}']")
    KEYBOARD_LEFT_SHIFT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{shift-left}']")
    KEYBOARD_RIGHT_SHIFT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{shift-right}']")
    KEYBOARD_SPACE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{space}']")
    KEYBOARD_HIDE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{downkeyboard}")
        # - Lower and Upper layouts - #
    KEYBOARD_COMMA_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn=',']")
    KEYBOARD_PERIOD_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='.']")
    KEYBOARD_LEFT_ALT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{alt-left}']")
    KEYBOARD_RIGHT_ALT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{alt-right}']")

    # -- Lower case [default] -- #
        # - row 1 - #
    KEYBOARD_LOWER_Q_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='q']")
    KEYBOARD_LOWER_W_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='w']")
    KEYBOARD_LOWER_E_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='e']")
    KEYBOARD_LOWER_R_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='r']")
    KEYBOARD_LOWER_T_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='t']")
    KEYBOARD_LOWER_Y_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='y']")
    KEYBOARD_LOWER_U_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='u']")
    KEYBOARD_LOWER_I_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='i']")
    KEYBOARD_LOWER_O_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='o']")
    KEYBOARD_LOWER_P_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='p']")
        # - row 2 - #
    KEYBOARD_LOWER_A_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='a']")
    KEYBOARD_LOWER_S_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='s']")
    KEYBOARD_LOWER_D_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='d']")
    KEYBOARD_LOWER_F_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='f']")
    KEYBOARD_LOWER_G_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='g']")
    KEYBOARD_LOWER_H_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='h']")
    KEYBOARD_LOWER_J_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='j']")
    KEYBOARD_LOWER_K_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='k']")
    KEYBOARD_LOWER_L_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='l']")
        # - row 3 - #
    KEYBOARD_LOWER_Z_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='z']")
    KEYBOARD_LOWER_X_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='x']")
    KEYBOARD_LOWER_C_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='c']")
    KEYBOARD_LOWER_V_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='v']")
    KEYBOARD_LOWER_B_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='b']")
    KEYBOARD_LOWER_N_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='n']")
    KEYBOARD_LOWER_M_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='m']")

    # -- Upper case [uppercase] -- #
        # - row 1 - #
    KEYBOARD_UPPER_Q_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='Q']")
    KEYBOARD_UPPER_W_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='W']")
    KEYBOARD_UPPER_E_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='E']")
    KEYBOARD_UPPER_R_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='R']")
    KEYBOARD_UPPER_T_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='T']")
    KEYBOARD_UPPER_Y_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='Y']")
    KEYBOARD_UPPER_U_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='U']")
    KEYBOARD_UPPER_I_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='I']")
    KEYBOARD_UPPER_O_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='O']")
    KEYBOARD_UPPER_P_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='P']")
        # - row 2 - #
    KEYBOARD_UPPER_A_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='A']")
    KEYBOARD_UPPER_S_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='S']")
    KEYBOARD_UPPER_D_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='D']")
    KEYBOARD_UPPER_F_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='F']")
    KEYBOARD_UPPER_G_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='G']")
    KEYBOARD_UPPER_H_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='H']")
    KEYBOARD_UPPER_J_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='J']")
    KEYBOARD_UPPER_K_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='K']")
    KEYBOARD_UPPER_L_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='L']")
        # - row 3 - #
    KEYBOARD_UPPER_Z_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='Z']")
    KEYBOARD_UPPER_X_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='X']")
    KEYBOARD_UPPER_C_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='C']")
    KEYBOARD_UPPER_V_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='V']")
    KEYBOARD_UPPER_B_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='B']")
    KEYBOARD_UPPER_N_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='N']")
    KEYBOARD_UPPER_M_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='M']")

    # -- Alt symbols [alt] -- #
        # - row 1 - #
    KEYBOARD_ONE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='1']")
    KEYBOARD_TWO_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='2']")
    KEYBOARD_THREE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='3']")
    KEYBOARD_FOUR_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='4']")
    KEYBOARD_FIVE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='5']")
    KEYBOARD_SIX_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='6']")
    KEYBOARD_SEVEN_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='7']")
    KEYBOARD_EIGHT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='8']")
    KEYBOARD_NINE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='9']")
    KEYBOARD_ZERO_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='0']")
        # - row 2 - #
    KEYBOARD_AT_SYMBOL_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='@']")
    KEYBOARD_NUMBER_SIGN_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='#']")
    KEYBOARD_DOLLAR_SIGN_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='$']")
    KEYBOARD_AMPERSAND_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='&']")
    KEYBOARD_ASTERISK_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='*']")
    KEYBOARD_LEFT_PARENTHESIS_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='(']")
    KEYBOARD_RIGHT_PARENTHESIS_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn=')']")
    KEYBOARD_SINGLE_QUOTE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn=\"'\"]")
    KEYBOARD_DOUBLE_QUOTE_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='\"']")
    KEYBOARD_LEFT_BRACKET_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='[']")
    KEYBOARD_RIGHT_BRACKET_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn=']']")
        # - row 3 - #
    KEYBOARD_PERCENT_SIGN_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='%']")
    KEYBOARD_MINUS_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='-']")
    KEYBOARD_PLUS_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='+']")
    KEYBOARD_EQUAL_SIGN_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='=']")
    KEYBOARD_FORWARD_SLASH_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='/']")
    KEYBOARD_SEMICOLON_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn=';']")
    KEYBOARD_COLON_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn=':']")
    KEYBOARD_EXCLAMATION_MARK_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='!']")
    KEYBOARD_QUESTION_MARK_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='?']")
        # - row 4 - #
    KEYBOARD_LEFT_DEFAULT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{default-left}']")
    KEYBOARD_RIGHT_DEFAULT_BUTTON = (By.XPATH, "//ics-keypad//button[@data-skbtn='{default-right}']")

    MACHINE_STATE = (By.XPATH, "//ics-system-state-text[@id = 'ispp-id-systemStateText-header']/div/div")
    WORKFLOW_DISPLAY_MESSAGE = (By.XPATH, "//ics-modal-info//ics-info-list-item//div[contains(@class,'sub')]/div")
    WORKFLOW_STATE = (By.XPATH, "//ics-modal-info-keypad//ics-info-list-item//ics-info-list-item-state")
    RESULTS_HEADER = (By.XPATH, "//div[@class ='secondary-panel-workflow-header-content']//div[@class='current step']")
