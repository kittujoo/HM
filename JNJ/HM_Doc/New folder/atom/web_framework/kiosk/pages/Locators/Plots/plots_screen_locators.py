"""
File_Name: plots_screen_locators.py
Desc: This file contains locator object of the web elements in the plots screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/08/2021
__modified__ = 'shamrila Vairamani" Added settings screen locators 05/03/2021
__modified__ = "Tyler Prada" Added time picker component wheels 3/1/22

"""
from selenium.webdriver.common.by import By


class PlotScreenLocators:
    FIVE_MINUTE_TIME_WINDOW = (By.XPATH, "//div[@class='ics-core-selector']//li[1]")
    FIFTEEN_MINUTE_TIME_WINDOW = (By.XPATH, "//div[@class='ics-core-selector']//li[2]")
    CUSTOM_TIME_WINDOW = (By.XPATH, "//div[@class='ics-core-selector']//li[3]")
    SYSTEM_ICON = (By.XPATH, "//ics-plot-controls-tab[@class='ics-plot-controls-tab']//div[contains(text(),'SYSTEM')]")
    ACQUISITION_ICON = (By.XPATH, "//div[contains(text(),'ACQUISITION')]")
    SETTINGS_ICON = (By.XPATH, "//div[contains(text(),'SETTINGS')]")
    PLAY_PAUSE_BUTTON = (By.XPATH, "//div[@class='plot-play-pause-content']//div[contains(@class,'tray-icon-circle')]//mat-icon")
    X_AXIS_LABELS = (By.XPATH, "//section[@class='plots-controls']//ics-plot-x-axis")
    TIME_BEFORE_DECIMAL = (By.XPATH, "//ics-plot-x-axis//*[@text-anchor='start']//*[@class='x-axis-first-value']")
    TIME_AFTER_DECIMAL = (By.XPATH, "//ics-plot-x-axis//*[@text-anchor='start']//*[@class='x-axis-second-value'][1]")
    TIME_UNIT = (By.XPATH, "//ics-plot-x-axis//*[@text-anchor='start']//*[@class='x-axis-second-value'][2]")
    TIME_NOW_VALUE = (By.XPATH, "//ics-plot-x-axis//*[@text-anchor='end']//*[@class='x-axis-second-value'][2]")
    PLAY_PAUSE_ELEMENT = (By.XPATH, "//div[@class='plot-play-pause-content']//ics-tab//ics-tray")
    TIME_WINDOW_COMPONENT = (By.XPATH, "//div[@class='system-plot-controls-core-selector']")
    PLOT_SCREEN = (By.XPATH, "//div[@class='system-plots-content']//ics-plot//figure//span[@class='highcharts-title']")

    CHART_ELEMENTS = (By.XPATH, "//div[@id='ispp-id-plots-container']//div[@class='highcharts-container ']")
    CHART = (By.XPATH, "//div[@id='ispp-id-plots-container']")
    CHART_TITLES = (By.XPATH, "//div[@id='ispp-id-plots-container']//div[@class='highcharts-container ']//span[@class='chart-title']")
    PLOTS_GRAPH = (By.XPATH, "//div[@id='ispp-id-plots-container']//div[@class='highcharts-container ']//*[local-name()='svg' ]/*[local-name()='g'][3]//*[local-name()='path' ][1]")

    # GRAPH_STATE = (By.XPATH,
    #                          "//div[@id='ispp-id-plots-container']//div[@class='highcharts-container ']//*[local-name()='svg' ]/*[local-name()='g'][3]//*[local-name()='path'][3]")
    GRAPH_STATE= (By.XPATH, "//div[@id='ispp-id-plots-container']//div[@class='highcharts-container ']//*[local-name()='svg' ]/*[local-name()='g'][3]//*[local-name()='path'][@visibility='visible']")

