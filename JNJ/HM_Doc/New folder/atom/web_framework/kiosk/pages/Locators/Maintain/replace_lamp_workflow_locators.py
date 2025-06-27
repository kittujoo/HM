"""
File_Name: replace_lamp_workflow_locators.py
Desc: This file contains locator object of the webelements in the replace lamp workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/24/22
"""
from selenium.webdriver.common.by import By


class ReplaceLampWorkflowLocators:

    WELCOME_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-welcome")
    CAUTIONS_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-cautions")
    PRECONDITIONS_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-preconditions")
    REMOVAL_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-remove-lamp")
    FIRST_INSTALL_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-install")
    SECOND_INSTALL_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-install-2")
    FINISH_BANNER = (By.ID, "ispp-id-replace-lamp-workflow-finish")

class ReplaceLampWorkflowWelcomeLocators:
    WELCOME_PARA_ONE = (By.XPATH, "//section[@id='instrumentBasicShutdownWorkflowWelcomeSection']//p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//section[@id='instrumentBasicShutdownWorkflowWelcomeSection']//p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//section[@id='instrumentBasicShutdownWorkflowWelcomeSection']//p[3]")

class ReplaceLampWorkflowCautionLocators:
    BURN_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-list//ics-warning-and-caution-item[1]//div[@class='warning-and-caution-item-description']")
    GENERAL_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-list//ics-warning-and-caution-item[2]//div[@class='warning-and-caution-item-description']//div")
    GENERAL_CAUTION_BULLET_ONE = (By.XPATH, "//ics-warning-and-caution-list//ics-warning-and-caution-item[2]//div[@class='warning-and-caution-item-description']//li[1]")
    GENERAL_CAUTION_BULLET_TWO = (By.XPATH, "//ics-warning-and-caution-list//ics-warning-and-caution-item[2]//div[@class='warning-and-caution-item-description']//li[2]")

class ReplaceLampWorkflowPreconditionsLocators:
    LAMP_STATE_STATUS = (By.XPATH, "//ics-replace-lamp-preconditions//ics-info-list-item[1]//ics-info-list-item-state//mat-icon")
    FLOW_STATE_STATUS = (By.XPATH, "//ics-replace-lamp-preconditions//ics-info-list-item[2]//ics-info-list-item-state//mat-icon")
    POWER_STATE_STATUS = (By.XPATH, "//ics-replace-lamp-preconditions//ics-info-list-item[3]//ics-info-list-item-state//mat-icon")
    WARNING_PARA_ONE = (By.XPATH, "//ics-information-card//p[1]")
    WARNING_PARA_TWO = (By.XPATH, "//ics-information-card//p[2]")
    WARNING_PARA_THREE = (By.XPATH, "//ics-information-card//p[3]")

class ReplaceLampWorkflowRemovalLocators:
    REMOVAL_STEP_ONE = (By.XPATH, "//ics-replace-lamp-remove-lamp//ics-info-list//li[1]")
    REMOVAL_STEP_TWO = (By.XPATH, "//ics-replace-lamp-remove-lamp//ics-info-list//li[2]")
    REMOVAL_STEP_THREE = (By.XPATH, "//ics-replace-lamp-remove-lamp//ics-info-list//li[3]")
    REMOVAL_STEP_FOUR = (By.XPATH, "//ics-replace-lamp-remove-lamp//ics-info-list//li[4]")
    WARNING_TEXT = (By.XPATH, "//ics-information-card-item//section")
    CAUTION_PARA_ONE = (By.XPATH, "//ics-information-card-item//span[1]")
    CAUTION_PARA_TWO = (By.XPATH, "//ics-information-card-item//span[2]")
    CAUTION_PARA_THREE = (By.XPATH, "//ics-information-card-item//span[3]")

class ReplaceLampWorkflowFirstInstallationLocators:
    INSTALLATION_STEP_ONE = (By.XPATH, "//ics-replace-lamp-install//li[1]")
    INSTALLATION_STEP_TWO = (By.XPATH, "//ics-replace-lamp-install//li[2]")
    INSTALLATION_STEP_THREE = (By.XPATH, "//ics-replace-lamp-install//li[3]")
    INSTALLATION_STEP_FOUR = (By.XPATH, "//ics-replace-lamp-install//li[4]")
    CAUTION_TEXT = (By.XPATH, "//ics-replace-lamp-install//section")

class ReplaceLampWorkflowSecondInstallationLocators:
    INSTALLATION_STEP_FIVE = (By.XPATH, "//ics-replace-lamp-install-2//li[1]")
    INSTALLATION_STEP_SIX = (By.XPATH, "//ics-replace-lamp-install-2//li[2]")
    INSTALLATION_STEP_SEVEN = (By.XPATH, "//ics-replace-lamp-install-2//li[3]")
    CAUTION_TEXT = (By.XPATH, "//ics-replace-lamp-install-2//section")

class ReplaceLampWorkflowFinishLocators:
    LAMP_HOURS = (By.XPATH, "//ics-replace-lamp-finish//ics-info-list-item[3]//div[contains(@class,'subtitle')][1]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")
