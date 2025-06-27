from selenium.webdriver.common.by import By


class PerformanceCounterScreenLocators:

    PERFORMANCE_COUNTERS_HEADER = (
        By.XPATH, "//div[contains(text(), 'View and configure available performance counters')]")
    MORE_OPTIONS_BUTTON = (
        By.XPATH, "//*[@id='ispp-id-performance-counters-hub']/div/div[2]/ics-vertical-scrolling-list"
                  "/div/div[3]/div/ics-total-injections-counter/ics-performance-counters/div/div/section[3]/ics-slide-out-menu/div/div[1]")
    RESET_BUTTON = (By.XPATH, "//div[contains(text(), 'Reset')]")
    RESET_CONFIRM_BUTTON = (By.XPATH, "//*[@id='ispp-id-reset-counter-dialog']/ics-dialog/div/div/div[2]/div[1]")
    INJECTION_COUNT = (By.XPATH, "//*[@id='ispp-id-performance-counters-hub']/div/div[2]/ics-vertical-scrolling-list/div/div[3]/div/"
                                 "ics-total-injections-counter/ics-performance-counters/div/div/section[2]/div[1]")
    BACK_BUTTON = (By.XPATH, "//*[@id='mat-dialog-0']/ics-secondary-panel-base/div/div[1]/ics-dynamic-component/"
                             "ics-secondary-panel-header/div/div[1]/div[2]/ics-primary-action")
    LAMP_LIFE_HOURS = (By.XPATH, "//*[@id='ispp-id-performance-counters-hub']/div/div[2]/ics-vertical-scrolling-list/div/div[3]/"
                                 "div/ics-lamp-life-counter/ics-performance-counters/div/div[1]/section[1]/div[2]")
    LAMP_HOURS_COUNTER = (By.XPATH, "//*[@id='ispp-id-performance-counters-hub']/div/div[2]/ics-vertical-scrolling-list/div/div[3]/"
                                    "div/ics-lamp-life-counter/ics-performance-counters/div/div[1]/section[2]/div[1]")
    LAMP_PROGRESS_BAR = (By.XPATH, "//*[@id='ispp-id-performance-counters-hub']//div[contains(@style, 'width')]")
