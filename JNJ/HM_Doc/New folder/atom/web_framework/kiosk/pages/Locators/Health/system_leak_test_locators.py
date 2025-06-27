"""
File_Name: system_leak_test_locators.py
Desc: This file contains locator object of the web elements in the dynamic leak test workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila" Initial Check-in 05/11/2022
__modified = "Tyler Prada" Locators for pressure unit validation 6/22/23
__modified = "Supreet Sethi" Added locator for accumulator target pressure hint validation 12/07/2023
"""
from selenium.webdriver.common.by import By


class SystemLeakTestLocators:
    DYNAMIC_LEAK_TEST_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='System Leak Test']")


class SystemLeakTestWorkflowLocators:
    WELCOME_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Welcome')]")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    CANCEL_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'cancel')]")
    WELCOME_PARA_ONE = (By.XPATH, "//ics-leak-test-overview//div/p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//ics-leak-test-overview//div/p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//ics-leak-test-overview//div/p[3]")
    POINT_ONE_FOR_BETTER_RESULTS_TEXT = (
        By.XPATH, "//ics-leak-test-overview//div//ul/li[1]")
    POINT_TWO_FOR_BETTER_RESULTS_TEXT = (
        By.XPATH, "//ics-leak-test-overview//div//ul/li[2]")
    POINT_THREE_FOR_BETTER_RESULTS_TEXT = (
        By.XPATH, "//ics-leak-test-overview//div//ul/li[3]")
    LAST_TESTED_ON_INFO = (
        By.XPATH, "//div[@class ='column'][2]//div[@class='module'][1]//section[1]//div[class='subtitle']")
    RECOMMENDATION_TEXT = (By.XPATH, "//div[@class= 'information-card-description']")


class SystemLeakTestWorkflowSetupLocators:
    SETUP_SOLVENT_LINE_BANNER = (By.ID, "ispp-id-leak-test-workflow-setup-solvent-lines")
    SETUP_TEST_OPTIONS_BANNER = (By.ID, "ispp-id-leak-test-workflow-setup-options")
    SETUP_CUSTOM_OPTIONS_BANNER = (By.ID, "ispp-id-leak-test-workflow-setup-custom-settings")
    SETUP_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Setup')]")
    SOLVENT_LINE_A = (By.XPATH, "//mat-radio-button[@ng-reflect-value='SolventLine_A']")
    SOLVENT_LINE_B = (By.XPATH, "//mat-radio-button[@ng-reflect-value='SolventLine_B']")
    SOLVENT_LINE_C = (By.XPATH, "//mat-radio-button[@ng-reflect-value='SolventLine_C']")
    SOLVENT_LINE_D = (By.XPATH, "//mat-radio-button[@ng-reflect-value='SolventLine_D']")
    STANDARD_TEST_PANEL = (
        By.XPATH, "//ics-info-list-icon[@id ='leak-test-setup-options-standard']//ics-info-list-item")
    CUSTOM_TEST_PANEL = (By.XPATH, "//ics-info-list-icon[@id ='leak-test-setup-options-custom']//ics-info-list-item")
    ACCUMULATOR_TARGET_HEADER = (By.XPATH, "//form//ics-info-list-item[1]//div[@class='pressure-text']")
    ACCUMULATOR_TARGET_PRESSURE_HINT = (By.XPATH, "//mat-hint[@id='ispp-id-hint-editField']")
    PRIMARY_TARGET_HEADER = (By.XPATH, "//form//ics-info-list-item[2]//div[@class='pressure-text']")
    ACCUMULATOR_TARGET_CHECKBOX = (
        By.XPATH,
        "//ics-modal-info-keypad[@id ='leak-test-target-pressures-body']//ics-info-list-item[1]//mat-checkbox")
    PRIMARY_TARGET_CHECKBOX = (
        By.XPATH,
        "//ics-modal-info-keypad[@id ='leak-test-target-pressures-body']//ics-info-list-item[2]//mat-checkbox")
    ACCUMULATOR_TARGET_FIELD = (By.XPATH, "//div[contains(text(),' Accumulator Target Pressure (psi) ')]/parent::div//input[@type='text'][1]")
    PRIMARY_TARGET_FIELD = (
        By.XPATH, "//div[contains(text(),' Primary Target Pressure (psi) ')]/parent::div//input[@type='text'][1]")
    END_POINT_VENT_VALVE_OPTION = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title ='End Point']//ics-core-selector//ul[1]//li[1]")
    END_POINT_COLUMN_OPTION = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title ='End Point']//ics-core-selector//ul[1]//li[2]")
    DO_NOT_PRIME_OPTION = (
        By.XPATH, "//ics-info-list-item[2]//ics-core-selector//div[@class='ics-core-selector']//li[1]")
    DO_PRIME_OPTION = (
        By.XPATH, "//ics-info-list-item[2]//ics-core-selector//div[@class='ics-core-selector']//li[2]")
    DO_NOT_RETRY_OPTION = (
        By.XPATH, "//ics-info-list-item[3]//ics-core-selector//div[@class='ics-core-selector']//li[1]")
    ONE_TIMES_RETRY_OPTION = (
        By.XPATH, "//ics-info-list-item[3]//ics-core-selector//div[@class='ics-core-selector']//li[2]")
    FIVE_TIMES_RETRY_OPTION = (
        By.XPATH, "//ics-info-list-item[3]//ics-core-selector//div[@class='ics-core-selector']//li[3]")
    EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id ='isppK-id-leakTest-accumulatorP']/div")


