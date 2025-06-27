"""
File_Name: needle_seal_readiness_workflow_locators.py
Desc: This file contains locator object of the web elements in the needle seal readiness leak test workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 5/17/22
__modified = "Tyler Prada" Locator changes for pressure unit validation 6/22/23
"""
from selenium.webdriver.common.by import By


class NeedleSealReadinessLocators:
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-ftn-needle-seal-readiness-test-overview-workflow")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    START_BUTTON = (
        By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH,
                     "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//"
                     "div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]//div[@class='primary-action']")


class NeedleSealReadinessWelcomeLocators:
    WELCOME_PARAGRAPH_ONE = (
        By.XPATH, "//ics-ftn-needle-seal-readiness-test-overview//div[@class='column'][1]//p[1]")
    WELCOME_PARAGRAPH_TWO = (
        By.XPATH, "//ics-ftn-needle-seal-readiness-test-overview//div[@class='column'][1]//p[2]")
    WELCOME_PARAGRAPH_THREE = (
        By.XPATH, "//ics-ftn-needle-seal-readiness-test-overview//div[@class='column'][1]//p[3]")
    WELCOME_LIST_PARAGRAPH = (
        By.XPATH, "//ics-ftn-needle-seal-readiness-test-overview//div[@class='column'][1]//p[4]")
    WELCOME_LIST_ITEM_ONE = (
        By.XPATH, "//ics-ftn-needle-seal-readiness-test-overview//div[@class='column'][1]//ul//li[1]")
    WELCOME_LIST_ITEM_TWO = (
        By.XPATH, "//ics-ftn-needle-seal-readiness-test-overview//div[@class='column'][1]//ul//li[2]")
    WELCOME_PARAGRAPH_FOUR = (
        By.XPATH, "//article[@id='ics-cms-ftn-needle-seal-readiness-test-workflow-overview']//p[6]")

class NeedleSealReadinessSetupLocators:
    SETUP_BANNER = (By.XPATH,
                    "//div[@id ='ispp-id-ftn-needle-seal-readiness-test-setup-workflow']//div[@class='current step']")
    COMPOSITION_BANNER = (By.XPATH,
                    "//div[@id ='ispp-id-ftn-needle-seal-readiness-test-composition-workflow']//div[@class='current step']")
    FLOW_RATE_FIELD = (By.XPATH, "//ics-edit-field//input")
    SETUP_LINE_ONE = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[1]")
    SETUP_LINE_TWO = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[2]")
    COMP_TEXT_ONE = (By.XPATH,
                     "//ics-modal-info-keypad[@class ='ftn-needle-seal-readiness-test-solvent-composition-container']//"
                     "section[1]")
    COMP_TEXT_TWO = (By.XPATH,
                     "//ics-modal-info-keypad[@class ='ftn-needle-seal-readiness-test-solvent-composition-container']//"
                     "section[2]")
    FLOW_EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id= 'ispp-id-ftn-needle-seal-readin']/div")
    COMP_EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@id= 'editField_1']/div")
    FlOW_HINT_FIELD = (By.XPATH, "//mat-hint[@id ='ispp-id-hint-editField']")
    COMP_HINT_FIELD = (By.XPATH, "//ics-edit-field[@id='editField_0']//mat-hint[@id ='ispp-id-hint-editField']")


class NeedleSealReadinessSummaryLocators:
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-ftn-needle-seal-readiness-test-summary-workflow")
    STATUS_BANNER = (By.ID, "ispp-id-ftn-needle-seal-readiness-test-status-workflow")
    RESULTS_BANNER = (By.ID, "ispp-id-ftn-needle-seal-readiness-test-collapsible-table")
    FLOW_RATE_INFO_LABEL = (By.XPATH, "//ul[@class='workflow-summary']//li[1]//div[2]")
    COMPOSITION_LABEL = (By.XPATH, "//ul[@class='workflow-summary']//li[2]//div[2]")
    SYSTEM_PRESSURE_INFO_LABEL = (By.XPATH, "//ul[@class='workflow-summary']//li[3]//div[2]")
    TEST_TIME_INFO_LABEL = (By.XPATH, "//ul[@class='workflow-summary']//li[3]//div[2]")
    SUMMARY_LINE_ONE = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[1]")
    SUMMARY_LINE_TWO = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[2]")
    SUMMARY_LINE_THREE = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[3]")


class NeedleSealReadinessResultsLocators:
    STATUS_BANNER = (
        By.XPATH, "//div[@id ='ispp-id-ftn-needle-seal-readiness-test-status-workflow']//div[@class='current step']")
    STATUS_LINE_ONE = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[1]")
    STATUS_LINE_TWO = (By.XPATH, "//ics-modal-info-keypad[contains(@class,'seal')]//section[2]")
    RESULTS_BANNER = (By.ID, "ispp-id-ftn-needle-seal-readiness-test-collapsible-table")
    RESULTS_SHOW_ICON_STATUS = (By.XPATH,
                                "//ics-collapsible-table[@id ='ispp-id-ftn-needle-seal-readiness-test-collapsible-table']//"
                                "ics-info-list-item[@ng-reflect-title='Needle Seal Readiness Test']")
    PRESSURE_DIFFERENCE_LABEL = (By.XPATH, "//ics-table//ul//li[2]//li/div")
    FLOW_RATE_INFO = (By.XPATH, "//ics-table//ul[2]//li[2]//li/div")
    RESULTS_LINE_ONE = (By.XPATH, "//ics-modal-info[@id ='ispp-id-ftn-needle-seal-readiness-test-results']//section[1]")
    RESULTS_LINE_TWO = (By.XPATH, "//ics-modal-info[@id ='ispp-id-ftn-needle-seal-readiness-test-results']//section[2]")
    RESULTS_SHOW_ICON = (By.XPATH,
                         "//ics-collapsible-table[@id ='ispp-id-ftn-needle-seal-readiness-test-collapsible-table']//"
                         "ics-info-list-item[@ng-reflect-title='Needle Seal Readiness Test']//"
                         "div[contains(@class,'icon')]//mat-icon")
    TEST_RESULT = (By.XPATH, "//ics-info-list-item[@class='collapsible-table-header']//div[contains(@class,'info-list-item-subtitle')]/div")
