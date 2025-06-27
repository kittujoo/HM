"""
File_Name: solvent_bottle_configuration_screen_locators.py
Desc: This file contains locator objects of the web elements in solvent bottle configuration screen locators
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/19/2022

"""
from selenium.webdriver.common.by import By


class SolventBottleConfigurationScreenLocators:
    WASH_SOLVENTS_PANEL = (By.XPATH, "//div[contains(text(),'Wash Solvents Configuration')]")
    MOBILE_PHASE_PANEL = (By.XPATH, "//div[contains(text(),' Mobile Phase Configuration ')]")
    
