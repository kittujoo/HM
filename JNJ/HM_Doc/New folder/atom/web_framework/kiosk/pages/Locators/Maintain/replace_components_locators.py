"""
File_Name: replace_components_locators.py
Desc: This file contains locator object of the webelements in the replace components screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = Sharmila Vairamani" Initial Check-in 09/19/2022
__modified__ = "Tyler Prada" Added pump maintenance locator 11/3/22
"""
from selenium.webdriver.common.by import By


class ReplaceComponentsScreenPageLocators:

    REPLACE_LAMP = (By.XPATH, "//ics-modal-info[@id = 'ispp-id-replace-components']//ics-info-list-item[1]")
    REPLACE_FLOWCELL = (By.XPATH, "//ics-modal-info[@id = 'ispp-id-replace-components']//ics-info-list-item[2]")
    REPLACE_COLUMN = (By.XPATH, "//ics-modal-info[@id = 'ispp-id-replace-components']//ics-info-list-item[3]")
    REPLACE_NEEDLE = (By.XPATH, "//ics-modal-info[@id = 'ispp-id-replace-components']//ics-info-list-item[4]")
    REPLACE_SEAL = (By.XPATH, "//ics-modal-info[@id = 'ispp-id-replace-components']//ics-info-list-item[5]")
    PUMP_MAINTENANCE = (By.XPATH, "//ics-modal-info[@id = 'ispp-id-replace-components']//ics-info-list-item[6]")
    HEADER = (By.XPATH,"//div[@class='secondary-panel-header-title' and text()='Replace Components']")