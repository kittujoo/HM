from selenium.webdriver.common.by import By
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class OverwriteWindowPage(WinAppBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_overwrite_dialog_opened(self, name):
        overwrite_popup_name_locator = (By.NAME, name)
        return self.is_displayed_with_timeout(3, overwrite_popup_name_locator)
