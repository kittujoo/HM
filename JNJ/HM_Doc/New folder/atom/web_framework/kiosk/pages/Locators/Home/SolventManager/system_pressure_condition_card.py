"""
File_Name: system_pressure_condition_card.py
Desc: This file contains locator objects of the web elements in the system pressure settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 3/29/2021

"""
from selenium.webdriver.common.by import By


class SystemPressureSettingsScreenLocators:
    PRESSURE_SETTINGS_OPTION_LIST = (By.XPATH, "//ics-pump-pressure-condition-settings//div[@class='info-list-content']")

    PSI_OPTION = (By.XPATH, "//li[contains(text(),'psi')]")
    BAR_OPTION = (By.XPATH, "//li[contains(text(),'bar')]")
    KPA_OPTION = (By.XPATH, "//li[contains(text(),'kPa')]")
    MPA_OPTION = (By.XPATH, "//li[contains(text(),'MPa')]")

    ACTIVE_PSI_OPTION = (By.XPATH, "//li[contains(text(),'psi') and contains(@class,'active')]")
    ACTIVE_BAR_OPTION = (By.XPATH, "//li[contains(text(),'bar') and contains(@class,'active')]")
    ACTIVE_KPA_OPTION = (By.XPATH, "//li[contains(text(),'kPa') and contains(@class,'active')]")
