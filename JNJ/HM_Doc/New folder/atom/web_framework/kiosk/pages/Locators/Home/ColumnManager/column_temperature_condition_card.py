from selenium.webdriver.common.by import By


class ColumnTemperatureSettingScreenLocators:
    HEADER = (By.ID, "ispp-id-CM-toggle-temperatureSettings")
    TEMPERATURE_EDIT_FIELD_HEADER = (
    By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-editField-setpointSettings']//div[contains(text(),'Temperature Setpoint (ºC)')]")
    TEMPERATURE_EDIT_FIELD_COMPONENT = (By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-editField-setpointSettings']//input")
    TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-toggle-temperatureSettings']//mat-slide-toggle")
    TOGGLE_BUTTON_ACTION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-toggle-temperatureSettings']//div[@class='ics-toggle']")
    COLUMN_TEMPERATURE_LIST = (By.XPATH, "//ics-picker-base//div[contains(@class,wheel)][1] /ul[@class = 'wheel-scroll']")
    SCROLL_WINDOW_HEADER = (By.XPATH, "//ics-picker-content[@ng-reflect-id = 'ispp-id-column-temperature-pic']")
    TEMPERATURE_READ_BACK_MESSAGE = (By.XPATH, "//ics-info-list-item[@id = 'ispp-id-CM-editField-setpointSettings']//div[contains(@class,'subtitle')][1]")
    SETPOINT_TEMPERATURE_HEADER = (By.ID, "ispp-id-CM-editField-setpointSettings")
