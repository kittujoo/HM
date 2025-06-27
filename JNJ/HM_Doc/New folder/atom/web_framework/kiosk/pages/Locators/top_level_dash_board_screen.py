"""
File_Name: top_level_dash_board_screen.py
Desc: This file contains locator object of the web elements in the top level dash board screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 04/23/2020
__modified__ = "Sharmila Vairamani Added flow related locator - 02/23/2021
__modified__ = "Sharmila Vairamani" Added Column Manager related locators  - 03/09/2021
__modified__ ="Sharmila Vairamani"  Changes the locator cclass name - 03/16/2021
__modified__ ="Sharmila Vairamani"  Added sample temperature related locatros - 04/06/2021
__modified__ ="Tyler Prada"  Added valve position locators - 4/9/2021
_modified__ = "Sharmila Vairamani" Added channel condition card specific locators - 05/20/2021


"""
from selenium.webdriver.common.by import By


class TopLevelDashBoardScreenLocators:
    COLUMN_MANAGER_READ_BACK_CARD = (By.ID, "ispp-id-columnManager-readbackCard")
    SOLVENT_MANAGER_READ_BACK_CARD = (By.ID, "ispp-id-solventManager-readbackCard")
    TUV_DETECTOR_READ_BACK_CARD = (By.ID, "ispp-id-TUV-detector-readbackCard")
    SAMPLE_MANAGER_READ_BACK_CARD = (By.ID, "isppK-id-READBACK-group-a-card")
    FLOW_READ_BACK_MESSAGE = (
        By.XPATH, "//div[@id='isppK-id-READBACK-group-e-card']//ul/li[1]//ics-readback-card-input")
    FLOW_UNITS = (By.XPATH, "//span[contains(text(),'mL/min')]")

    COLUMN_POSITION_READ_BACK = (By.XPATH, "//div[@id='isppK-id-CM-command-column']//span[2]")
    COLUMN_MANAGER_CARD_READER = (By.ID, "isppK-id-READBACK-column-manager-card")
    COLUMN_TEMPERATURE_ACTUAL = (By.XPATH, "//*[@id='ispp-id-group-a-readbackCard']/div/ul/li[2]/div/div[2]/ics-readback-card-input[1]/span[1]")
    COLUMN_TEMPERATURE_ACTUAL_AFTER_DECIMAL = (By.XPATH, "//*[@id='ispp-id-group-a-readbackCard']/div/ul/li[2]/div/div[2]/ics-readback-card-input[1]/span[2]")
    COLUMN_TEMPERATURE = (
        By.XPATH, "//div[@id = 'isppK-id-READBACK-group-a-card']//li[2]//ics-readback-card-input[2]/span[1]")
    COLUMN_TEMPERATURE_AFTER_DECIMAL = (
        By.XPATH, "//div[@id = 'isppK-id-READBACK-group-a-card']//li[2]//ics-readback-card-input[2]/span[2]")
    COLUMN_TEMPERATURE_UNITS = (
        By.XPATH, "//div[@id = 'isppK-id-READBACK-group-a-card']//li[2]//span[@class = 'readback-card-item-units']")
    COLUMN_POSITION = (
        By.XPATH, "//div[@id = 'isppK-id-READBACK-column-manager-card']//li[3]//ics-readback-card-input[1]")
    SOLVENT_CARD_PRESSURE_UNIT = (By.XPATH,
                                  "//ics-readback-card[@id ='ispp-id-group-b-readbackCard']//"
                                  "li[1]//ics-readback-card-input//span[3]")
    SOLVENT_CARD_NUMBER_VALUE = (
        By.XPATH,
        "//div[@id = 'isppK-id-READBACK-group-b-card']//li[2]//ics-readback-card-input/span[1]")
    SOLVENT_CARD_DECIMAL_VALUE = (
        By.XPATH,
        "//div[@id = 'isppK-id-READBACK-group-b-card']//li[2]//ics-readback-card-input/span[2]")
    SAMPLE_TEMPERATURE = (
        By.XPATH, "//div[@id = 'isppK-id-READBACK-group-a-card']//ics-readback-card-input[1]/span[1]")
    SAMPLE_TEMPERATURE_AFTER_DECIMAL = (
        By.XPATH, "//div[@id = 'isppK-id-READBACK-group-a-card']//ics-readback-card-input[1]/span[2]")
    SAMPLE_TEMPERATURE_UNITS = (
        By.XPATH,
        "//div[@id = 'isppK-id-READBACK-group-a-card']//span[@class = 'readback-card-item-units']")
    SAMPLE_TEMPERATURE_SETPOINT = (By.XPATH, "//*[@id='ispp-id-group-a-readbackCard']/div/ul/li[1]/div/div[2]/ics-readback-card-input[2]/span[1]")
    SAMPLE_TEMPERATURE_SETPOINT_AFTER_DECIMAL = (By.XPATH, "//*[@id='ispp-id-group-a-readbackCard']/div/ul/li[1]/div/div[2]/ics-readback-card-input[2]/span[2]")

    SAMPLE_PRESSURE_VALUE = (
        By.XPATH, "//ics-readback-card[@id='ispp-id-group-b-readbackCard']//li[3]//ics-readback-card-input/span[1]")
    SAMPLE_PRESSURE_AFTER_DECIMAL_VALUE = (
        By.XPATH, "//ics-readback-card[@id='ispp-id-group-b-readbackCard']//li[3]//ics-readback-card-input/span[2]")
    SAMPLE_PRESSURE_UNITS = (
        By.XPATH, "//ics-readback-card[@id='ispp-id-group-b-readbackCard']//li[3]//ics-readback-card-input/span[3]")

    SAMPLE_CARD_VALVE_POSITION = (By.XPATH, "//ics-readback-card//li[4]//ics-readback-card-input//span")
    LAMP_STATE = (
        By.XPATH, "//div[@id='isppK-id-READBACK-group-d-card']//li[1]//ics-readback-card-input")
    WAVE_LENGTH_1_READ_BACK_VALUE = (
        By.XPATH, "//div[@id='isppK-id-READBACK-group-d-card']//li[2]//ics-readback-card-input/span")
    WAVE_LENGTH_1_READ_BACK_VALUE_AFTER_DECIMAL = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[2]//ics-readback-card-input/span[2]")
    WAVE_LENGTH_1_READ_BACK_UNITS = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[2]//ics-readback-card-input/span[3]")
    WAVE_LENGTH_2_READ_BACK_VALUE = (
        By.XPATH, "//div[@id='isppK-id-READBACK-group-d-card']//li[3]//ics-readback-card-input/span")
    WAVE_LENGTH_2_READ_BACK_UNITS = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[3]//ics-readback-card-input/span[3]")
    CHANNEL_A_ABSORBANCE_VALUE_BEFORE_DECIMAL = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[2]//ics-readback-card-input[2]/span")
    CHANNEL_A_ABSORBANCE_VALUE_AFTER_DECIMAL = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[2]//ics-readback-card-input[2]/span[2]")
    CHANNEL_A_ABSORBANCE_UNITS = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[2]//ics-readback-card-input[2]/span[3]")
    CHANNEL_B_ABSORBANCE_VALUE_BEFORE_DECIMAL = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[3]//ics-readback-card-input[2]/span")
    CHANNEL_B_ABSORBANCE_VALUE_AFTER_DECIMAL = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[3]//ics-readback-card-input[2]/span[2]")
    CHANNEL_B_ABSORBANCE_UNITS = (
        By.XPATH,
        "//div[@id='isppK-id-READBACK-group-d-card']//li[3]//ics-readback-card-input[2]/span[3]")
    WAVE_LENGTH_2_READ_BACK_VALUE_AFTER_DECIMAL = (
        By.XPATH, "//div[@id='isppK-id-READBACK-group-d-card']//li[3]//ics-readback-card-input/span[2]")

    # Icons are on top level dashboard, minimized icons are within condition card screens
    COLUMN_ICON = (By.XPATH, "//ics-tray[@id='ispp-id-CM-column-icon']//div[@class='tray-icon-circle available']")
    COLUMN_ICON_MIN = (By.XPATH, "//ics-system-schematic//div[contains(@class,'hot-spot-item')][3]//ics-tray//div[contains(@class,'tray-container')]")
    
    TUV_ICON = (By.XPATH, "//ics-tray[@id='ispp-id-TUV-wavelength-icon']//div[@class='tray-icon-circle available']")
    TUV_ICON_MIN = (By.XPATH, "//ics-system-schematic//div[contains(@class,'hot-spot-item')][1]//ics-tray//div[contains(@class,'tray-container')]")
    
    BOTTLE_ICON = (By.XPATH, "//ics-tray[@id = 'ispp-id-solvent-bottle-icon']//div[@class='tray-icon-circle available']")
    BOTTLE_ICON_MIN = (By.XPATH, "//ics-system-schematic//div[contains(@class,'hot-spot-item')][5]//ics-tray//div[contains(@class,'tray-container')]")
    
    SAMPLE_ICON = (By.XPATH, "//ics-tray[@id='ispp-id-SM-injection-icon']//div[@class='tray-icon-circle available']")
    SAMPLE_ICON_MIN = (By.XPATH, "//ics-system-schematic//div[contains(@class,'hot-spot-item')][2]//ics-tray//div[contains(@class,'tray-container')]")
    
    SOLVENT_ICON = (By.XPATH, "//ics-tray[@id='ispp-id-QSM-flow-icon']//div[@class='tray-icon-circle available']")
    SOLVENT_ICON_MIN = (By.XPATH, "//ics-system-schematic//div[contains(@class,'hot-spot-item')][4]//ics-tray//div[contains(@class,'tray-container')]")
    
    AMBIENT_TEMPERATURE = (By.XPATH, "//ics-readback-card[@id = 'ispp-id-group-a-readbackCard']//li[3]//ics-readback-card-input//span[1]")
    AMBIENT_TEMPERATURE_AFTER_DECIMAL = (By.XPATH, "//ics-readback-card[@id = 'ispp-id-group-a-readbackCard']//li[3]//ics-readback-card-input//span[2]")
    AMBIENT_TEMPERATURE_UNITS = (By.XPATH, "//ics-readback-card[@id = 'ispp-id-group-a-readbackCard']//li[3]//ics-readback-card-input//span[3]")
    COLUMN_TEMPERATURE_OFF_MESSAGE = (By.XPATH, "//ics-readback-card[@id ='ispp-id-group-a-readbackCard']//li[2]//ics-readback-card-input[2]")
    LAMP_USED_HOURS_READBACK_MESSAGE = (By.XPATH, "//ics-readback-card[@id ='ispp-id-group-d-readbackCard']//li[4]//ics-readback-card-input//span[1]")
    LAMP_TOTAL_HOURS_READBACK_MESSAGE = (By.XPATH, "//ics-readback-card[@id ='ispp-id-group-d-readbackCard']//li[4]//ics-readback-card-input//span[3]")
    LAMP_HOURS_STATE = (By.XPATH, "//ics-readback-card-group-d//ics-readback-card//li[4]")
    SAMPLE_INJECTIONS_COUNT = (By.XPATH, "//*[@id='ispp-id-group-c-readbackCard']/div/ul/li/div/div[2]/ics-readback-card-input/span[1]")
