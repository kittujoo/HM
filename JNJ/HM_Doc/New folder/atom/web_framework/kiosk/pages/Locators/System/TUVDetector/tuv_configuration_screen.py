"""
File_Name: tuv_configuration_screen.py
Desc: This file contains locator object of the web elements in tuv configuration screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 03/18/2021
__modified__ = "Tyler Prada" Updated locators 8/9/21

"""
from selenium.webdriver.common.by import By


class TUVConfigurationScreenLocators:
    TUV_ICON = (By.ID, "ispp-id-TUV-wavelength-icon")
    TUV_HEADER = (By.XPATH, "//div[contains(text(),'TUV Detector')]")
    LAMP_PANEL = (By.XPATH, "//ics-info-list-item//div[contains(@class,'info-list-item-title') and contains(text(),'Lamp')]")
    PREFERENCES_TAB = (By.XPATH, "//div[contains(text(),'Preferences')]")
    TEMPERATURE_SETTINGS_READ_BACK = (
        By.XPATH, "//div[@class='info-list-items']//ics-info-list-icon[1]//ics-info-list-item[1]")
    OPTIONS_TAB = (By.XPATH, "//div[contains(text(),'Options')]")
    OPERATION_SETTINGS_READ_BACK = (
        By.XPATH, "//div[@class='info-list-items']//ics-info-list-icon[3]//ics-info-list-item[1]")
    CLOSE_SHUTTER_PREFERENCE_TAB = (By.XPATH, "//div[contains(text(),'Close Shutter Preference')]")
    SHUTTER_PREFERENCE_SETTINGS_READ_BACK = (
        By.XPATH, "//div[@class='info-list-items']//ics-info-list-icon[4]//ics-info-list-item[1]")
    OPTIONS_SETTINGS_READ_BACK = (
        By.XPATH, "//div[@class='info-list-items']//ics-info-list-icon[2]//ics-info-list-item[1]")


