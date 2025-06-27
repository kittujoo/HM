"""
File_Name: sample_temperature_condition_card.py
Desc: This file contains locator object of the web elements in sample temperature setting screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 04/06/2021
__author__ = "Sharmila Vairamani" Added TOGGLE_BUTTON_ACTION locator - 04/12/2021

"""
from selenium.webdriver.common.by import By


class SampleTemperatureSettingScreenLocators:
    SAMPLE_TEMPERATURE_OPTIONS = "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//"

    HEADER = (
        By.XPATH, "//ics-secondary-panel[@class='ng-star-inserted']//div[contains(text(),' Sample Temperature ')]")
    TEMPERATURE_EDIT_FIELD_HEADER = (By.XPATH,
                                     "//ics-info-list-item[@id='ispp-id-ftn-editField-setpointSettings']//div[contains(text(),'Temperature Setpoint (ºC)')]")
    TEMPERATURE_EDIT_FIELD_COMPONENT = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-ftn-editField-setpointSettings']//input")
    TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-ftn-toggle-temperatureSettings']//mat-slide-toggle")
    TOGGLE_BUTTON_ACTION = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-ftn-toggle-temperatureSettings']//div[@class='ics-toggle']")
    TEMPERATURE_EDIT_FIELD_STATUS = (
        By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-ftn-editField-setpoint']/div")

    TWENTY_ONE_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[18]")
    THIRTY_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[27]")
    THIRTY_SIX_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[33]")
    FORTY_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[37]")
    SCROLL_WINDOW_HEADER = (By.XPATH, "//ics-picker-content[@ng-reflect-id= 'ispp-id-sample-temperature-pic']")
    SET_TEMPERATURE_READ_BACK_MESSAGE = (By.XPATH,
                                         "//ics-info-list-item[@id = 'ispp-id-ftn-editField-setpointSettings']//div[@class= 'info-list-item-subtitle ng-star-inserted']")
    THIRTY_EIGHT_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[35]")
    THIRTY_THREE_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[30]")
    TWENTY_FIVE_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//ul//li[22]")
    
    # SAMPLE_TEMPERATURE_LIST is the whole number value for sample temperature
    # The space after the "wheel " class name is intentional, do not remove unless locator changes
    SAMPLE_TEMPERATURE_LIST = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-sample-temperature-pic']//div[contains(@class,'wheel ')][1]//ul")
    SETPOINT_TEMPERATURE_HEADER = (By.ID, "ispp-id-ftn-editField-setpointSettings")
