"""
File_Name: dash_board_screen_locators.py
Desc: This file contains locator object of the webelements in the dashboard screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__modified__  == "Sharmila Vairamani" changed the ids to reflect the latest change - 10/16/2020
__modified__ = "Sharmila Vairamani" changed the locator for commands- 10/20/2020
__modified__ = "Sharmila Vairamani" removed the locator for settings- 10/21/2020
__modified__ = "Sharmila Vairamani" Added locators for  HEALTH_PAGE_TWO 2/23/2022


"""
from selenium.webdriver.common.by import By


class DashBoardsScreenPageLocators:
    HOME = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-home']/div[1]")
    COMMANDS = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-commands']/div[1]")
    INSTRUMENT = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-settings']/div[1]")
    SETUP = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-setup']/div[1]")
    MAINTAIN = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-maintain']/div[1]")
    PLOTS = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-plots']/div[1]")
    HEALTH = (By.XPATH, "//ics-navigation-item[@id='isppK-id-navigationItem-diagnose']/div[1]")
    NOTIFICATION = (By.XPATH, "//ics-notification-toast[@id='isppK-id-try-notification']/div[1]/ics-tray[1]/div[1]/div[1]")
    USER_SETTINGS = (By.XPATH, "//ics-tray[@id='userTray']/div[1]/div[1]")
    LOCK_ICON = (By.ID, "lockTray")
    HEADER = (By.XPATH, "//div[contains(text(),'Ready')]")
    SYSTEM_CURRENT_STATE = (By.ID, "ispp-id-systemStateText-title")
    HEALTH_PAGE_TWO = (By.XPATH, "//li//a[@id='isppK-id-pagination-page2']")
    FLOW_PATH_SCHEMATIC_ICON = (By.XPATH, "//ics-fluidic-path[@class ='fluidic-path']")
    FLOW_PATH_LINE = (By.XPATH, "//ics-fluidic-path[@class ='fluidic-path']//*[local-name()='svg']//*[local-name()='path'][1]")
    SAMPLE_TEMPERATURE = (By.XPATH, "//div[@id='isppK-id-READBACK-group-a-card']//span")
    LAMP_STATE = (By.XPATH, "//div[@id='isppK-id-READBACK-group-d-card']//li[1]//span[1]")
    SYSTEM_STATE = (By.ID, "ispp-id-systemStateText-title")
    PRESSURE_UNIT = (By.XPATH, "//div[text()='Delta Pressure']/parent::div/descendant::span[@class='readback-card-item-units']")
