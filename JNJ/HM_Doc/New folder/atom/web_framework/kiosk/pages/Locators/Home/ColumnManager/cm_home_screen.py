from selenium.webdriver.common.by import By


class ColumnManagerHomeScreenLocators:
    COLUMN_TEMPERATURE_CONDITIONAL_CARD = (
        By.XPATH, "//div[@id='isppK-id-CM-conditionCard-temperature']//div[@class='condition-card-information-area']")

    TEMPERATURE_TITLE_ICON = (By.XPATH,
                              "//div[@id='isppK-id-CM-conditionCard-temperature']//div[@class='condition-card-header-icon']/mat-icon[1]")
    SETPOINT_TEMPERATURE = (
        By.XPATH, "//div[@class='condition-card-values']//div[2]//ics-condition-card-input[1]//div[1]//span[2]")
    SETPOINT_TEMPERATURE_AFTER_DECIMAL = (
        By.XPATH, "//div[@class='condition-card-values']//div[2]//ics-condition-card-input[1]//div[1]//span[3]")
    SETPOINT_TEMPERATURE_UNITS = (
        By.XPATH, "//div[@id='isppK-id-CM-conditionCard-temperature']//div[contains(text(),'Setpoint (°C)')]")

    SETPOINT_LOCATOR = (By.XPATH, "//div[@class='condition-card-values']/div[2]/ics-condition-card-input")
    SETPOINT_STATUS = (By.XPATH, "//div[@id='isppK-id-CM-conditionCard-temperature']//div[@class='condition-card-status-area']/div")
    CURRENT_TEMPERATURE = (
        By.XPATH, "//div[@id='isppK-id-CM-conditionCard-temperature']//span[@class='condition-card-firstVal']")
    CURRENT_TEMPERATURE_AFTER_DECIMAL = (
        By.XPATH, "//ics-cm-column-temperature-condition//span[3]")
    CURRENT_TEMPERATURE_UNITS = (
        By.XPATH, "//div[@id='isppK-id-CM-conditionCard-temperature']//div[contains(text(),'Current (°C)')]")
    STATUS_READ_BACK = (By.XPATH, "//div[@id='isppK-id-CM-conditionCard-temperature']//div[@class='condition-card-footer-status']")
    COLUMN_CONDITIONAL_CARD = (
        By.XPATH, "//div[@id='isppK-id-CM-command-column']//div[@class='condition-card-information-area']")

    COLUMN_POSITION_READ_BACK = (By.XPATH, "//div[@id='isppK-id-CM-command-column']//span[2]")
    PROGRESS_BAR_COMPONENT = (
        By.XPATH, "//div[@id ='isppK-id-CM-conditionCard-temperature']//div[@class='inner-progress-bar']//div[1]")
