"""
File_Name: command_screen_locators.py
Desc: This file contains locator object of the webelements in the command screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/15/2020
__modified__ = "Sharmila Vairamani" changed the locator for command description- 10/20/2020
__modified__ "Tyler Prada" Added locators: prime solvent, autozero, prime seal, reset, page2 7/2/21
__modified__ = "Tyler Prada" added startup workflow start button locator 9/27/2021
"""
from selenium.webdriver.common.by import By


class CommandsScreenPageLocators:
    COMMAND_FLY_MENU = (By.XPATH, "//div[@class='slide-out-panel']")

    UV_LAMP_COMMAND_BUTTON_TEXT = (
        By.XPATH, "//ics-commands-refresh[@class='lamp-control-container']//div[@class='commands-refresh-subtitle1']")

    FLOWRATE_INFO = (By.XPATH, "//ics-flow-control//ics-commands-refresh//div[@class='commands-refresh-subtitle1']")

    UV_LAMP_COMMAND_BUTTON = (
        By.XPATH, "//ics-commands-refresh[@class='lamp-control-container']/descendant::div[@class='status-ring progressing_determinate']")

    UV_LAMP_COMMAND_DESCRIPTION = (By.XPATH, "//ics-lamp-on-off[@class='ng-star-inserted']//mat-card-subtitle"
                                             "[contains(@class,'mat-card-subtitle')][1]")
    ROTARY_TRAY_COMMAND_BUTTON = (By.XPATH,
                                  "//ics-action-button[@id='ispp-id-commandCard-actionButton']//div[@class ='action-button-label ng-star-inserted']")

    ROTARY_TRAY_COMMAND_DESCRIPTION = (By.ID, "ispp-id-commandCard-subtitle1")

    UV_LAMP_ON = (By.ID, "ispp-id-commandCard-subtitle1")

    PRIME_SOLVENT_BUTTON = (By.XPATH, "//ics-prime-solvents//ics-action-button")
    PRIME_SOLVENT_LABEL = (By.XPATH, "//ics-prime-solvents//mat-card-subtitle")
    
    FLOW_COMMAND_BUTTON = (
        By.XPATH, "//ics-dynamic-component//ics-commands-refresh[@class='flow-control-container']//ics-status-ring")
    
    FLOW_COMMAND_PROGRESS_BAR = (By.XPATH, "//ics-flow-command//ics-progress-bar")

    AUTO_ZERO_BUTTON = (By.XPATH, "//ics-detector-autozero//ics-action-button")
    AUTO_ZERO_LABEL = (By.XPATH, "//ics-detector-autozero//mat-card-subtitle")

    PRIME_SEAL_BUTTON = (By.XPATH, "//ics-prime-seal-wash//ics-action-button")
    PRIME_SEAL_LABEL = (By.XPATH, "//ics-prime-seal-wash//mat-card-subtitle[@id='ispp-id-commandCard-subtitle1']")

    RESET_SYSTEM_BUTTON = (By.XPATH, "//ics-commands-refresh[@class='reset-command-container']//mat-icon")
    RESET_SYSTEM = (By.XPATH, "//ics-reset-command//div[contains(@class,'tap')]")
    RESET_TEXT = (By.XPATH, "//ics-reset-command//div[@class ='commands-refresh-subtitle1']")
    STOP_TEXT = (
        By.XPATH,
        "//ics-commands-refresh[@class ='estop-command-container']//div[@class ='commands-refresh-subtitle1']")
    STOP_SYSTEM = (By.XPATH, "//ics-commands-refresh[@class ='estop-command-container']//ics-status-ring")
    STOP_SYSTEM_BUTTON = (By.XPATH, "//ics-commands-refresh[@class ='estop-command-container']//mat-icon")
    COMMANDS_PAGE_TWO = (By.XPATH, "//li//a[@id='isppK-id-pagination-page2']")

    LEAK_TEST_PANEL = (By.XPATH, "//button[@id='leakTestWorkflowActionButton']")

    STARTUP_WORKFLOW_START = (By.ID, "instrumentStartupActionButton")
    FLOW_COMMAND_BUTTON_TEXT = (
        By.XPATH, "//ics-flow-control//ics-commands-refresh//div[@class='commands-refresh-subtitle1']")
    FLOW_RATE_UNITS = (
        By.XPATH, "//ics-flow-control//ics-commands-refresh//div[@class='commands-refresh-subtitle2']")