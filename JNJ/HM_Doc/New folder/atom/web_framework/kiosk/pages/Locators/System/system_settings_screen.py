"""
File_Name: system_settings_screen.py
Desc: This file contains locator object of the web elements in system settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 02/02/2021
__modified__ ="Sharmila Vairamani" Change the locators due to change in the screen layout - 09/10/2021
__modified__ = "Tyler Prada" Locator change 1/4/23
__modified = "Tyler Prada" Changed config tab locator 6/22/23
"""
from selenium.webdriver.common.by import By


class SystemSettingsScreenLocators:

    HEADER = (By.XPATH, "//ics-expansion-panel[@id = 'ispp-id-system-settings-expansion-panel']//"
                        "div[@class = 'expansion-panel-title']")
    CONFIGURATION_TAB = (By.XPATH, "//div[contains(text(), 'Module Configuration')]")
    LOGS_TAB = (By.XPATH, "//div[contains(text(), 'Logs')]")
    PARTS_TAB = (By.XPATH, "//ics-info-list-icon[@ng-reflect-title ='Parts']//div[@class='info-list-item-header']")
    LEAK_SENSOR_TAB = (By.XPATH, "//div[contains(text(), 'Leak Sensors')]")
    KIOSK_SETTINGS_TAB = (By.XPATH, "//ics-info-list-icon[@ng-reflect-title ='Kiosk Settings']//div")
    ABOUT_TAB = (By.XPATH, "//div[contains(text(), 'About')]")
    ADMINISTRATION_TAB = (By.XPATH, "//div[contains(text(), 'Administration')]")
    PERFORMANCE_COUNTERS_TAB = (By.XPATH, "//div[contains(text(), 'Performance Counters')]")
