"""
File_Name: instrument_configuration_settings_screen.py
Desc: This file contains locator object of the web elements in instrument configuration screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/20/2021
__modified = "Tyler Prada" Added settings screen locators 6/22/23
__modified__ = "Tyler Prada" New locators for tab navigation 10/19/23
"""
from selenium.webdriver.common.by import By


class InstrumentConfigurationSettingsScreenLocators:
    INSTRUMENT_CONFIG_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-title' and contains(text(),'System')]")

    DWELL_VOLUME_TAB = (By.XPATH, "//ics-vertical-information-panel//ul//li[1]")
    UNITS_TAB = (By.XPATH, "//ics-vertical-information-panel//ul//li[2]")
    TUBING_KIT_TAB = (By.XPATH, "//ics-vertical-information-panel//ul//li[3]")

    DWELL_VOLUME_FIELD = (By.XPATH, "//input")
    ACTIVE_PRESSURE_UNIT = (By.XPATH, "//ics-info-list-item[1]//ics-core-selector//li[contains(@class,'active')]")
    PSI_PRESSURE_UNIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'psi')]")
    BAR_PRESSURE_UNIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'bar')]")
    KPA_PRESSURE_UNIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'kPa')]")
    MPA_PRESSURE_UNIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'MPa')]")
    STANDARD_TUBING_KIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'Standard')]")
    HIGH_FLOW_TUBING_KIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'High Flow')]")
    HIGH_PH_TUBING_KIT = (By.XPATH, "//div[@class='ics-core-selector']//li[contains(text(),'High pH')]")
    CANCEL_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'cancel')]")
    INFORMATION_BANNER = (By.ID, "ispp-id-instrument-dwellVolume-infoListItemInfoState")


class RemindersSettingsScreenLocators:
    REMINDERS_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-title' and contains(text(),'Reminders')]")
    DAY_SELECTION_OPTION = (By.XPATH, "//div[@class='ics-core-selector']//li[2]")
    WEEKDAYS_BUTTON = (By.XPATH, "//div[contains(@class,'grid-picker-wrapper-button')]")
    MONDAY_OPTION = (By.XPATH, "//div[@class='grid-picker-item-text' and contains(text(),'Monday')]")
    TUESDAY_OPTION = (By.XPATH, "//div[@class='grid-picker-item-text' and contains(text(),'Tuesday')]")
    WEDNESDAY_OPTION = (By.XPATH, "//div[@class='grid-picker-item-text' and contains(text(),'Wednesday')]")
    THURSDAY_OPTION = (By.XPATH, "//div[@class='grid-picker-item-text' and contains(text(),'Thursday')]")
    FRIDAY_OPTION = (By.XPATH, "//div[@class='grid-picker-item-text' and contains(text(),'Friday')]")
    TIME_PANEL = (By.XPATH, "//ics-info-list-item//div[contains(text(),'Time')]")
    HOUR_TWO = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][1]//li[2]")
    MINUTE_TWO = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[3]")
    MINUTE_THREE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[4]")
    MINUTE_FOUR = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[5]")
    MINUTE_FIVE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[6]")
    SELECTED_MASK_COMPONENT = (By.XPATH, "//div[@class ='mask-selected-item']")
    PM_PERIOD = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][4]//li[2]")
    AM_PERIOD = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][4]//li[1]")
    HOUR_THREE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][1]//li[3]")
    HOUR_FOUR = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][1]//li[4]")
    HOUR_FIVE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][1]//li[5]")
    MINUTE_TWENTY_NINE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[30]")
    MINUTE_TWENTY_TWO = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[23]")
    MINUTE_TWENTY_THREE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[24]")
