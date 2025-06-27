"""
File_Name: heater_cooler_workflow_locators.py
Desc: This file contains locator object of the web elements in the heater/cooler workflow screens
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 1/14/2021
__modified__ = "Tyler Prada" Added welcome text locators 1/20/22
__modified__ = "Tyler Prada" Added summary and result screen locators 2/15/22
__modified__ = "Tyler Prada" Adjustments due to workflow changes & results rework 7/22/22
"""
from selenium.webdriver.common.by import By


class HeaterCoolerWorkflowLocators:
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-column-heater-cooler-workflow-overview")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    START_BUTTON = (By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'primary-action-done')]")


class HeaterCoolerWelcomeLocators:
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//ics-column-heater-cooler-test-overview//div[@class='column'][1]//p[1]")
    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//ics-column-heater-cooler-test-overview//div[@class='column'][1]//p[2]")


class HeaterCoolerPreconditionLocators:
    PRECONDITION_PAGE_BANNER = (By.ID, "ispp-id-column-heater-cooler-workflow-pre-conditions")
    CONFIRMATION_CHECK = (By.XPATH, "//mat-checkbox")
    AMBIENT_TEMPERATURE_INFO_LABEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Ambient Temperature']//div[contains(@class,'subtitle')][1]")
    COLUMN_TEMPERATURE_INFO_LABEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Compartment Temperature']//div[contains(@class,'subtitle')][1]")
    COLUMN_DOOR_INFO_LABEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Compartment Door']//div[contains(@class,'subtitle')][1]")


class HeaterCoolerSummaryLocators:
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-column-heater-cooler-workflow-summary")
    AMBIENT_TEMPERATURE_INFO_LABEL = (By.XPATH, "//ics-workflow-summary//ul//li[1]//div[2]")
    COLUMN_TEMPERATURE_INFO_LABEL = (By.XPATH, "//ics-workflow-summary//ul//li[2]//div[2]")
    COLUMN_DOOR_INFO_LABEL = (By.XPATH, "//ics-workflow-summary//ul//li[3]//div[2]")
    TIME_ESTIMATE_INFO_LABEL = (By.XPATH, "//ics-workflow-summary//ul//li[4]//div[2]")
    PROGRESS_BANNER = (By.ID, "ispp-id-column-heater-cooler-workflow-status")
    COLUMN_DOOR_STATE = (By.XPATH, "//ics-column-heater-cooler-test-summary//ics-workflow-summary//ul//li[3]/div[2]")
    STATUS_BANNER = (By.XPATH, "//div[@id ='ispp-id-column-heater-cooler-workflow-status']//div[@class='current step']")
    WORKFLOW_STOPPED_BANNER = (By.XPATH, "//div[contains(text(),'Workflow stopped')]")


class HeaterCoolerResultsLocators:
    RESULTS_PAGE_BANNER = (By.ID, "ispp-id-column-heater-cooler-workflow-results")
    RESULTS_TABLE_TOGGLE = (By.XPATH, "//div[@class='info-list-item-content active']//div[@class='item-icon-position ng-star-inserted']")
    AMBIENT_TEMPERATURE_INFO_LABEL = (By.XPATH, "//ics-table//div//ul[contains(@class,'table-row')][1]//li[2]//div")
    RESULTS_STATUS = (By.XPATH, "//ics-collapsible-table//ics-info-list-item//div[contains(@class, 'header')]//div[contains(@class,'subtitle')][1]//div")
    TARGET_RATE_INFO_LABEL = (By.XPATH, "//ics-table//div//ul[contains(@class,'table-row')][2]//li[2]//div")
    MEASURED_RATE_INFO_LABEL = (By.XPATH, "//ics-table//div//ul[contains(@class,'table-row')][3]//li[2]//div")
