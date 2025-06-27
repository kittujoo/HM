"""
File_Name: instrument_configuration_screen.py
Desc: This file contains locator object of the web elements in instrument configuration screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 02/02/2021
__modified__ = "Tyler Prada" added reminders locator 8/20/2021
"""
from selenium.webdriver.common.by import By


class InstrumentConfigurationScreenLocators:
    DWELL_VOLUME = (By.XPATH, "//div[contains(text(),'Dwell Volume')]")
    PRESSURE_UNITS = (By.XPATH, "//ics-vertical-information-panel//li[2]")
    TUBING_KIT = (By.XPATH, "//div[contains(text(),'Tubing Kit')]")
    OPTIONS_PANEL = (By.XPATH, "//ics-info-list-item//div[contains(text(),'Options')]")
    REMINDERS_PANEL = (By.XPATH, "//ics-expansion-panel[@id = 'ispp-id-instrument-configuration-reminders-expansion']//ics-info-list-icon")
    HEADER = (By.ID, "ispp-id-instrument-configuration-expansion")
    TUV_ICON = (By.ID, "ispp-id-TUV-wavelength-icon")
    SAMPLE_MANAGER_ICON = (By.ID, "ispp-id-SM-injection-icon")
    SOLVENT_MANAGER_ICON = (By.XPATH, "//ics-tray[@id='ispp-id-QSM-flow-icon']")
    COLUMN_MANAGER_ICON = (By.ID, "ispp-id-CM-column-icon")
    BOTTLE_ICON = (By.XPATH, "//ics-tray[@id='ispp-id-solvent-bottle-icon']/div")

