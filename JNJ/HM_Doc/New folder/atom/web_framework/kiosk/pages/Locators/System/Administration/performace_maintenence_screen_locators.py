from selenium.webdriver.common.by import By


class PerformanceMaintenanceScreenLocators:
    MONTHS_PICKER_WHEEL = (By.XPATH, "//ics-picker-base//div[@class='wheel-wrapper']//div[1]//ul")
    DEFAULT_MONTH_BUTTON = (By.XPATH, "//ics-picker-button")
    PERFORMANCE_MAINTENANCE = (By.XPATH, "//div[contains(text(), 'Performance Maintenance')]")
    PERFORMANCE_MAINTENANCE_MENU = (
        By.XPATH,
        "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Performance Maintenance')]")
    PERFORMANCE_MAINTENANCE_TOGGLE = (By.XPATH, "//ics-toggle[@id='ispp-id-system-qualification-toggle']//mat-slide-toggle")
    MAINTENANCE_EXPIRATION_TITLE = (By.XPATH, "//div[contains(text(),' Next Performance Maintenance is due')]")
    MAINTENANCE_EXPIRATION_LABEL = (
        By.XPATH, "// div[contains(text(), ' Next Performance Maintenance is due')]/following-sibling::div[1]")
    PERFORMANCE_MAINTENANCE_TAB_EXPIRY = (
        By.XPATH, "// div[contains(text(), 'Performance Maintenance')]/following-sibling::div[1]")
    NOTE_TAB = (By.XPATH, "//div[contains(text(),'Note')]")
    ADD_ENTRY_TEXT_AREA = (By.XPATH, "//textarea[contains(@class, 'comment-area')]")
    ADD_OR_EDIT_NOTE_TITLE = (By.XPATH, "//div[contains(text(), ' Add or Edit Note ')]")
    NOTE_TAB_CONTENT = (By.XPATH, "// div[contains(text(),'Note')]/following-sibling::div[1]")
    DONE_BUTTON_FOR_NOTES = (By.XPATH,
                             "//div[contains(@class,'global-overlay')][3]//ics-primary-action//ics-tray[@ng-reflect-icon='ics-img-done']")
