from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class SampleSetsTab(WinAppBasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        pass

    def validate_opened(self):
        pass
