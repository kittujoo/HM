"""
File_Name: lock_screen_locators.py
Desc: This file contains locator object of the web elements in the lock screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__modified__ = "Tyler Prada" added name label locator 9/28/22
"""

from selenium.webdriver.common.by import By


class LockScreenPageLocators:
    swipe_up_component = (By.XPATH, "//div[@id='isppK-id-icon-unlock']")
    swipe_to_unlock_component = (By.ID, "isppK-id-icon-unlock")
    click_kiosk_app = (By.XPATH, "//*[@id='kioskBtn']/span")
    base_url = (By.XPATH, "/html/body")
    SYSTEM_READY_COMPONENT = (By.ID, "isppK-id-systemStateText-title")

    INSTRUMENT_NAME_LABEL = (By.XPATH, "//div[@class='lock-screen-title']")
    

