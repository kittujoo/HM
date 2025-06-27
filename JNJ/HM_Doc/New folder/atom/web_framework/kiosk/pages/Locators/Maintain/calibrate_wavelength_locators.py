"""
File_Name: calibrate_wavelength_locators.py
Desc: This file contains locator object of the web elements in the calibrate workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = Sharmila Vairamani" Initial Check-in 06/06/2022
__modified__ = "Tyler Prada" added summary locators 7/18/22
__modified__ = "Tyler Prada" Tweaked status and results, misc cleanup 9/7/22
"""
from selenium.webdriver.common.by import By


class CalibrateWavelengthWorkflowLocators:
    # -- Page Banners -- #
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-verify-and-calibrate-wavelengths-overview")
    FUNCTION_BANNER = (By.ID, "ispp-id-verify-and-calibrate-wavelengths-functions")
    OPTIONS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-wavelengths-workflow-options")
    PRECONDITIONS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-wavelengths-workflow-preconditions")
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-calibrate-wavelengths-workflow-summary")
    PROGRESS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-wavelengths-workflow-status")
    RESULTS_PAGE_BANNER = (By.ID, "ispp-id-calibrate-wavelengths-workflow-results")
    PRE_FLUSH_PAGE_BANNER = (By.XPATH, "//div[text()=' Flush Option ']")
    ADDITIONAL_FLUSH_OPTION_BANNER = (By.XPATH, "//div[text()=' Additional Flush Option ']")
    FLOW_CONTROL_BANNER = (By.ID, "ispp-id-calibrate-wavelengths-workflow-flow-control")
    FLOW_RATE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Flow Rate')]")
    INTERRUPTED_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),' Workflow interrupted ')]")

    # -- General Workflow Locators -- #
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    RETRY_BUTTON = (By.XPATH, "//div[text()=' RETRY ']/ancestor::ics-primary-action")
    START_BUTTON = (
        By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH,
                     "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[1]//ics-tray[@ng-reflect-text = 'Done']")
    WORKFLOW_STOPPED_BANNER = (By.XPATH, "//div[contains(text(),'Workflow stopped unexpectedly')]")
    CALIBRATE_WAVELENGTH_OPTION = (
        By.XPATH,
        "//ics-info-list-icon[@id ='verify-and-calibrate-wavelengths-functions-calibrate']//ics-info-list-item")
    VERIFY_WAVELENGTH_OPTION = (
        By.XPATH, "//ics-info-list-icon[@id ='verify-and-calibrate-wavelengths-functions-verify']//ics-info-list-item")

    # -- Options Screen -- #
    FLUSH_TOGGLE_BUTTON = (
        By.ID, "ispp-id-verify-and-calibrate-wavelengths-flush-column-toggle")
    PRE_FLUSH_TOGGLE = (By.ID, "ispp-id-verify-and-calibrate-wavelengths-additional-flush-column-toggle")

    BUFFER_OPTIONS = (By.XPATH, "//ics-toggle[@id ='ispp-id-calibrate-wavelengths-options-using-buffers-toggle']")
    # -- Solvents Screen -- #
    SOLVENT_LINE_A = (By.XPATH, "//mat-radio-button[1]//label[@class='mat-radio-label']")
    SOLVENT_LINE_B = (By.XPATH, "//mat-radio-button[2]//label[@class='mat-radio-label']")
    SOLVENT_LINE_C = (By.XPATH, "//mat-radio-button[3]//label[@class='mat-radio-label']")
    SOLVENT_LINE_D = (By.XPATH, "//mat-radio-button[4]//label[@class='mat-radio-label']")

    FLOW_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@formcontrolname='calibrateFlowControlToggle']//mat-slide-toggle")
    FLOW_EDIT_FIELD = (By.XPATH, "//ics-edit-field//div[contains(@class,'mat-form-field-wrapper')]//input")
    FLOW_EDIT_STATE = (By.XPATH, "//ics-edit-field[@ ng-reflect-unique-id= 'ispp-id-verify-and-calibrate-w']/div")
    CHECK_FOR_LEAK_BUTTON = (By.XPATH, "//mat-checkbox")

    # -- Welcome Screen -- #
    WELCOME_PARA_ONE = (By.XPATH, "//ics-verify-and-calibrate-wavelengths-overview//div[@class='column'][1]//p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//ics-verify-and-calibrate-wavelengths-overview//div[@class='column'][1]//p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//ics-verify-and-calibrate-wavelengths-overview//div[@class='column'][1]//p[3]")
    POINT_ONE_FOR_BETTER_RESULTS_TEXT = (By.XPATH, "//ics-verify-and-calibrate-wavelengths-overview//div[@class='column'][1]//div[2]//li[1]")
    POINT_TWO_FOR_BETTER_RESULTS_TEXT = (By.XPATH, "//ics-verify-and-calibrate-wavelengths-overview//div[@class='column'][1]//div[2]//li[2]")
    RECOMMENDATION_TEXT = (By.XPATH, "//ics-information-card//div[@class='information-card-description']")

    VERIFY_ICON = (
        By.XPATH, "//ics-secondary-panel-footer[1]/div[1]/div[3]//ics-primary-action[1]/div[1]/ics-tray[1]/div[1]")
    REVERIFY_ICON = (By.XPATH, "//ics-tray[@ng-reflect-text ='REVERIFY']//mat-icon")
    WAVELENGTH_TABLE = (
        By.XPATH, "//ics-info-list-item[@class='collapsible-table-header']//ics-table")
    WAVELENGTH_TABLE_DATA = (By.XPATH, "//div[@class='collapsible-table-body expanded']/descendant::div[text()=' Deviation (nm) ']")
    WAVELENGTH_ROW = (By.XPATH,
                      "//ics-info-list-item[@class='collapsible-table-header']//ics-table//div[@class='table']/ul[' + str(row) + ']")

    RESULTS_ARROW = (By.XPATH, "//mat-icon[@class='mat-icon notranslate active mat-icon-no-color']")
    TEST_STATUS = (By.XPATH, "//div[text()=' Calibrate Wavelengths ']/following-sibling::div")
    WAVELENGTH_DEVIATION = "//ics-info-list-item//ics-table//div[@class='table']/ul[3]"
    CALIBRATE_ICON = (By.XPATH,
                      "//ics-secondary-panel-footer[1]/div[1]/div[3]/ics-primary-action[1]/div[1]/ics-tray[@ng-reflect-text='CALIBRATE']")
    WAVELENGTH_ROWS = (
        By.XPATH, "//ics-info-list-item[@class='collapsible-table-header']//ics-table//div[@class='table']/ul")
    LAMP_STATE = (By.XPATH,
                  "//div[@id = 'ispp-id-verify-and-calibrate-wavelengths-pre-conditions']//ics-info-list-item[1]//div[@class='ng-star-inserted']")
    FLOW_CELL_TYPE = (By.XPATH,
                      "//div[@id = 'ispp-id-verify-and-calibrate-wavelengths-pre-conditions']//ics-info-list-item[2]//div[@class='ng-star-inserted']")


