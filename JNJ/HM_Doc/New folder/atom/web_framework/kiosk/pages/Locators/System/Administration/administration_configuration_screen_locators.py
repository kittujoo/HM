"""
File_Name: administration_configuration_screen_locators.py
Desc: This file contains locator object of the web elements in administration screen
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
"""
from selenium.webdriver.common.by import By


class AdministrationConfigurationScreenLocators:
    ADMINISTRATION_CONFIGURATION_MENU = (By.XPATH, "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Administration')]")
    SYSTEM_QUALIFICATION_TAB = (By.ID, "ispp-id-administration-system-qualifications")
    ACQUISITION_CHECKS_TAB = (By.ID, "ispp-id-administration-acquisitionChecks")
    ACQUISITION_CHECKS_MENU = (By.XPATH, "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Acquisition Checks')]")
    RUN_TIME_CHECKS_TAB = (By.ID, "ispp-id-acquisition-checks-runTime")
    PRE_RUN_CHECKS_TAB = (By.ID, "ispp-id-acquisition-checks-preRun")
