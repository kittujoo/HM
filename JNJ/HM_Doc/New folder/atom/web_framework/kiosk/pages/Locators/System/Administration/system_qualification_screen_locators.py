"""
File_Name: administration_configuration_screen_locators.py
Desc: This file contains locator object of the web elements in administration screen
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
"""
from selenium.webdriver.common.by import By


class SystemQualificationScreenLocators:
    SYSTEM_QUALIFICATION_MENU = (By.XPATH, "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'System Qualification')]")
    SYSTEM_QUALIFICATION_TOGGLE = (By.XPATH, "//ics-toggle[@id='ispp-id-system-qualification-toggle']")
    QUALIFICATION_EXPIRES_LABEL = (By.XPATH, "//ics-info-list-icon//ics-info-list-item//div[contains(@class,'info-list-item-subtitle ')]")
    MONTHS_PICKER_WHEEL = (By.XPATH, "//ics-picker-base//div[@class='wheel-wrapper']//div[1]//ul")
    DEFAULT_MONTH_BUTTON = (By.XPATH, "//ics-picker-button")
