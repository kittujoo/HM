"""
File_Name: volume_pumped_condition_card_locators.py
Desc: This file contains locator objects of the web elements in the volume pumped settings screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/07/2022

"""
from selenium.webdriver.common.by import By


class VolumePumpSettingsScreenLocators:
    FLOW_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id ='ispp-id-QSM-toggle-volumePumpedWarning']//mat-slide-toggle")
    FLOW_RATE_EDIT_FIELD = (By.XPATH,"//ics-info-list-item[@id ='ispp-id-QSM-entryField-volumePumpedThreshold']//input")
    FLOW_RATE_EDIT_FIELD_STATE = (By.XPATH, "//ics-info-list-item[@id ='ispp-id-QSM-entryField-volumePumpedThreshold']//ics-edit-field//div")
    FLOW_HINT_LOCATOR = (By.ID, "ispp-id-hint-editField")
