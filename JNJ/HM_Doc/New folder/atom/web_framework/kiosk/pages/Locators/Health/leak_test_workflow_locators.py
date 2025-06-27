"""
File_Name: leak_test_workflow_locators.py
Desc: This file contains locator object of the web elements in the leak test workflow screens
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/24/2021
__modified__ = "Sharmila Vairamani" Locators for the welcome screen
__modified__ = "Tyler Prada" Adjustments for leak test moving to health screen 2/21/22
"""
from selenium.webdriver.common.by import By


class LeakTestWorkflowLocators:
    WELCOME_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Welcome')]")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    WELCOME_PARA_ONE = (By.XPATH, "//ics-leak-test-overview//div[@class='column'][1]//section[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//ics-leak-test-overview//div[@class='column'][1]//section[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//ics-leak-test-overview//div[@class='column'][1]//section[3]")
    POINT_ONE_FOR_BETTER_RESULTS_TEXT = (By.XPATH, "//ics-leak-test-overview//div[@class='column'][1]//section[4]//li[1]")
    POINT_TWO_FOR_BETTER_RESULTS_TEXT = (By.XPATH, "//ics-leak-test-overview//div[@class='column'][1]//section[4]//li[2]")
    POINT_THREE_FOR_BETTER_RESULTS_TEXT = (By.XPATH, "//ics-leak-test-overview//div[@class='column'][1]//section[4]//li[3]")
    LAST_TESTED_ON_INFO = (
        By.XPATH, "//div[@class ='column'][2]//div[@class='module'][1]//section[1]//div[class='subtitle']")
    RECOMMENDATION_TEXT = (By.XPATH, "//div[@class= 'information-card-description']")


class LeakTestWorkflowSetupLocators:
    SETUP_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Setup')]")
    SOLVENT_LINE_A = (By.XPATH, "//mat-radio-button[@ng-reflect-value='A']")
    SOLVENT_LINE_B = (By.XPATH, "//mat-radio-button[@ng-reflect-value='B']")
    SOLVENT_LINE_C = (By.XPATH, "//mat-radio-button[@ng-reflect-value='C']")
    SOLVENT_LINE_D = (By.XPATH, "//mat-radio-button[@ng-reflect-value='D']")
    STANDARD_TEST_PANEL = (
        By.XPATH, "//ics-info-list-icon[@id ='leak-test-setup-options-standard']//ics-info-list-item")
    CUSTOM_TEST_PANEL = (By.XPATH, "//ics-info-list[2]")
    ACCUMULATOR_TARGET_CHECKBOX = (By.XPATH, "//div[@class='mat-checkbox-inner-container'][1]")
    PRIMARY_TARGET_CHECKBOX = (
        By.XPATH, "//ics-modal-info-keypad[@id ='leak-test-target-pressures-body']//ics-info-list-item[2]//label")
    ACCUMULATOR_TARGET_FIELD = (By.XPATH, "//input[@type='text'][1]")
    PRIMARY_TARGET_FIELD = (
        By.XPATH, "//ics-edit-field[@ng-reflect-unique-id = 'isppK-id-leakTest-primaryPress']//input")
    END_POINT_VENT_VALVE_OPTION = (By.XPATH, "//ics-core-selector//li[contains(text(),'Vent Valve')]")
    END_POINT_COLUMN_OPTION = (By.XPATH, "//ics-core-selector//li[contains(text(),'Column')]")
    DO_NOT_PRIME_OPTION = (
        By.XPATH, "//ics-info-list-item[2]//ics-core-selector//div[@class='ics-core-selector']//li[1]")
    PRIME_FOR_TWO_MIN_OPTION = (
        By.XPATH, "//ics-info-list-item[2]//ics-core-selector//div[@class='ics-core-selector']//li[2]")
    DO_NOT_RETRY_OPTION = (
        By.XPATH, "//ics-info-list-item[3]//ics-core-selector//div[@class='ics-core-selector']//li[1]")
    ONE_TIMES_RETRY_OPTION = (
        By.XPATH, "//ics-info-list-item[3]//ics-core-selector//div[@class='ics-core-selector']//li[2]")
    FIVE_TIMES_RETRY_OPTION = (
        By.XPATH, "//ics-info-list-item[3]//ics-core-selector//div[@class='ics-core-selector']//li[3]")
    EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id ='isppK-id-leakTest-accumulatorP']/div")


class LeakTestWorkFlowSummaryLocators:
    SUMMARY_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Summary')]")
    SOLVENT_INFO_LABEL = (
        By.XPATH,
        "//div[@class='leak-test-summary']//li[1]//div[@class='workflow-summary-item-subtitle ng-star-inserted']")
    ACCUMULATOR_TARGET_INFO_LABEL = (
        By.XPATH,
        "//div[@class='leak-test-summary']//li[2]//div[@class='workflow-summary-item-subtitle ng-star-inserted']")
    PRIMARY_TARGET_INFO_LABEL = (
        By.XPATH,
        "//div[@class='leak-test-summary']//li[3]//div[@class='workflow-summary-item-subtitle ng-star-inserted']")
    ENDPOINT_INFO_LABEL = (
        By.XPATH,
        "//div[@class='leak-test-summary']//li[4]//div[@class='workflow-summary-item-subtitle ng-star-inserted']")
    TEST_FAIL_INFO_LABEL = (
        By.XPATH,
        "//div[@class='leak-test-summary']//li[5]//div[@class='workflow-summary-item-subtitle ng-star-inserted']")
    TIME_ESTIMATE_INFO_LABEL = (
        By.XPATH,
        "//div[@class='leak-test-summary']//li[6]//div[@class='workflow-summary-item-subtitle ng-star-inserted']")
    START_BUTTON = (
        By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")


class LeakTestWorkflowPrimingLocators:
    PRIMING_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Status: Priming')]")
    PRIMARY_TARGET_PRESSURE = (
        By.XPATH, "//div[@class='pressure-card leak-test-primary-pressure']//div[@class='pressure-card-subtitle']")
    ACCUMULATOR_TARGET_PRESSURE = (
        By.XPATH,
        "//div[@class='pressure-card leak-test-accumulator-pressure']//div[@class='pressure-card-subtitle']//div")
    STOP_BUTTON = (By.XPATH, "//ics-primary-action//mat-icon")


class LeakTestWorkflowResultsLocators:
    RESULTS_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Results')]")
    ACCUMULATOR_STATUS = (By.XPATH, "//div[contains(@class,'results')]//li[2]//div[contains(@class,'status')]")
    PRIMARY_STATUS = (By.XPATH, "//div[contains(@class,'results')]//li[3]//div[contains(@class,'status')]")
    DETAILS_PANEL = (By.XPATH, "//div[@class='more']")
    ACCUMULATOR_LEAK_RATE = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[2]//li[2]")
    PRIMARY_LEAK_RATE = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[2]//li[3]")
    ACCUMULATOR_MAX_PRESSURE = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[3]//li[2]")
    PRIMARY_MAX_PRESSURE = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[3]//li[3]")
    ACCUMULATOR_STROKE_PERCENT = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[4]//li[2]")
    PRIMARY_STROKE_PERCENT = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[4]//li[3]")
    ACCUMULATOR_ATTEMPTS = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[5]//li[2]")
    PRIMARY_ATTEMPTS = (By.XPATH, "//div[@class='details ng-star-inserted expanded']//ul[5]//li[3]")
