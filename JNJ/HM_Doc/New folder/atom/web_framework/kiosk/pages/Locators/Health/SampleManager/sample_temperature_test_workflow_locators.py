"""
File_Name: sample_temperature_test_workflow_locators.py
Desc: This file contains locator object of the web elements in the sample temperature test workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 12/15/22
__modified__ = "Tyler Prada" Post-FCS update 7/19/23
"""
from selenium.webdriver.common.by import By


class SampleTemperatureTestLocators:
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-ftn-sample-cooling-workflow-overview")
    PRECONDITIONS_PAGE_BANNER = (By.ID, "ispp-id-ftn-sample-cooling-workflow-pre-conditions")
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-ftn-sample-cooling-workflow-summary")
    STATUS_PAGE_BANNER = (By.ID, "ispp-id-ftn-sample-cooling-workflow-status")
    RESULTS_PAGE_BANNER = (By.ID, "ispp-id-ftn-sample-cooling-workflow-results")
    RESULTS_GRID_ARROW = (By.XPATH, "//ics-info-list-item[@class='collapsible-table-header']//div[contains(@class,'icon')]")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    START_BUTTON = (By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]//div[@class='primary-action']")

    WELCOME_PARA_ONE = (By.XPATH, "//ics-ftn-sample-cooling-test-overview//div[1]/p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//ics-ftn-sample-cooling-test-overview//div[1]/p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//ics-ftn-sample-cooling-test-overview//div[1]/p[3]")

    AMBIENT_TEMPERATURE_STATE = (By.XPATH, "//ics-ftn-sample-cooling-test-preconditions//ics-info-list-item[1]//ics-info-list-item-state//div")
    COMPARTMENT_TEMPERATURE_STATE = (By.XPATH, "//ics-ftn-sample-cooling-test-preconditions//ics-info-list-item[2]//ics-info-list-item-state//div")
    COMPARTMENT_DOOR_STATE = (By.XPATH, "//ics-ftn-sample-cooling-test-preconditions//ics-info-list-item[3]//ics-info-list-item-state//div")
    SAMPLE_TRAY_STATE = (By.XPATH, "//ics-ftn-sample-cooling-test-preconditions//ics-info-list-item[4]//ics-info-list-item-state//div")

    PRECONDITION_CHECKBOX = (By.XPATH, "//mat-checkbox")

    RESULTS_STATUS = (By.XPATH, "//ics-collapsible-table//ics-info-list-item//div[contains(@class, 'header')]//div[contains(@class,'subtitle')][1]//div")
    TARGET_CHANGE = (By.XPATH, "//ics-table//ul[contains(@class,'table-row')][2]//li[contains(@class,'table-row')][2]//div")
    MEASURED_CHANGE = (By.XPATH, "//ics-table//ul[contains(@class,'table-row')][3]//li[contains(@class,'table-row')][2]//div")
    STATUS_BANNER = (By.XPATH, "//div[@id ='ispp-id-ftn-sample-cooling-workflow-status']//div[@class='current step']")
    WORKFLOW_STOPPED_BANNER = (By.XPATH, "//div[contains(text(),'Workflow stopped')]")


class SampleTemperaturesummaryScreenLocators:
    SUMMARY_DOOR_STATE = (By.XPATH, "//ics-ftn-sample-cooling-test-summary//ics-workflow-summary//ul//li[3]/div[2]")