class PlotsSettingsScreenLocators:
    FIVE_MINUTE_TIME_WINDOW = (By.XPATH, "//div[@class='plot-settings-hub']//div[@class='ics-core-selector']//li[1]")
    FIFTEEN_MINUTE_TIME_WINDOW = (By.XPATH, "//div[@class='plot-settings-hub']//div[@class='ics-core-selector']//li[2]")
    CUSTOM_TIME_WINDOW = (By.XPATH, "//div[@class='plot-settings-hub']//div[@class='ics-core-selector']//li[3]")
    HOURS_PICKER_WHEEL = (By.XPATH, "//ics-picker-base//div[@class='wheel-wrapper']//ul")
    MINUTES_PICKER_WHEEL = (By.XPATH,
                            "//ics-picker-base//div[@class='wheel-wrapper']/div[3]//ul")
    CUSTOM_TEXT = (By.XPATH, "//div[@class='plot-settings-hub']//div[@class='ics-core-selector']//li[3]/div")
    TIME_WINDOW_COMPONENT = (By.XPATH, "//div[@id='ispp-id-time-window-picker']")
    FIRST_MORE_ACTION_ICON = (By.XPATH, "//mat-icon[@id='ispp-id-plot-menu-moreActionsIcon']")
    FIRST_SETTINGS_ICON = (
        By.XPATH, "//mat-icon[@id='ispp-id-plot-menu-settingsIcon']")
    FIRST_MAXIMISE_ICON = (
        By.XPATH, "//mat-icon[@id='ispp-id-plot-menu-maximizeIcon']")
    SECOND_MORE_ACTION_ICON = (By.XPATH, "//div[@id='chart_1']//mat-icon[@id='ispp-id-plot-menu-moreActionsIcon']")
    THIRD_MORE_ACTION_ICON = (By.XPATH, "//div[@id='chart_2']//mat-icon[@id='ispp-id-plot-menu-moreActionsIcon']")
    SECOND_SETTINGS_ICON = (
        By.XPATH, "//div[@id='play-pause-container']/div[3]//mat-icon[@id='ispp-id-plot-menu-settingsIcon']")
    SECOND_MAXIMISE_ICON = (
        By.XPATH, "//div[@id='play-pause-container']/div[3]//mat-icon[@id='ispp-id-plot-menu-maximizeIcon']")
    THIRD_SETTINGS_ICON = (
        By.XPATH, "//div[@id='play-pause-container']/div[4]//mat-icon[@id='ispp-id-plot-menu-settingsIcon']")
    THIRD_MAXIMISE_ICON = (
        By.XPATH, "//div[@id='play-pause-container']/div[4]//mat-icon[@id='ispp-id-plot-menu-maximizeIcon']")
    AVAILABLE_MORE_ACTION_ICONS = (By.ID, "ispp-id-plot-menu-moreActionsIcon")
    TIME_WINDOW_HEADER = (By.ID, "ispp-id-plot-time-window")
    CENTER_PLAY_PAUSE_BUTTON = (By.XPATH, "//div[@class='play-pause-icon']")
    CENTER_PLAY_PAUSE_ELEMENT = (By.XPATH, "//div[@class='play-pause-icon']/mat-icon")
    PLOT_ONE_TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@id ='ispp-id-plot-settings-show-plot1']//mat-slide-toggle")
    PLOT_TWO_TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@id ='ispp-id-plot-settings-show-plot2']//mat-slide-toggle")
    PLOT_THREE_TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@id ='ispp-id-plot-settings-show-plot3']//mat-slide-toggle")
    PLOT_FOUR_TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@id ='ispp-id-plot-settings-show-plot4']//mat-slide-toggle")

    PLOT_ONE_TAB = (
        By.XPATH, "//ics-dynamic-modal-panel[@id = 'ispp-id-plot-settings-hub']//ics-vertical-information-panel//li[2]")
    PLOT_TWO_TAB = (
        By.XPATH, "//ics-dynamic-modal-panel[@id = 'ispp-id-plot-settings-hub']//ics-vertical-information-panel//li[3]")
    PLOT_THREE_TAB = (
        By.XPATH, "//ics-dynamic-modal-panel[@id = 'ispp-id-plot-settings-hub']//ics-vertical-information-panel//li[4]")
    PLOT_FOUR_TAB = (
        By.XPATH, "//ics-dynamic-modal-panel[@id = 'ispp-id-plot-settings-hub']//ics-vertical-information-panel//li[5]")
    PLOTS_SPINNER_LOCATOR = (By.XPATH, "//ics-dynamic-component//div[@class='vertical-selector-menu']")
    PLOT_ONE_COLOR_TAB = (
        By.XPATH,
        "//ics-info-list-item[@id = 'ispp-id-plot-settings-show-plot1-color']//div[@class='info-list-item-body']")
    PLOT_TWO_COLOR_TAB = (
        By.XPATH,
        "//ics-info-list-item[@id = 'ispp-id-plot-settings-show-plot2-color']//div[@class='info-list-item-body']")
    PLOT_THREE_COLOR_TAB = (
        By.XPATH,
        "//ics-info-list-item[@id = 'ispp-id-plot-settings-show-plot3-color']//div[@class='info-list-item-body']")
    PLOT_FOUR_COLOR_TAB = (
        By.XPATH,
        "//ics-info-list-item[@id = 'ispp-id-plot-settings-show-plot4-color']//div[@class='info-list-item-body']")
    COLOR_SELECTOR_COMPONENT = (By.XPATH, "//ics-color-picker[@class='ics-color-picker']")
    RED_ICON = (
        By.XPATH,
        "//ics-picker-wrapper//div[@id='ispp-id-colorPicker-option-01--v01']")
    PINK_ICON = (
        By.XPATH,
        "//ics-picker-wrapper//div[@id='ispp-id-colorPicker-option-03--v01']")
    BLUE_ICON = (
        By.XPATH,
        "//ics-picker-wrapper//div[@id='ispp-id-colorPicker-option-05--v01']")
    GREEN_ICON = (
        By.XPATH,
        "//ics-picker-wrapper//div[@id='ispp-id-colorPicker-option-06--v03']")
    YELLOW_ICON = (
        By.XPATH,
        "//ics-picker-wrapper//div[@id='ispp-id-colorPicker-option-08--v03']")
    ORANGE_ICON = (
        By.XPATH,
        "//ics-picker-wrapper[@ng-reflect-title='Select Color']//div[@id='ispp-id-colorPicker-option-09--v01']")
    ALPHABETIC_ORDER_OPTION = (By.XPATH, "//ics-vertical-selector//ics-core-selector[1]//ul/li[1]")
    CATOGARY_OPTION =  (By.XPATH, "//ics-vertical-selector//ics-core-selector[1]//ul/li[2]")  
    DEFAULT_TIME_BUTTON = (By.XPATH, "//div[@class ='buttons-container']//ics-picker-button") 


class TimeWheelLocators:
    ONE_HOUR = (By.XPATH, "//ics-picker-base//ul/li[2]")
    # ONE_MINUTE = (By.XPATH, "//div[@class='wheel wheel-date ng-star-inserted'][3]//li[2]")
    ONE_MINUTE = (By.XPATH,
                  "//ics-picker-base//div[3]//ul/li[3]")
    TWO_HOUR = (By.XPATH, "//ics-picker-base//ul/li[3]")
    TWO_MINUTE = (By.XPATH, "//ics-picker-base//div[3]//ul/li[4]")
    THREE_HOUR = (By.XPATH, "//ics-picker-base//ul/li[4]")
    THREE_MINUTE = (By.XPATH, "//ics-picker-base//div[3]//ul/li[5]")
    WHEEL_COMPONENT_STRING = "//li[contains(@style,'rotateX(-25deg)')]//div"
