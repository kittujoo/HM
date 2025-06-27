"""
File_Name: replace_flow_cell_workflow_locators.py
Desc: This file contains locator object of the webelements in the replace flow cell workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/14/22
"""
from selenium.webdriver.common.by import By


class ReplaceFlowCellWorkflowLocators:

    WELCOME_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-welcome")
    CAUTION_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-cautions")
    PRECONDITIONS_SUMMARY_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-preconditions-summary")
    PRECONDITIONS_STATUS_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-preconditions")
    REMOVAL_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-remove-flow-cell")
    FIRST_INSTALLATION_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-install-flow-cell-1")
    SECOND_INSTALLATION_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-install-flow-cell-2")
    FLOW_CONDITIONING_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-conditioning-A")
    SOLVENT_CONDITIONING_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-conditioning-B")
    STATUS_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-status")
    FINISH_BANNER = (By.ID, "ispp-id-replace-flow-cell-workflow-finish")
    START_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")
    CANCEL_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'cancel')]")

class ReplaceFlowCellWelcomeScreenLocators:
    WELCOME_PARA_ONE = (By.XPATH, "//section[@id='replaceFlowCellWorkflowWelcomeSection']//p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//section[@id='replaceFlowCellWorkflowWelcomeSection']//p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//section[@id='replaceFlowCellWorkflowWelcomeSection']//p[3]")

class ReplaceFlowCellCautionScreenLocators:
    HOT_SURFACE_TEXT = (By.XPATH, "//ics-warning-and-caution-item[1]//div[@class='warning-and-caution-item-description']")
    GENERAL_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-item[2]//div[@class='warning-and-caution-item-description']")

class ReplaceFlowCellPreconditionsScreenLocators:
    LAMP_STATE_CHECK_STATUS = (By.XPATH, "//ics-progressing-info-list-item[1]//mat-icon")
    FLOW_STATE_CHECK_STATUS = (By.XPATH, "//ics-progressing-info-list-item[2]//mat-icon")
    POWER_STATE_CHECK_STATUS = (By.XPATH, "//ics-progressing-info-list-item[3]//mat-icon")

class ReplaceFlowCellRemoveScreenLocators:
    REPLACE_STEP_ONE = (By.XPATH, "//ol//li[1]")
    REPLACE_STEP_TWO = (By.XPATH, "//ol//li[2]")
    REPLACE_STEP_THREE = (By.XPATH, "//ol//li[3]")
    REPLACE_STEP_FOUR = (By.XPATH, "//ol//li[4]")

class ReplaceFlowCellInstallScreenLocators:
    #page 1
    INSTALL_STEP_FIVE = (By.XPATH, "//ol//li[1]")
    INSTALL_STEP_SIX = (By.XPATH, "//ol//li[2]")
    INSTALL_STEP_SEVEN = (By.XPATH, "//ol//li[3]")
    INSTALL_STEP_EIGHT = (By.XPATH, "//ol//li[4]")
    # page 2
    INSTALL_STEP_NINE = (By.XPATH, "//ol//li[1]")
    INSTALL_STEP_TEN = (By.XPATH, "//ol//li[2]")
    INSTALL_STEP_ELEVEN = (By.XPATH, "//ol//li[3]")

class ReplaceFlowCellConditioningLocators:
    FLOW_RATE_FIELD = (By.XPATH, "//ics-info-list-item[1]//input")
    FLOW_RATE_FIELD_STATUS = (By.XPATH, "//ics-info-list-item[1]//div[contains(@class,'edit-field')]")
    FLOW_DURATION_FIELD = (By.XPATH, "//ics-info-list-item[2]//input")
    FLOW_DURATION_FIELD_STATUS = (By.XPATH, "//ics-info-list-item[2]//div[contains(@class,'edit-field')]")
    SOLVENT_OPTION_A = (By.XPATH, "//mat-radio-group//mat-radio-button[1]")
    SOLVENT_OPTION_B = (By.XPATH, "//mat-radio-group//mat-radio-button[2]")

class ReplaceFlowCellStatusScreenLocators:
    STATUS_LABEL = (By.XPATH, "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]")
