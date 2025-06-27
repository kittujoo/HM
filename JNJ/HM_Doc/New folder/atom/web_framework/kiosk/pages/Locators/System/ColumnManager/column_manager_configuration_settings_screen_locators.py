"""
File_Name: column_manager_configuration_settings_screen.py
Desc: This file contains locator objects of the web elements in column manager configuration settings
      screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 12/15/2021
__modified__ = "Tyler Prada" Removal of max temp 2/2/22
"""
from selenium.webdriver.common.by import By


class ColumnManagerConfigurationSettingsScreenLocators:
    COLUMN_MANAGER_SETTINGS_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-title' and contains(text(),'Column')]")
    LEAK_SENSOR_ALARM_TOGGLE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-toggle-leak-sensor']//ics-toggle")
    DOOR_OPEN_ALARM_TOGGLE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-toggle-door-open']//ics-toggle")
    LEAK_DETECTION_STATE = (By.XPATH, "//ics-info-list-item/descendant::div[contains(text(),'Leak Sensor') ]/following-sibling::div/child::div")
