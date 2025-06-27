"""
File_Name: pump_module_configuration_screen.py
Desc: This file contains locator objects of the web elements in solvent manager configuration screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/3/2021
__modified__ = "Tyler Prada" added mixer config locator 7/2/21
__modified__ = "Tyler Prada" added options panel locator 1/25/22
__modified__ = "Tyler Prada" Updated locators due to UI changes 1/31/22
__modified__ = Tyler Prada" refactoring for pump module 1/4/23
"""
from selenium.webdriver.common.by import By


class PumpModuleConfigurationScreenlocators:
    SOLVENT_MANAGER_CONFIGURATION_MENU = (By.XPATH, "//div[contains(@class,'expansion-panel-title') and contains(text(),'Pump')]")
    OPTIONS_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title = 'Options']//div[@class='info-list-item-header']")
