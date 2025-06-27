"""
File_Name: wavelength_condition_card.py
Desc: This file contains locator object of the web elements in the setting screen of the wavelength conditional card
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 03/25/2021

"""
from selenium.webdriver.common.by import By


class WavelengthSettingScreenLocators:
    SELECTOR_COMPONENT = (By.ID, "ispp-id-tuv-coreSelector-mode")
    HEADER = (By.XPATH, "//div[@class = 'secondary-panel-header-container']//div[contains(text(),'Wavelength')]")
    WAVE_LENGTH_MODE_READ_BACK = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelengthMode']//span["
                                            "@class='readback-units ng-star-inserted']")
    WAVE_LENGTH_1_READ_BACK_VALUE = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelength1']//span[1]")
    WAVE_LENGTH_1_READ_BACK_UNITS = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelength1']//span[2]")
    WAVE_LENGTH_2_READ_BACK_VALUE = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelength2']//span[1]")
    WAVE_LENGTH_2_READ_BACK_UNITS = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelength2']//span[2]")
    WAVE_LENGTH_MODE_SINGLE_SELECTOR_COMPONENT = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[1]")
    WAVE_LENGTH_MODE_DUAL_SELECTOR_COMPONENT = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[2]")
    DUAL_WAVE_LENGTH_ENTRY_FIELD_HEADER = (By.CSS_SELECTOR, "#ispp-id-TUV-editField-groupWavelengthInput2")
    SINGLE_WAVE_LENGTH_ENTRY_FIELD_HEADER = (By.CSS_SELECTOR, "#ispp-id-TUV-editField-groupWavelengthInput1")
    DUAL_WAVE_LENGTH_ENTRY_FIELD_LABEL = (By.XPATH, "//mat-label[contains(text(),'Wavelength 2')]")
    SINGLE_WAVE_LENGTH_ENTRY_FIELD_LABEL = (By.XPATH, "//mat-label[contains(text(),'Wavelength 1')]")

    SINGLE_WAVE_LENGTH_ENTRY_FIELD = (
        By.XPATH, "//ics-edit-field[@id='ispp-id-TUV-editField-groupWavelengthInput1']//input")
    DUAL_WAVE_LENGTH_ENTRY_FIELD = (
        By.XPATH,
        "//ics-edit-field[@id='ispp-id-TUV-editField-groupWavelengthInput2']//input")