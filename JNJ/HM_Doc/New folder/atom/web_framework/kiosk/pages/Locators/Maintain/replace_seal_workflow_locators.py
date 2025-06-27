"""
File_Name: replace_seal_workflow_locators.py
Desc: This file contains locator object of the webelements in the replace seal workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/27/22
"""
from selenium.webdriver.common.by import By


class ReplaceSealWorkflowLocators:

    WELCOME_BANNER = (By.ID, "ispp-id-replace-seal-workflow-welcome")
    CAUTIONS_BANNER = (By.ID, "ispp-id-replace-seal-workflow-cautions")
    PRECONDITIONS_BANNER = (By.ID, "ispp-id-replace-seal-workflow-preconditions")
    CARRIAGE_STATUS_BANNER = (By.ID, "ispp-id-replace-seal-workflow-status")
    PROCEDURE_ONE_BANNER = (By.ID, "ispp-id-replace-seal-workflow-procedure1")
    PROCEDURE_TWO_BANNER = (By.ID, "ispp-id-replace-seal-workflow-procedure2")
    SEAL_TEST_STATUS_BANNER = (By.ID, "ispp-id-replace-seal-workflow-running-tests")
    START_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")

class ReplaceSealWorkflowWelcomeLocators:
    WELCOME_PARA_ONE = (By.XPATH, "//section[@id='replaceSealWorkflowWelcomeSection']//p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//section[@id='replaceSealWorkflowWelcomeSection']//p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//section[@id='replaceSealWorkflowWelcomeSection']//p[3]")

class ReplaceSealWorkflowCautionLocators:
    CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-list//ics-warning-and-caution-item[1]//div[@class='warning-and-caution-item-description']")

class ReplaceSealWorkflowPreconditionsLocators:
    DOOR_STATE_STATUS = (By.XPATH, "//ics-replace-seal-preconditions//ics-info-list-item[1]//ics-info-list-item-state//mat-icon")
    POWER_STATE_STATUS = (By.XPATH, "//ics-replace-seal-preconditions//ics-info-list-item[2]//ics-info-list-item-state//mat-icon")

class ReplaceSealWorkflowProcedureOneLocators:
    PROC_ONE_PARA_ONE = (By.XPATH, "//ics-replace-seal-procedure1//div[@id='ispp-id-replace-seal-procedure-container']//div[1]")
    PROC_ONE_PARA_TWO = (By.XPATH, "//ics-replace-seal-procedure1//div[@id='ispp-id-replace-seal-procedure-container']//div[2]")
    PROC_ONE_PARA_THREE = (By.XPATH, "//ics-replace-seal-procedure1//div[@id='ispp-id-replace-seal-procedure-container']//div[3]")
