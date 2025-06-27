"""
File_Name: sign_in_screen_locators.py
Desc: This file contains locator object of the web elements in the sign-in screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__author__    = "Sharmila Vairamani" Initial Check-in 03/02/2020
__author__    = "Sharmila Vairamani" Initial Check-in 03/18/2020
__modified__ = "Tyler Prada" added delete locator, removed clear locator - 10/20/21
"""

from selenium.webdriver.common.by import By


class SignInScreenLocators:

    PIN_TEXT_BOX = (By.XPATH,
                    "//ics-pin-entry//input")
    PIN_FIELD_STATE = (By.XPATH, "//ics-pin-entry//ics-edit-field/div")
    NUM_PAD_1 = (By.XPATH, "//button[@data-displaylabel='1']")
    NUM_PAD_2 = (By.XPATH, "//button[@data-displaylabel='2']")
    NUM_PAD_3 = (By.XPATH, "//button[@data-displaylabel='3']")
    NUM_PAD_4 = (By.XPATH, "//button[@data-displaylabel='4']")
    NUM_PAD_5 = (By.XPATH, "//button[@data-displaylabel='5']")
    NUM_PAD_6 = (By.XPATH, "//button[@data-displaylabel='6']")
    NUM_PAD_7 = (By.XPATH, "//button[@data-displaylabel='7']")
    NUM_PAD_8 = (By.XPATH, "//button[@data-displaylabel='8']")
    NUM_PAD_9 = (By.XPATH, "//button[@data-displaylabel='9']")
    NUM_PAD_0 = (By.XPATH, "//button[@data-displaylabel='0']")

    PIN_DISPLAY = (By.ID, "ispp-id-hint-editField")
    UNLOCK_BUTTON = (
        By.XPATH, "//button[@class='hg-button hg-functionBtn hg-button-ok']")
    BACK_BUTTON = (By.XPATH, "//ics-secondary-panel-header//div[@class='sign-in-header-action-back']")
    DELETE_BUTTON = (By.XPATH, "//button[@class='hg-button hg-functionBtn hg-button-clear']")
    SHOW_PASSWORD_ICON = (By.ID, "ispp-id-iconRight-editField")

