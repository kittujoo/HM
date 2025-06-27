"""
File_Name: replace_column_workflow_locators.py
Desc: This file contains locator object of the webelements in the replace column workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 9/21/22
"""
from selenium.webdriver.common.by import By


class ReplaceColumnWorkflowLocators:

    WELCOME_BANNER = (By.ID, "ispp-id-replace-column-overview-workflow")
    CAUTION_BANNER = (By.ID, "ispp-id-replace-column-caution-workflow")
    FLUSH_COLUMN_BANNER = (By.ID, "ispp-id-replace-column-flush-workflow")
    FLUSH_COLUMN_COMPOSITION_BANNER = (By.ID, "ispp-id-replace-column-flush-composition-workflow")
    FLUSH_COLUMN_SUMMARY_BANNER = (By.ID, "ispp-id-replace-column-flush-summary-workflow")
    FLUSH_COLUMN_STATUS_BANNER = (By.ID, "ispp-id-replace-column-flush-status-workflow")
    PRECONDITIONS_BANNER = (By.ID, "ispp-id-replace-columnpre-conditions-workflow")
    REMOVE_BANNER = (By.ID, "ispp-id-replace-column-remove-workflow")
    INSTALL_BANNER = (By.ID, "ispp-id-replace-column-install-workflow")
    NEW_COLUMN_BANNER = (By.XPATH, "ispp-id-replace-column-new-column-workflow")
    NEW_COLUMN_OPTIONS_BANNER = (By.XPATH, "ispp-id-replace-column-new-column-options-workflow")
    CONDITION_COLUMN_BANNER = (By.ID, "ispp-id-replace-column-condition-column-workflow")
    CONDITION_SOLVENTS_COLUMN_BANNER = (By.ID, "ispp-id-replace-column-condition-solvents-workflow")
    CONDITION_DURATION_COLUMN_BANNER = (By.ID, "ispp-id-replace-column-condition-duration-workflow")
    COLUMN_SUMMARY_BANNER = (By.ID, "ispp-id-replace-column-summary-workflow")
    COLUMN_STATUS_BANNER = (By.ID, "ispp-id-replace-column-status")
    COLUMN_RESULTS_BANNER = (By.ID, "ispp-id-replace-column-results-workflow")

    START_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")

    FLUSH_COLUMN_TOGGLE = (By.XPATH, "//ics-toggle//mat-slide-toggle")
    FLOW_RATE_FIELD = (By.XPATH, "//ics-edit-field//input")
    FLUSH_DURATION_STEPPER = (By.XPATH, "//ics-input-stepper")

    FLUSH_COLUMN_STATUS_LABEL = (By.XPATH, "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]")

    FLUSH_COLUMN_COMPOSITION_LABEL = (By.XPATH, "//ics-workflow-summary//ul//li[1]//div[2]")

    COMPARTMENT_TEMPERATURE_STATUS_ICON = (By.XPATH, "//ics-info-list[@id='ispp-id-replace-column-preconditions-infoList']//ics-info-list-item[1]//div[contains(@class,'info-list-state-container')]")
    FLOW_CONTROL_STATUS_ICON = (By.XPATH, "//ics-info-list[@id='ispp-id-replace-column-preconditions-infoList']//ics-info-list-item[2]//div[contains(@class,'info-list-state-container')]")

    CONDITION_COLUMN_TOGGLE = (By.XPATH, "//ics-toggle//mat-slide-toggle")
    CONDITION_COLUMN_FLOW_RATE_FIELD = (By.XPATH, "//ics-edit-field//input")
    CONDITION_DURATION_STEPPER = (By.XPATH, "//ics-input-stepper")
    CONDITION_COLUMN_STATUS_LABEL = (By.XPATH, "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]")

class ReplaceColumnWelcomeScreenLocators:
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//section//p[1]")
    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//section//p[2]")
    WELCOME_LIST_ITEM_ONE = (By.XPATH, "//section//div//div//li[1]")
    WELCOME_LIST_ITEM_TWO = (By.XPATH, "//section//div//div//li[2]")
    WELCOME_LIST_ITEM_THREE = (By.XPATH, "//section//div//div//li[3]")

class ReplaceColumnCautionScreenLocators:
    HOT_SURFACE_PARAGRAPH = (By.XPATH, "//ics-warning-and-caution-item[1]//div[@class='warning-and-caution-item-description']")
    CORROSIVE_MATERIALS_PARAGRAPH = (By.XPATH, "//ics-warning-and-caution-item[2]//div[@class='warning-and-caution-item-description']")
    CAUTION_PARAGRAPH = (By.XPATH, "//ics-warning-and-caution-item[3]//div[@class='warning-and-caution-item-description']")


class ReplaceColumnNewColumnScreenLocators:
    SERIAL_NUMBER_INFO_LABEL = (By.XPATH, "//ics-replace-column-new-column//ics-info-list-item[1]//div[contains(@class,'subtitle')][1]")
    PART_NUMBER_INFO_LABEL = (By.XPATH, "//ics-replace-column-new-column//ics-info-list-item[2]//div[contains(@class,'subtitle')][1]")
    DESCRIPTION_INFO_LABEL = (By.XPATH, "//ics-replace-column-new-column//ics-info-list-item[3]//div[contains(@class,'subtitle')][1]")
