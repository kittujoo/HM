"""
File_Name: solvent_manager_configuration_settings_screen.py
Desc: This file contains locator objects of the web elements in solvent manager configuration settings
      screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/3/2021
__modified__ "Tyler Prada" added mixer config locators 7/2/21
__modified__ = "Tyler Prada" added new locators based on mixer changes 1/25/22
__modified__ = "Tyler Prada" Updated locators due to UI changes 1/31/22
__modified__ = Tyler Prada" refactoring for pump module 1/4/23
"""
from selenium.webdriver.common.by import By


class PumpModuleConfigurationSettingsScreenLocators:
    SOLVENT_MANAGER_CONFIGURATION_SETTINGS_HEADER = (
        By.XPATH, "//ics-secondary-panel-header//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Pump')]")
    SOLVENT_MANAGER_CONFIGURATION_SETTINGS_NUMPAD = (By.XPATH, "//ics-settings-keypad//div[@class='settings-keypad-container']")
    INACTIVE_SOLVENT_MANAGER_CONFIGURATION_SETTINGS_NUMPAD = (By.XPATH, "//ics-settings-keypad//div[@class='settings-keypad-container inactive']")
    DONE_BUTTON_LABEL = (By.XPATH, "//ics-primary-action[@class='primary-action-done ng-star-inserted']//ics-tray")


class FluidicChamberLightTabLocators:
    FLUIDIC_CHAMBER_LABEL = (By.XPATH, "//div[contains(text(),' Light When Door is Opened ')]")
    FLUIDIC_CHAMBER_LIGHT_TOGGLE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-qsm-toggle-compartment-light']//ics-toggle")


class LeakDetectionTabLocators:
    LEAK_DETECTION_LABEL = (By.XPATH, "//div[contains(text(),' Leak Sensor ')]")
    LEAK_DETECTION_TOGGLE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-qsm-toggle-leak-sensor']//ics-toggle")
    LEAK_DETECTION_STATE = (By.XPATH, "//ics-info-list-item/descendant::div[contains(text(),'Leak Sensor') ]/following-sibling::div/child::div")


class MixerConfigurationTabLocators:
    NONE_OPTION = (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(),'None')]")
    CUSTOM_MIXER_OPTION = (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(),'Custom')]")
    MIXER_OPTION_100MM = (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(),'100 MM')]")
    MIXER_OPTION_50MM = (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(),'50 MM')]")
    MIXER_OPTION_30MM = (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(),'30 MM')]")
    MIXER_OPTION_NONE = (By.XPATH, "//div[@class='ng-star-inserted' and contains(text(),'None')]")
    MIXER_VOLUME_LABEL = (By.XPATH, "//div[contains(text(),'Mixer Volume (μL)')]")
    MIXER_VOLUME_VALUE = (By.XPATH, "//*[@id='ispp-id-qsm-mix-vol-title']/div/div[2]/div/div[2]/pre")
    CUSTOM_MIXER_FIELD = (By.XPATH, "//ics-edit-field//input")
    FIELD_CONTAINER = (By.XPATH, "//ics-edit-field")
