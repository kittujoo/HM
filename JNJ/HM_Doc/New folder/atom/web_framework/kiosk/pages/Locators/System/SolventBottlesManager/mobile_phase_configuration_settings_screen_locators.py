"""
File_Name: mobile_phase_configuration_settings_screen_locators.py
Desc: This file contains locator objects of the web elements in solvent bottle configuration screen locators
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/19/2022

"""
from selenium.webdriver.common.by import By


class MobilePhaseConfigurationScreenLocators:
    SOLVENTS_A_PANEL = (By.XPATH, "//ics-vertical-information-panel//li[1]")
    SOLVENTS_A_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-0']")
    BOTTLE_A_VOLUME_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-bottle-size-0']")
    SOLVENT_A_COLOUR_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-line-color-0']")
    SOLVENT_VOLUME_A_READ_BACK_VALUE = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-solvent-bottle-size-0']//div[@class='info-list-item-subtitle ng-star-inserted']")
    SOLVENT_VOLUME_B_READ_BACK_VALUE = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-solvent-bottle-size-1']//div[@class='info-list-item-subtitle ng-star-inserted']")
    SOLVENT_VOLUME_C_READ_BACK_VALUE = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-solvent-bottle-size-1']//div[@class='info-list-item-subtitle ng-star-inserted']")
    SOLVENT_VOLUME_D_READ_BACK_VALUE = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-solvent-bottle-size-1']//div[@class='info-list-item-subtitle ng-star-inserted']")
    SOLVENTS_B_PANEL = (By.XPATH, "//ics-vertical-information-panel//li[2]")
    SOLVENTS_B_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-1']")
    BOTTLE_B_VOLUME_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-bottle-size-1']")
    SOLVENT_B_COLOUR_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-line-color-1']")

    SOLVENTS_C_PANEL = (By.XPATH, "//ics-vertical-information-panel//li[3]")
    SOLVENTS_C_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-2']")
    BOTTLE_C_VOLUME_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-bottle-size-2']")
    SOLVENT_C_COLOUR_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-line-color-2']")

    SOLVENTS_D_PANEL = (By.XPATH, "//ics-vertical-information-panel//li[4]")
    SOLVENTS_D_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-3']")
    BOTTLE_D_VOLUME_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-bottle-size-3']")
    SOLVENT_D_COLOUR_PANEL = (By.XPATH, "//ics-info-list-item[@id= 'ispp-id-solvent-line-color-3']")

    SOLVENT_BOTTLE_STRING = "//ics-dynamic-component[@ng-reflect-id='ispp-id-modal-info-keypad-dyna']"
    SOLVENT_BOTTLE_SIZE = (By.XPATH, "//ics-dynamic-component[@ng-reflect-id='ispp-id-modal-info-keypad-dyna']//ul")
    RED_ICON = (By.XPATH, "//ics-color-picker[@class='ics-color-picker']//div[@id='ispp-id-colorPicker-option-01--v01']")
    PINK_ICON = (By.XPATH, "//ics-color-picker[@class='ics-color-picker']//div[@id='ispp-id-colorPicker-option-03--v01']")
    GREEN_ICON = (
        By.XPATH, "//ics-color-picker[@class='ics-color-picker']//div[@id ='ispp-id-colorPicker-option-06--v01']")

    BLUE_ICON = (By.XPATH, "//ics-color-picker[@class='ics-color-picker']//div[@id "
                           "='ispp-id-colorPicker-option-05--v03']")

    YELLOW_ICON = (
        By.XPATH, "//ics-color-picker[@class='ics-color-picker']//div[@id ='ispp-id-colorPicker-option-08--v01']")

    ORANGE_ICON = (
        By.XPATH, "//ics-color-picker[@class='ics-color-picker']//div[@id ='ispp-id-colorPicker-option-10--v03']")

    SOLVENT_A_LINE_COLOR_ICON = (By.XPATH, "//ics-vertical-information-panel//li[1]//ics-solvent-badge/div")
    SOLVENT_B_LINE_COLOR_ICON = (By.XPATH, "//ics-vertical-information-panel//li[2]//ics-solvent-badge/div")
    SOLVENT_C_LINE_COLOR_ICON = (By.XPATH, "//ics-vertical-information-panel//li[3]//ics-solvent-badge/div")
    SOLVENT_D_LINE_COLOR_ICON = (By.XPATH, "//ics-vertical-information-panel//li[4]//ics-solvent-badge/div")