class SystemLeakTestWorkFlowSummaryLocators:
    SUMMARY_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Summary')]")
    SOLVENT_INFO_LABEL = (
        By.XPATH,
        "//div[text()=' Solvent ']//following-sibling::div")
    ACCUMULATOR_TARGET_INFO_LABEL = (
        By.XPATH,
        "//div[text()=' Accumulator Target Pressure ']//following-sibling::div")
    PRIMARY_TARGET_INFO_LABEL = (
        By.XPATH,
        "//div[text()=' Primary Target Pressure ']//following-sibling::div")
    ENDPOINT_INFO_LABEL = (
        By.XPATH,
        " //div[text()=' End Point ']//following-sibling::div")
    TEST_FAIL_INFO_LABEL = (
        By.XPATH,
        " //div[text()=' When Test Fails ']//following-sibling::div")
    TIME_ESTIMATE_INFO_LABEL = (
        By.XPATH,
        "//div[text()=' Estimated Time ']//following-sibling::div")
    START_BUTTON = (
        By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    PRIME_OPTION_LABEL = (By.XPATH, "//div[text()=' Priming Option ']//following-sibling::div")


class SystemLeakTestWorkflowPrimingLocators:
    PRIMING_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Status: Priming')]")
    PRIMARY_TARGET_PRESSURE = (
        By.XPATH, "//div[@class='pressure-card leak-test-primary-pressure']//div[@class='pressure-card-subtitle']")
    ACCUMULATOR_TARGET_PRESSURE = (
        By.XPATH,
        "//div[@class='pressure-card leak-test-accumulator-pressure']//div[@class='pressure-card-subtitle']//div")
    STOP_BUTTON = (By.XPATH, "//ics-primary-action//mat-icon")


class SystemLeakTestWorkflowResultsLocators:
    RESULTS_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Results')]")
    RESULTS_HEADER = (By.XPATH, "//div[@class ='secondary-panel-workflow-header-content']//div[@class='current step']")
    ACCUMULATOR_STATUS = (By.XPATH, "//div[contains(@class,'results')]//li[2]//div[contains(@class,'status')]")
    PRIMARY_STATUS = (By.XPATH, "//div[contains(@class,'results')]//li[3]//div[contains(@class,'status')]")
    DETAILS_PANEL = (By.XPATH, "//div[@class='more']")
    ACCUMULATOR_LEAK_RATE = (By.XPATH, "//ul[@class='table-row odd ng-star-inserted'][2]//li[3]")
    PRIMARY_LEAK_RATE = (By.XPATH, "//ul[@class='table-row odd ng-star-inserted'][2]//li[3]")
    ACCUMULATOR_MAX_PRESSURE = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][2]//li[2]")
    PRIMARY_MAX_PRESSURE = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][2]//li[3]")
    ACCUMULATOR_STROKE_PERCENT = (By.XPATH, "//ul[@class='table-row odd ng-star-inserted'][3]//li[2]")
    PRIMARY_STROKE_PERCENT = (By.XPATH, "//ul[@class='table-row odd ng-star-inserted'][3]//li[3]")
    ACCUMULATOR_ATTEMPTS = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][3]//li[2]")
    PRIMARY_ATTEMPTS = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][3]//li[3]")
    ARROW_STATUS = (By.XPATH, "//div[@id ='leak-test-results']//ics-info-list-item")
    PRIMARY_RESULT_STATE = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][1]//li[3]")
    ACCUMULATOR_RESULT_STATE = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][1]//li[2]")
    EXTEND_ICON = (
        By.XPATH, "//div[@id = 'leak-test-results']//div[@class='item-icon-position ng-star-inserted']//mat-icon")
    STOP_BUTTON_STATE = (
        By.XPATH, "//ics-primary-action//ics-tray[@ng-reflect-text='Close']//div[@class ='tray-container']//div")


class SystemLeakTestSinglePressureLocators:
    PRIMARY_RESULT_STATE = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][1]//li[2]")
    PRIMARY_MAX_PRESSURE = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][2]//li[2]")
    PRIMARY_LEAK_RATE = (By.XPATH, "//ul[@class='table-row odd ng-star-inserted'][1]//li[2]")
    PRIMARY_STROKE_PERCENT = (By.XPATH, "//ul[@class='table-row odd ng-star-inserted'][2]//li[2]")
    PRIMARY_ATTEMPTS = (By.XPATH, "//ul[@class='table-row even ng-star-inserted'][3]//li[2]")
