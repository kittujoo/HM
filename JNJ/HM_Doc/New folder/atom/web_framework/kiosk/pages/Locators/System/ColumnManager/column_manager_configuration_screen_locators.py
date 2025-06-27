"""
File_Name: column_manager_configuration_screen_locators.py
Desc: This file contains locator objects of the web elements in column manager configuration screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 12/15/2021

"""
from selenium.webdriver.common.by import By


class ColumnManagerConfigurationScreenLocators:
    COLUMN_MANAGER_CONFIGURATION_MENU = (By.XPATH, "//div[contains(@class,'expansion-panel-header')]//div[contains(text(),'Column')]")
    OPTIONS_PANEL = (By.XPATH, "//div[@class='info-list-item-content divider-item']")
