"""
File_Name: sm_configuration_screen.py
Desc: This file contains locator object of the web elements in sample manager configuration screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/26/2021
__modified__ = "Tyler Prada" Rework for ui changes 1/30/23
__modified__ = "Tyler Prada" Locator adjustments 9/27/23
"""
from selenium.webdriver.common.by import By


class SMConfigurationScreenLocators:
    SAMPLE_MANAGER_ICON = (By.ID, "ispp-id-SM-injection-icon")
    HEADER = (By.XPATH, "//div[contains(@class,'expansion-panel-header')]//div[contains(text(),'Sample Manager')]")
    VOLUMES_TAB = (By.XPATH, "//ics-info-list-item[1]")
    COMPARTMENT_LIGHT_TAB = (By.XPATH, "//ics-info-list-item[2]")
    OPTIONS_TAB = (By.XPATH, "//ics-info-list-item[3]")
    PREFERENCES_TAB = (By.XPATH, "//div[contains(text(),'Preferences')]")
