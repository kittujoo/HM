from selenium.webdriver.common.by import By

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.web_driver_common.constants import WIN_APP_BY


class SampleSetMethodPage(WinAppBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_toolbar_save_button(self):
        locator = (By.NAME, "Save")
        self.click_on_element(locator)

    def set_current_sample_set_name(self, method_name):
        locator = (WIN_APP_BY, '6188')
        method_name_input = self.find_element(locator)
        method_name_input.clear()
        method_name_input.send_keys(method_name)

    def set_current_sample_set_comments(self, method_comment):
        locator = (WIN_APP_BY, '7709')
        method_name_input = self.find_element(locator)
        method_name_input.clear()
        method_name_input.send_keys(method_comment)

    def click_dialog_save_button(self):
        locator = (WIN_APP_BY, '6189')
        self.click_on_element(locator)

    def is_overwrite_dialog_opened(self) -> bool:
        overwrite_popup_name_locator = (By.NAME, "Run Samples")
        return self.is_displayed_with_timeout(3, overwrite_popup_name_locator)
