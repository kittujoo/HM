"""
File_Name: replace_needle_workflow_locators.py
Desc: This file contains locator object of the web elements in the calibrate workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = Sharmila Vairamani" Initial Check-in 09/19/2022

"""
from selenium.webdriver.common.by import By


class ReplaceNeedleWelcomeScreenLocators:
    # -- Page Banners -- #
    WELCOME_PARA_ONE = (By.XPATH, "//section[@id= 'replaceNeedleWorkflowWelcomeSection']//p[1]")
    WELCOME_PARA_TWO = (By.XPATH, "//section[@id= 'replaceNeedleWorkflowWelcomeSection']//p[2]")
    WELCOME_PARA_THREE = (By.XPATH, "//section[@id= 'replaceNeedleWorkflowWelcomeSection']//p[3]")
    CAUTION_TEXT = (By.XPATH, "//div[@class='warning-and-caution-item-container']")


class ReplaceNeedlePreconditionsScreenLocators:
    # -- Page Banners -- #
    COMPARTMENT_DOOR = (By.XPATH, "//ics-info-list[@class='preconditions-info-list']//ics-info-list-item[1]//mat-icon")
    SAMPLE_PLATES = (By.XPATH, "//ics-info-list[@class='preconditions-info-list']//ics-info-list-item[3]//mat-icon")
    POWER_STATE = (By.XPATH, "//ics-info-list[@class='preconditions-info-list']//ics-info-list-item[2]//mat-icon")
    WARNING_TEXT = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Warning']//section")
    STOP_BUTTON = (By.XPATH, "//div[@class='primary-action']//ics-tray[@ng-reflect-text= 'Stop']")


class StatusAndTestsScreenLocators:
    PROGRESS_BAR = (By.XPATH, "//ics-progressing-info-list-item//ics-progress-bar")
    REPLACE_NEEDLE_TEST_PARA_ONE = (By.XPATH, "//div[@id='ispp-id-replace-needle-procedure-container']//div[1]")
    REPLACE_NEEDLE_TEST_PARA_TWO = (By.XPATH, "//div[@id='ispp-id-replace-needle-procedure-container']//div[2]")
    REPLACE_NEEDLE_TEST_PARA_THREE = (By.XPATH, "//div[@id='ispp-id-replace-needle-procedure-container']//div[3]")
    PLAY_ICON = (By.XPATH, "//ics-info-list[@id = 'ispp-id-replace-needle-procedure2-info-list']//mat-icon")
    TEST_ONE = (By.XPATH, "//ics-information-card-item//li[1]")
    TEST_TWO = (By.XPATH, "//ics-information-card-item//li[2]")
    TEST_THREE = (By.XPATH, "//ics-information-card-item//li[3]")
    INFORMATION_TEXT = (By.XPATH,
                        "//ics-information-card-item[@ng-reflect-title='Information']//div[@class='information-card-description']")