class CalibrateWavelengthSummaryLocators:
    PRE_FLUSH_INFO_LABEL = (By.XPATH,
                            "//ics-info-list-item[@id ='ispp-id-verify-and-calibrate-preflush-item']//div[contains(@class, 'subtitle')]/div")
    FLUSH_INFO_LABEL = (By.XPATH,
                        "//ics-info-list-item[@id ='ispp-id-verify-and-calibrate-flush-item']//div[contains(@class, 'subtitle')]/div")
    FLOW_CELL_INFO_LABEL = (By.XPATH,
                            "//ics-info-list-item[@id ='ispp-id-verify-and-calibrate-flow-cell-type-item']//div[contains(@class, 'subtitle')]/div")
    LAMP_INFO_LABEL = (By.XPATH,
                       "//ics-info-list-item[@id ='ispp-id-verify-and-calibrate-lamp-item']//div[contains(@class, 'subtitle')]/div")
    FLOW_INFO_LABEL = (By.XPATH,
                       "//ics-info-list-item[@id ='ispp-id-verify-and-calibrate-flow-rate-item']//div[contains(@class, 'subtitle')]/div")
    SUMMARY_HEADER = (By.XPATH, "//div[@id ='ispp-id-calibrate-wavelengths-workflow-summary']")
    TERMINATE_BANNER = (By.XPATH,
                        "//div[@id = 'ispp-id-Verify and Calibrate Wavelengths-workflow-interruption']//div[@class ='current step']")
    CLOSE_BUTTON_STATE = (By.XPATH, "//ics-tray[@ng-reflect-text ='Close']//div[@class = 'tray-container']/div")
