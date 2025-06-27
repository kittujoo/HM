"""
File_Name: system_logs_screen_locators.py
Desc: This file contains locator object of the web elements in system log screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."

"""
from selenium.webdriver.common.by import By


class LeakSensorScreenLocators:
    LEAK_SENSOR_CONFIGURATION_MENU = (By.XPATH, "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Leak Sensors')]")
    QSM_LEAK_SENSOR = (By.XPATH, "//div[text()='QSM Leak Sensor']/parent::div/following-sibling::div/child::ics-toggle")
    QSM_LEAK_STATUS = (By.XPATH, "//ics-vertical-scrolling-list-item/descendant::div[contains(text(),'QSM Leak Sensor') ]/following-sibling::div")
    CHC_LEAK_SENSOR = (By.XPATH, "//div[text()='CHC Leak Sensor']/parent::div/following-sibling::div/child::ics-toggle")
    CHC_LEAK_STATUS = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item//div[contains(text(),'CHC Leak Sensor') ]/following-sibling::div")
    TUV_LEAK_SENSOR = (By.XPATH, "//div[text()='TUV Leak Sensor']/parent::div/following-sibling::div/child::ics-toggle")
    TUV_LEAK_STATUS = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item//div[contains(text(),'TUV Leak Sensor') ]/following-sibling::div")
    SM_LEAK_SENSOR = (By.XPATH, "//div[text()='SM Leak Sensor']/parent::div/following-sibling::div/child::ics-toggle")
    SM_LEAK_STATUS = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[4]//div[contains(text(),'SM Leak Sensor') ]/following-sibling::div")
    CHC_LEAK_SENSOR_TOGGLE = (By.XPATH, "//div[text()='CHC Leak Sensor']/parent::div/following-sibling::div/child::ics-toggle")
    CHC_LEAK_SENSOR_STATUS = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item//div[contains(text(),'CHC Leak Sensor') ]/following-sibling::div")
