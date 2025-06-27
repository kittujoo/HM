"""
File_Name: maintain_screen_locators.py
Desc: This file contains locator object of the webelements in the maintain screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/2/2021
__modified__ = "Tyler Prada" updated locators 4/4/22
__modified__ = "Tyler Prada" Changed calibrate panel locator 7/26/23
"""
from selenium.webdriver.common.by import By


class MaintainScreenPageLocators:

    MAINTAIN_HEADER = (By.XPATH, "//div[@class='expansion-panel-title' and text()='Maintain']")
    REPLACE_PANEL = (By.XPATH, "//ics-vertical-scrolling-list//ics-info-list-item[1]/div")
    CALIBRATE_PANEL = (By.XPATH, "//ics-info-list-item[1]//div[contains(@class,'info-list-item-content')]")
    SERVICE_PANEL = (By.XPATH, "//ics-info-list-icon[3]//ics-info-list-item//div")
    CALIBRATE_DETECTOR = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Calibrate Detector']")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'back')]")