"""
File_Name: ambient_temperature_condition_card.py
Desc: This file contains locator object of the web elements in ambient temperature setting screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 04/19/2021
__modified__ = "Tyler Prada" ambient temperature conversion - 10/1/21
"""
from selenium.webdriver.common.by import By


class AmbientTemperatureSettingScreenLocators:
    HEADER = (
        By.XPATH, "//div[contains(text(),' Configure ambient temperature settings ')]")
    TEMPERATURE_EDIT_FIELD = (By.XPATH, "//ics-info-list-item[@id='ispp-id-ftn-entryField-roomTemperature']//input")
    TOLERANCE_RANGE_LIST = (
        By.XPATH, "//ics-picker-base//div[contains(@class,wheel)][3] /ul[@class = 'wheel-scroll']")
    TOLERANCE_TEMPERATURE_LIST = (By.XPATH, "//ics-picker-base//div[contains(@class,wheel)][1] /ul[@class = 'wheel-scroll']")
    TOGGLE_BUTTON_STATE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-ftn-toggle-notifications']//mat-slide-toggle")
    TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-ftn-ambient-warning']//mat-slide-toggle")
    TEMPERATURE_EDIT_FIELD_STATE = (
        By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-ftn-entryField-roomTem']/div")
    TEMPERATURE_TOLERANCE_EDIT_FIELD_STATE = (
        By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-ftn-entryField-tempera']/div")
    AMBIENT_TEMPERATURE_LIST = (
        By.XPATH, "//ics-picker-base//div[contains(@class,'wheel')][1]/ul[@class = 'wheel-scroll']")
    TEMPERATURE = (By.XPATH,
                   "//ics-info-list-item[@id ='ispp-id-ftn-ambient-temperature-tolerance']//div[contains(@class,'info-list-item-subtitle')]")
    TEMPERATURE_DEFAULT_BUTTON = (By.XPATH, "//div[@class='content-container']//ics-picker-button")
    SCROLL_WINDOW_HEADER = (By.ID,"ispp-id-ambient-temperature-picker")
    INFORMATION_TEXT = (By.XPATH, "//div[@class ='information-card-description']")
    AMBIENT_TEMPERATURE_INFO = ( By.XPATH, "//ics-info-list-item[@id ='ispp-id-ftn-ambient-temperature-tolerance']//div[contains(@class,'sub')][1]")
