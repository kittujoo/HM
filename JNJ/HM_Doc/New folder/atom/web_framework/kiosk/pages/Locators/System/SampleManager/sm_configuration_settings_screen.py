"""
File_Name: sm_configuration_settings_screen.py
Desc: This file contains locator object of the web elements in sample manager configuration settings
      screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/21/2021
__modified__ = "Tyler Prada" Rework for ui changes 1/30/23
__modified__ = "Tyler Prada" Addition & adjustment of locators 9/27/23
"""
from selenium.webdriver.common.by import By


class SMConfigurationSettingsScreenLocators:
    SM_CONFIGURATION_HEADER = (By.XPATH, "//ics-secondary-panel-header//div[@class='secondary-panel-header-title' and contains(text(),'Sample Manager')]")


class VolumeSettingsTab:
    VOLUMES_TAB = (By.XPATH, "//ics-dynamic-modal-panel[@id='ispp-id-CM-watDynamic']//div[@class='vertical-panel-container']//li[1]")
    VOLUMES_HEADER = (By.XPATH, "//div[contains(text(),'Extension Loop')]")
    EXTENSION_LOOP_TOGGLE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-volume-config-extension-loop-toggle']//ics-toggle")
    EXTENSION_LOOP_VOLUME = (By.XPATH, "//div[text() = 'Extension Loop (µL)']")

    FIFTY_MICRO_LITRE_OPTION = (By.XPATH, "//ics-core-selector//li[1]")
    HUNDRED_MICRO_LITRE_OPTION = (By.XPATH, "//ics-core-selector//li[2]")
    # Multi-draw enabled only
    TWO_FIFTY_MICRO_LITRE_OPTION = (By.XPATH, "//ics-core-selector//li[3]")
    ONE_THOUSAND_MICRO_LITRE_OPTION = (By.XPATH, "//ics-core-selector//li[4]")
    TWO_THOUSAND_MICRO_LITRE_OPTION = (By.XPATH, "//ics-core-selector//li[5]")

    HUNDRED_MICRO_LITRE_SYRINGE_OPTION = (By.XPATH,"//ics-info-list-item[@id='ispp-id-volume-config-syringe-size']//div[@class='info-list-item-body']//li[1]")
    TWO_FIFTY_MICRO_LITRE_SYRINGE_OPTION = (By.XPATH,"//ics-info-list-item[@id='ispp-id-volume-config-syringe-size']//div[@class='info-list-item-body']//li[2]")
    FIVE_HUNDRED_MICRO_LITRE_SYRINGE_OPTION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-volume-config-syringe-size']//div[@class='info-list-item-body']//li[3]")

    MULTI_DRAW_READ_BACK_MESSAGE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-volume-config-information']//div[contains(@class,'subtitle')][1]//div")
    SINGLE_DRAW_READ_BACK_MESSAGE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-volume-config-no-multi-draw']//div[@class='info-list-item-subtitle ng-star-inserted']")


class CompartmentLightTab:
    LIGHT_TURN_ON_FOR_PLATE_OPTION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-compartmentLight-plateScanned']//div[@class='ics-core-selector']//li[1]")
    LIGHT_TURN_OFF_FOR_PLATE_OPTION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-compartmentLight-plateScanned']//div[@class='ics-core-selector']//li[2]")

    LIGHT_TURN_ON_FOR_DOOR_OPTION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-compartmentLight-doorOpened']//div[@class='ics-core-selector']//li[1]")
    LIGHT_TURN_OFF_FOR_DOOR_OPTION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-compartmentLight-doorOpened']//div[@class='ics-core-selector']//li[2]")

    LIGHT_PREFERENCE_TAB = (By.XPATH, "//ics-dynamic-modal-panel[@id='ispp-id-CM-watDynamic']//div[@class='vertical-panel-container']//li[2]")
    LIGHT_PREFERENCE_HEADER = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-compartmentLight-plateScanned']")

    LIGHT_PREFERENCE_TOGGLE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-compartmentLight-doorOpened']//ics-toggle")


class OptionsTab:
    INJECTION_FAILS_OPTIONS = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-core-selector']//div[@class='ics-core-selector']//li[1]")
    INJECTION_CONTINUES_OPTIONS = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-core-selector']//div[@class='ics-core-selector']//li[2]")
    OPTIONS_TAB = (By.XPATH, "//ics-dynamic-modal-panel[@id='ispp-id-CM-watDynamic']//div[@class='vertical-panel-container']//li[3]")
    OPTIONS_HEADER = (By.ID, "ispp-id-sm-options-leak-sensor")
    LEAK_SENSOR_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-leak-sensor']//ics-toggle")
    LEAK_SENSOR_TOGGLE_BUTTON_STATUS = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-leak-sensor']/div/div[2]//div[2]")
    MULTI_DRAW_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-multi-draw-rotary']//ics-toggle")
    INJECTION_OPTIONS_READ_BACK_MESSAGE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-core-selector']//div[@class='info-list-item-subtitle ng-star-inserted']")


class PreferencesTab:
    NOTIFICATION_TAB = (By.XPATH, "//ics-dynamic-modal-panel[@id='ispp-id-CM-watDynamic']//div[@class='vertical-panel-container']//li[3]")
    NOTIFICATION_HEADER = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-preferences-vial-missing-toggle']")
    #LEAK_DETECTION_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-toggleLeakDetection']//ics-toggle")
    LEAK_DETECTION_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-preferences-vial-missing-toggle']//ics-toggle")
    DOOR_OPEN_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-sm-options-door-alarm']//ics-toggle")
    #DOOR_OPEN_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-preferences-wash-needle-toggle']//ics-toggle")
    #AUDIBLE_ALARM_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-toggleDoorOpenAlarm']//ics-toggle")
    AUTO_ROTATE_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-preferences-auto-rotate-toggle']//ics-toggle")
    AUDIBLE_ALARM_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-preferences-wash-needle-toggle']//ics-toggle")
    PLATE_DETECTION_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-SM-preferences-plate-detection-toggle']//ics-toggle")
