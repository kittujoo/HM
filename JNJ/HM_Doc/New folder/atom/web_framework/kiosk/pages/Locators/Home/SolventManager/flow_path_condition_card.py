"""
File_Name: flow_path_condition_card.py
Desc: This file contains locator objects of the web elements in the flow path settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/16/2021
__modified__ = "Tyler Prada" changed locators to one mixer 3/1/22
"""
from selenium.webdriver.common.by import By


class FlowPathSettingsScreenLocators:
    FLOW_PATH_OPTION_LIST = (By.XPATH, "//ics-qsm-flow-path-condition-settings//div[@class='info-list-item-body']")
    AVAILABLE_FLOW_PATH_OPTIONS = (By.XPATH, "//ics-core-selector[@id='ispp-id-FTN-coreSelector-positionSettings']//li")

    BLOCKED_OPTION = (By.XPATH, "//li[contains(text(),'Blocked')]")
    VENT_OPTION = (By.XPATH, "//li[contains(text(),'Vent')]")
    MIXER_OPTION = (By.XPATH, "//li[contains(text(),'Mixer')]")

    ACTIVE_BLOCKED_OPTION = (By.XPATH, "//li[contains(text(),'Blocked') and contains(@class,'active')]")
    ACTIVE_VENT_OPTION = (By.XPATH, "//li[contains(text(),'Vent') and contains(@class,'active')]")
    ACTIVE_FIRST_MIXER_OPTION = (By.XPATH, "//li[contains(text(),'Mixer 1') and contains(@class,'active')]")
    ACTIVE_SECOND_MIXER_OPTION = (By.XPATH, "//li[contains(text(),'Mixer 2') and contains(@class,'active')]")

