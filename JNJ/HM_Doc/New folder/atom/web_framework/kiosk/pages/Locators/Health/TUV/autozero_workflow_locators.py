"""
File_Name: autozero_workflow_locators.py
Desc: This file contains locator object of the web elements in the autozero workflow
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 8/1/23
"""
from selenium.webdriver.common.by import By


class AutozeroWorkflowLocators:
    PAGE_BANNER = (By.XPATH, "//ics-secondary-panel-header//div//div[contains(text(),'Autozero Offsets') and contains(@class,'title')]")
    AUTOZERO_BUTTON = (By.ID, "ispp-id-detector-autozero-button-autozero")
    RESET_BUTTON = (By.ID, "ispp-id-detector-autozero-button-reset")
    CHANNEL_A_OFFSET = (By.XPATH, "//ics-tuv-clear-autozero-offsets//ics-info-list-item[1]//div[contains(@class,'subtitle')][1]//div")
    CHANNEL_B_OFFSET = (By.XPATH, "//ics-tuv-clear-autozero-offsets//ics-info-list-item[2]//div[contains(@class,'subtitle')][1]//div")
    BACK_BUTTON = (By.XPATH, "//mat-dialog-container//ics-secondary-panel-base/div/div[1]/ics-dynamic-component/ics-secondary-panel-header/div/div[1]/div[2]")
