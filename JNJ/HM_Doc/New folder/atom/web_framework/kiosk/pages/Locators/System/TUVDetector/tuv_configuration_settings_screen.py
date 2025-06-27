"""
File_Name: tuv_configuration_settings_screen.py
Desc: This file contains the locators used in the tuv_configuration_settings_screen_locators class object for the web elements.
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/23/2020
--modified__ = "Sharmila Vairamani" updates the locators with the latest changes - 10/21/2020
__modified__ = "Tyler Prada" updated locators 8/9/21
__modified__ = "Tyler Prada" Close shutter preference toggle conversion changes 11/17/21
"""
from selenium.webdriver.common.by import By


class TUVConfigurationSettingsScreenLocators:
    TUV_CONFIGURATION_SETTINGS_HEADER = (By.XPATH, "//div[contains(@class,'header') and contains(text(),'TUV Detector')]")
    LAMP_TAB = (By.XPATH, "//ics-dynamic-modal-panel[@id='ispp-id-TUV-watDynamic']//div[contains(text(),'Lamp')]")
    LAMP_SERIAL_NUMBER_LABEL = (By.XPATH, "//ics-tuv-lamp-settings//ics-info-list-item[1]//div[contains(@class,'subtitle')]")
    FLOW_CELL_TAB = (By.XPATH, "//ics-dynamic-modal-panel[@id='ispp-id-TUV-watDynamic']//div[contains(text(),'Flow Cell')]")
    FLOW_CELL_PART_NUMBER_LABEL = (By.XPATH, "//ics-tuv-flow-cell-settings//ics-info-list-item[1]//div[contains(@class,'subtitle')]")
    PREFERENCES_TAB = (By.XPATH,
                                            "//ics-dynamic-modal-panel[@id='ispp-id-TUV-watDynamic']//div[contains(text(),'Preferences')]")
    OPTIONS_TAB = (By.XPATH,
                                          "//ics-dynamic-modal-panel[@id='ispp-id-TUV-watDynamic']//div[contains(text(),'Options')]")
    NORMAL_TEMPERATURE_SETTINGS = (
    By.XPATH, "//ics-core-selector[@id='ispp-id-TUV-opticsTempStabilization-coreSelector']//li[1]")
    HIGHER_TEMPERATURE_SETTINGS = (
    By.XPATH, "//ics-core-selector[@id='ispp-id-TUV-opticsTempStabilization-coreSelector']//li[2]")
    MUCH_HIGHER_TEMPERATURE = (
    By.XPATH, "//ics-core-selector[@id='ispp-id-TUV-opticsTempStabilization-coreSelector']//li[3]")
    CLOSE_SHUTTER_TOGGLE = (By.XPATH, "//ics-tuv-preferences-settings-component//ics-toggle")
    LEAK_SENSOR_TOGGLE_BUTTON = (By.ID, "ispp-id-TUV-leakSensor-toggle")
    LEAK_SENSOR_STATE = (By.XPATH, "//ics-info-list-item/descendant::div[contains(text(),'Leak Sensor') ]/following-sibling::div/child::div")
    CLOSE_SHUTTER_PREFERENCE_TAB = (By.XPATH,
                                    "//ics-dynamic-modal-panel[@id='ispp-id-TUV-watDynamic']//div[contains(text(),'Close Shutter Preference')]")
    LAMP_WITH_RESIDENT_ID_TOGGLE_BUTTON = (By.ID, "ispp-id-TUV-requiredResidentLampId-toggle")
    FLOW_CELL_WITH_RESIDENT_ID_TOGGLE_BUTTON = (By.ID, "ispp-id-TUV-requiredResidentFlowId-toggle")
    OPTIONS_CONTAINER = (By.XPATH, "//div[@class='tuv-options-settings-container']")
