"""
File_Name: health_screen_locators.py
Desc: This file contains locator object of the web elements in the health screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/24/2021
__modified__ = "Tyler Prada" added now page locators/workflow locators 1/14/21
__modified__ = "Tyler Prada" Adjusted heater/cooler locator 2/15/22
__modified__ = "Tyler Prada" Adjustments for leak test moving to health screen 2/21/22
__modified__ = "Sharmila Vairamani" Added locators for  calibrate wavelength 2/23/2022
__modified__ = "Tyler Prada" Added calibrate axes workflow button 3/9/2022
__modified__ = "Tyler Prada" added noise drift panel locator 4/20/22
__modified__ = "Tyler Prada" Added column manager icon 7/22/22
__modified__ = "Tyler Prada" locator adjustment 10/7/22
__modified = "Tyler Prada" locator adjustment 6/22/23
__modified = "Tyler Prada" Added autozero panel 8/1/23
"""
from selenium.webdriver.common.by import By


class HealthScreenLocators:
    TROUBLESHOOT_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Troubleshoot']//"
                                    "div[contains(@class,'info-list-item-content')]")

    ISSUE_RESOLUTION_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Issue Resolution']")

    TUV_SECTION_ICON = (By.ID, "ispp-id-TUV-wavelength-icon")
    TUV_SECTION_ICON_NEW = (By.XPATH, "//mat-icon[@ng-reflect-svg-icon='ics-img-wavelength']")

    NOISE_DRIFT_START_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Noise and Drift Test']//"
                                         "div[contains(@class,'info-list-item-content')]")
    AUTOZERO_START_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Autozero Offsets']//div[contains(@class,'info-list-item-content')]")

    ROTARY_TRAY_BUTTON = (By.XPATH, "//div[@class='rotary-tray-card-container']//ics-action-button")

    HEALTH_PAGE_TWO = (By.XPATH, "//li//a[@id='isppK-id-pagination-page2']")

    LEAK_TEST_PANEL = (By.ID, "ispp-id-leakTestWorkflow-actionButton")

    HEATER_COOLER_WORKFLOW_START = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Column Compartment Temperature']")
                                              
    CALIBRATE_WAVELENGTH_BUTTON = (By.ID, "verifyAndCalibrateWavelengthsActionButton")
    CALIBRATE_AXES_BUTTON = (By.ID, "ispp-id-calibrateAxes-actionButton")

    SAMPLE_MANAGER_ICON = (By.ID, "ispp-id-SM-injection-icon")
    SAMPLE_METERING_PUMP_PANEL = (By.XPATH,
                                  "//ics-info-list-item[@ng-reflect-title='Sample Metering Pump Leak Test']")
    NEEDLE_SEAL_READINESS_PANEL = (By.XPATH,
                                   "//ics-info-list-item[@ng-reflect-title='Needle Seal Readiness Test']//"
                                   "div[contains(@class,'info-list-item-content')]")

    SAMPLE_TEMPERATURE_TEST_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Sample Compartment Temperature']")

    COLUMN_MANAGER_ICON = (By.ID, "ispp-id-CM-column-icon")
    SCAN_WAVELENGTH_ICON = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Scan Wavelengths']")

    HEALTH_TITLE = (By.XPATH, "//div[@class='expansion-panel-title' and contains(text(),'Health')]")
