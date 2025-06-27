"""
File_Name: sample_metering_pump_workflow_locators.py
Desc: This file contains locator object of the web elements in the sample metering pump leak test workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 5/10/22
__modified__ = "Tyler Prada" added results locators 6/27/22
__modified__ = "Tyler Prada" Post FCS adjustments 6/13/23
__modified = "Tyler Prada" Locators for pressure unit validation 6/22/23
__modified = "Supreet Sethi" Added locator for target pressure hint validation 12/07/2023
"""
from selenium.webdriver.common.by import By


class SampleMeteringPumpLocators:
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-overview")
    START_BUTTON = (By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//"
                              "div[@class='primary-action']/ics-tray")
    CANCEL_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//"
                               "div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]//div[@class='primary-action']")


class SampleMeteringPumpWelcomeLocators:
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//ics-ftn-sample-metering-pump-leak-test-overview//div[@class='column'][1]//p[1]")
    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//ics-ftn-sample-metering-pump-leak-test-overview//div[@class='column'][1]//p[2]")


class SampleMeteringPumpSetupLocators:
    SOLVENT_SETUP_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-setup-composition")

    PRIME_SETUP_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-setup-prime")
    PRIME_TOGGLE = (By.XPATH, "//ics-toggle[@id='ispp-id-ftn-sample-metering-pump-leak-test-setup-toggle']//"
                              "mat-slide-toggle")
    TARGET_PRESSURE_HEADER = (By.XPATH, "//ics-ftn-sample-metering-pump-leak-test-setup-prime//ics-info-list-item[2]//"
                                        "div[contains(@class,'info-list-item-title')]")
    PRESSURE_FIELD = (By.XPATH, "//ics-edit-field//div[contains(@class,'edit-field')]")
    PRESSURE_TEXT_FIELD = (By.XPATH, "//ics-edit-field//div[contains(@class,'edit-field')]//input")

    TARGET_PRESSURE_HINT = (By.XPATH, "//mat-hint[@id='ispp-id-hint-editField']")


class SampleMeteringPumpSummaryLocators:
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-summary")
    COMPOSITION_LABEL = (By.XPATH, "//ul[@class='workflow-summary']//li[1]//div[2]")
    PRIMING_OPTION_INFO_LABEL = (By.XPATH, "//ics-workflow-summary//li[2]//div[2]")
    TARGET_PRESSURE_INFO_LABEL = (By.XPATH, "//ics-workflow-summary//li[3]//div[2]")
    IN_PROGRESS_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-status")
    RESULTS_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-results")


class SampleMeteringPumpStatusLocators:
    STOP_BUTTON = (By.XPATH, "//div[contains(@class,'secondary')]//ics-primary-action")


class SampleMeteringPumpResultsLocators:
    RESULTS_PAGE_BANNER = (By.ID, "ispp-id-sample-metering-pump-leak-test-workflow-results")
    TABLE_TOGGLE_ARROW = (By.XPATH, "//ics-collapsible-table//div[@class='item-icon-position ng-star-inserted']")
    LEAK_RATE_INFO_LABEL = (By.XPATH, "//div[contains(@class,'collapsible-table-body')]//ul//li[2]//ul//li//div")
    WORKFLOW_STOPPED_BANNER = (By.XPATH, "//div[contains(text(),'Workflow stopped unexpectedly')]")


class SampleMeteringPumpLogScreenLocators:
    SampleMeteringPumpLogSource = (By.XPATH, "//ul[2]/li[3]//div[contains(text(), 'SystemMeteringPumpLeakTest')]")
