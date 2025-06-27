"""
File_Name: pump_maintenance_workflow_locators.py
Desc: This file contains locator object of the web elements in the pump maintenance workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/3/22
"""
from selenium.webdriver.common.by import By


class PumpMaintenanceWorkflowLocators:

    WELCOME_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-welcome")
    CAUTIONS_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-cautions")
    PROCEDURE_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-procedure-summary")
    FLUSH_OPTIONS_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-flush")
    FLUSH_SOLVENT_OPTIONS_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-flush-options")
    SUMMARY_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-flush-summary")
    STATUS_BANNER = (By.ID, "ispp-id-pump-head-maintenance-workflow-flush-status")
    FLUSH_START_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")


class PumpMaintenanceWorkflowWelcomeLocators:
    WELCOME_PARAGRAPH = (By.XPATH, "//section//div[1]//p")

    LEFT_LIST_ITEM_ONE = (By.XPATH, "//section//div[2]//td[1]//li[1]")
    LEFT_LIST_ITEM_TWO = (By.XPATH, "//section//div[2]//td[1]//li[2]")
    LEFT_LIST_ITEM_THREE = (By.XPATH, "//section//div[2]//td[1]//li[3]")
    LEFT_LIST_ITEM_FOUR = (By.XPATH, "//section//div[2]//td[1]//li[4]")
    LEFT_LIST_ITEM_FIVE = (By.XPATH, "//section//div[2]//td[1]//li[5]")
    LEFT_LIST_ITEM_SIX = (By.XPATH, "//section//div[2]//td[1]//li[6]")

    RIGHT_LIST_ITEM_ONE = (By.XPATH, "//section//div[2]//td[2]//li[1]")
    RIGHT_LIST_ITEM_TWO = (By.XPATH, "//section//div[2]//td[2]//li[2]")
    RIGHT_LIST_ITEM_THREE = (By.XPATH, "//section//div[2]//td[2]//li[3]")
    RIGHT_LIST_ITEM_FOUR = (By.XPATH, "//section//div[2]//td[2]//li[4]")
    RIGHT_LIST_ITEM_FIVE = (By.XPATH, "//section//div[2]//td[2]//li[5]")


class PumpMaintenanceWorkflowCautionLocators:
    FIRST_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-item[1]//div[contains(@class,'description')]")
    SECOND_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-item[2]//div[contains(@class,'description')]")


class PumpMaintenanceWorkflowProcedureLocators:
    PROCEDURE_TOP_PARAGRAPH = (By.XPATH, "//ics-info-list-item//section[1]")

    PROCEDURE_STEP_ONE = (By.XPATH, "//ics-info-list-item//ol//li[1]")
    PROCEDURE_STEP_TWO = (By.XPATH, "//ics-info-list-item//ol//li[2]")
    PROCEDURE_STEP_THREE = (By.XPATH, "//ics-info-list-item//ol//li[3]")
    PROCEDURE_STEP_FOUR = (By.XPATH, "//ics-info-list-item//ol//li[4]")
    PROCEDURE_STEP_FIVE = (By.XPATH, "//ics-info-list-item//ol//li[5]")
    PROCEDURE_STEP_SIX = (By.XPATH, "//ics-info-list-item//ol//li[6]")
    PROCEDURE_STEP_SEVEN = (By.XPATH, "//ics-info-list-item//ol//li[7]")
    PROCEDURE_STEP_EIGHT = (By.XPATH, "//ics-info-list-item//ol//li[8]")

    PROCEDURE_BOTTOM_PARAGRAPH = (By.XPATH, "//ics-info-list-item//section[2]")


class PumpMaintenanceFlowOptionsLocators:
    FLUSH_DURATION_TOGGLE = (By.XPATH, "//ics-toggle")
    FLUSH_DURATION_FIELD = (By.XPATH, "//ics-edit-field//div[contains(@class,'edit-field')]")
    FLUSH_DURATION_FIELD_VALUE = (By.XPATH, "//ics-edit-field//input")
    DEFAULT_VALUE_BUTTON = (By.XPATH, "//ics-settings-keypad-wrapper//ics-action-button")

    SOLVENT_A_RADIO = (By.XPATH, "//mat-radio-group//mat-radio-button[1]")
    SOLVENT_B_RADIO = (By.XPATH, "//mat-radio-group//mat-radio-button[2]")
    SOLVENT_C_RADIO = (By.XPATH, "//mat-radio-group//mat-radio-button[3]")
    SOLVENT_D_RADIO = (By.XPATH, "//mat-radio-group//mat-radio-button[4]")


class PumpMaintenanceSummaryLocators:
    FLUSH_PARAMS_INFO_LABEL = (By.XPATH, "//ics-pump-head-maintenance-flush-summary//ics-info-list-item[1]//div[contains(@class,'subtitle')][1]")
