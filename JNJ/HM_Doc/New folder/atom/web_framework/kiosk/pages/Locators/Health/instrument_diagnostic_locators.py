"""
File_Name: instrument_diagnostic_locators.py
Desc: This file contains locator object of the web elements in the instrument diagnostic screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/10/22
__modified__ = "Sharmila Vairamani" Added schematic icon locators
"""
from selenium.webdriver.common.by import By


class InstrumentDiagnosticLocators:
    ISSUE_RESOLUTION_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Issue Resolution']")
    FIRST_ACTIVE_ERROR_ISSUE = (By.XPATH, "(//ics-info-list-item[@ng-reflect-indicator='error'])[position()=1]")
    ISSUE_ITEMS = (By.XPATH, "//ics-info-list-item[@ng-reflect-inline='true']")
    NEEDLE_SEAL_READINESS_PANEL = (By.XPATH,
                                   "//ics-info-list-item[@ng-reflect-title='Needle Seal Readiness Test']//div[contains(@class,'info-list-item-content')]")
    SOLVENT_MANAGER_ICON = (By.ID, "ispp-id-QSM-flow-icon")
    COLUMN_MANAGER_ICON = (By.ID, "ispp-id-CM-column-icon")
    HEADER = (By.XPATH, "//div[@class ='expansion-panel-title']")
