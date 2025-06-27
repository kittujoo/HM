"""
File_Name: calibrate_axes_locators.py
Desc: This file contains locator object of the web elements in the calibrate_axes workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 3/9/2022
__modified__ = "Tyler Prada" added platter shut down locators, changed some header locators 5/3/22
__modified__ = "Tyler Prada" added summary screen locators & various locator fixes 6/17/22
__modified__ = "Tyler Prada" added B0 path results locators 7/28/22
__modified__ = "Tyler Prada" added platter path results locators 8/31/22
__modified__ = "Tyler Prada" Post-FCS Adjustments 7/26/23
"""
from selenium.webdriver.common.by import By


class CalibrateAxesWorkflowLocators:
    # -- general & navigation -- #
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    START_BUTTON = (By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    POWER_OFF_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'primary-action-done')]//div[@class='primary-action']")
    CONFIRMATION_CHECK = (By.XPATH, "//mat-checkbox[contains(@id,'mat-checkbox')]")

    # -- paths -- #
    ZAXIS_PATH = (By.ID,"ispp-id-calibrate-axes-functions-Z-axis")
    ZPAXIS_PATH = (By.ID, "ispp-id-calibrate-axes-functions-Zp-axis")
    PLATTER_PATH = (By.ID, "ispp-id-calibrate-axes-functions-platter")
    B0_PATH = (By.ID, "ispp-id-calibrate-axes-functions-B-axes")
    HARD_STOP_PATH = (By.ID, "ispp-id-calibrate-axes-functions-hard-stop")

    # -- headers -- #
    FUNCTIONS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-functions")
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-overview")
    CAUTIONS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-cautions")
    POWEROFF_INFO_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-poweroff-info")
    POWEROFF_STATUS_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-poweroff-status")
    SETUP_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-setup")
    PRECONDITIONS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-conditions")
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-summary")
    STATUS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-status")
    RESULTS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-results")
    COMPLETION_PAGE_BANNER = (By.ID, "ispp-id-calibrate-axes-workflow-complete-calibration")
    # ispp-id-calibrate-axes-workflow-instructions ||| setup screen [Also status screen for B-0]
    # ispp-id-calibrate-axes-workflow-poweroff-status ||| status screen

    # -- Summary & Results Info Labels -- #
    COMPARTMENT_DOOR_INFO_LABEL = (By.XPATH, "//div[@class='info-list-item-content divider-item']//div[text()='Closed']")
    SAMPLE_PLATES_INFO_LABEL = (By.XPATH, "//div[@class='workflow-summary-container']//li[2]//div[2]")
    TEST_TIME_INFO_LABEL = (By.XPATH, "//div[@class='workflow-summary-container']//li//div[contains(text(),'minute') or contains(text(),'minutes')]")
    TRAY_DRAWER_INFO_LABEL = (By.XPATH, "//div[@class='workflow-summary-container']//li[2]//div[2]")
    NEEDLE_ADAPTOR_INFO_LABEL = (By.XPATH, "//div[@class='workflow-summary-container']//li[3]//div[2]")
    COLLAPSIBLE_TABLE_TOGGLE = (By.XPATH, "//ics-collapsible-table//div[contains(@class,'item-icon-position')]")
    RESULTS_STATUS = (By.XPATH, "//ics-collapsible-table//ics-info-list-item//div[contains(@class, 'header')]//div[contains(@class,'subtitle')][1]//div")

    # -- Platter Path Results -- #
    OFFSET_VALUE_LABEL = (By.XPATH, "//ics-table//ul//li[2]//div")
    OFFSET_VALUE = (By.XPATH, "//ics-table//ul//li[1]/ul")

    # -- B0 Path Results -- #
    PLATE_ONE_RN = (By.XPATH, "//ics-table//ul[2]//li[2]")
    PLATE_ONE_LC = (By.XPATH, "//ics-table//ul[2]//li[3]")
    PLATE_ONE_BETA = (By.XPATH, "//ics-table//ul[2]//li[4]")
    PLATE_ONE_THETA = (By.XPATH, "//ics-table//ul[2]//li[5]")

    PLATE_TWO_RN = (By.XPATH, "//ics-table//ul[3]//li[2]")
    PLATE_TWO_LC = (By.XPATH, "//ics-table//ul[3]//li[3]")
    PLATE_TWO_BETA = (By.XPATH, "//ics-table//ul[3]//li[4]")
    PLATE_TWO_THETA = (By.XPATH, "//ics-table//ul[3]//li[5]")

    PLATE_THREE_RN = (By.XPATH, "//ics-table//ul[4]//li[2]")
    PLATE_THREE_LC = (By.XPATH, "//ics-table//ul[4]//li[3]")
    PLATE_THREE_BETA = (By.XPATH, "//ics-table//ul[4]//li[4]")
    PLATE_THREE_THETA = (By.XPATH, "//ics-table//ul[4]//li[5]")

    # -- Welcome Screen for Z-axis -- #
    WELCOME_PARA_ONE_Z_AXIS = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[1]")
    WELCOME_PARA_TWO_Z_AXIS = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[2]")
    WELCOME_PARA_THREE_Z_AXIS = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[3]")

    # -- Welcome Screen for Zp-axis -- #
    WELCOME_PARA_ONE_Zp_AXIS = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[1]")
    WELCOME_PARA_TWO_Zp_AXIS = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[2]")

    # -- Welcome Screen for Hard Stop -- #
    WELCOME_PARA_ONE_HARD_STOP = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[1]")
    WELCOME_PARA_TWO_HARD_STOP = (By.XPATH, "//ics-calibrate-axes-overview//div[@class='column'][1]//section[2]")
