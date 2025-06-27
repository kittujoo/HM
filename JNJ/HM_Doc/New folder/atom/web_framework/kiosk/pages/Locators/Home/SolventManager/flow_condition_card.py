"""
File_Name: flow_setting_screen_locators.py
Desc: This file contains locator object of the web elements in the flow setting screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 06/23/2020
__modified__ = "Sharmila Vairamani" Refactored the locators  11/06/2020
__modified__ = "Sharmila Vairamani" Moved file to the Solvent Manager folder 02/15/2021
__modified__ = "Sharmila Vairamani" Added edit field state locator 02/24/2021
__modified__ = "Sharmila Vairamani" Changed the class name - 02/25/2021
__modified__= "Sharmila Vairamani" Change the SOLVENT_COMPOSITION_TAB locator - 02/08/2021
__modified__ = "Tyler Prada" Added locators for field focus - 11/15/21
__modified__ = "Tyler Prada" Adjustments for removal of flow options 12/7/21
"""
from selenium.webdriver.common.by import By


class SolventCompositionTabScreen:
    SOLVENT_COMPOSITION_TAB = (By.XPATH, "//div[@class='modal-info-item ng-star-inserted']//li")
    SOLVENT_A_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='editField_0']//input")
    SOLVENT_B_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='editField_1']//input")
    SOLVENT_B_EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='editField_1']//div")
    SOLVENT_C_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='editField_2']//input")
    SOLVENT_D_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='editField_3']//input")
    SOLVENT_A_FIELD_FOCUS = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-id='editField_0']//ics-edit-field//div")
    SOLVENT_B_FIELD_FOCUS = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-id='editField_1']//ics-edit-field//div")
    SOLVENT_C_FIELD_FOCUS = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-id='editField_2']//ics-edit-field//div")
    SOLVENT_D_FIELD_FOCUS = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-id='editField_3']//ics-edit-field//div")
    SOLVENT_A_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_0']")
    SOLVENT_B_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_1']")
    SOLVENT_C_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_2']")
    SOLVENT_D_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_3']")
    SOLVENT_A_LINE_ID = (By.XPATH, "//ics-solvent-badge[@ng-reflect-value='A']")
    SOLVENT_B_LINE_ID = (By.XPATH, "//ics-solvent-badge[@ng-reflect-value='B']")
    SOLVENT_C_LINE_ID = (By.XPATH, "//ics-solvent-badge[@ng-reflect-value='C']")
    SOLVENT_D_LINE_ID = (By.XPATH, "//ics-solvent-badge[@ng-reflect-value='D']")
    RESET_COMPOSITION_BUTTON = (By.ID, "ispp-id-qsmFlowRateCondition-resetCompositionBtn")
    SOLVENT_A_HINT_LOCATOR = (By.XPATH, "//ics-edit-field[@id='editField_0']//div[@ng-reflect-ng-switch ='hint']/div/mat-hint")
    SOLVENT_B_HINT_LOCATOR = (By.XPATH,
                              "//ics-edit-field[@id='editField_1']//div[@ng-reflect-ng-switch ='hint']/div/mat-hint")
    SOLVENT_C_HINT_LOCATOR = (By.XPATH,
                              "//ics-edit-field[@id='editField_2']//div[@ng-reflect-ng-switch ='hint']/div/mat-hint")
    SOLVENT_D_HINT_LOCATOR = (By.XPATH,
                              "//ics-edit-field[@id='editField_3']//div[@ng-reflect-ng-switch ='hint']/div/mat-hint")


class FlowControlTabScreen:
    FLOW_TAB = (By.ID, "ispp-id-qsm-informationPanelItem-flowControl")
    FLOW_RATE_EDIT_FIELD = (
        By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-QSM-flow-rate-edit-fie']//input")
    FLOW_DEFAULT_VALUE_BUTTON = (By.XPATH, "//ics-action-button[@id='ispp-id-settingsKeypad-optionalBtn1']//button")
    FLOW_INFO = (
        By.XPATH, "//li[@id='ispp-id-qsm-informationPanelItem-flow']//span[@class='readback-value ng-star-inserted']")
    FLOW_RATE_VALUE_INFO = (
        By.XPATH,
        "//li[@id='ispp-id-qsm-informationPanelItem-flowRate']//span[@class='readback-value ng-star-inserted']")
    FLOW_RATE_UNIT_INFO = (By.XPATH, "//span[contains(text(),'mL')]")
    FLOW_EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id= 'ispp-id-QSM-flow-rate-edit-fie']/div ")
    FLOW_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id ='ispp-id-QSM-flow-toggle']//mat-slide-toggle")
    FLOW_HINT_LOCATOR = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-QSM-flow-rate-edit-fie']//div[@ng-reflect-ng-switch ='hint']/div//mat-hint")
    FLOW_CARD_RATE_LOCATOR = (By.XPATH, "//ics-flow-control//div[@class='commands-refresh-subtitle1']")
    TIME_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-QSM-flow-ramp-edit-fie']//input")


class FlowSettingsScreenLocator:
    HEADER = (By.XPATH, "//div[contains(text(),'Set Flow Rate')]")
