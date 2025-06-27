from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class WashTimePage(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    _wash_time_title_locator = (By.XPATH, "//Text[contains(@Name, 'Wash Time')]")
    _wash_time_settings_locator = (By.XPATH, "//Text[contains(@Name, 'Wash Time (s)')]")
    _wash_time_settings_summary_locator = (By.XPATH, "//Text[contains(@Name, 'Specify time for additional needle washing between injections')]")
    _group_title_locator = (By.XPATH, "//Text[contains(@Name, 'Wash Time')]")

    _wash_time_editbox_locator = (By.XPATH, "//Text[@Name='Specify time for additional needle washing between injections']/following::Spinner")
    _wash_time_hint_locator = (By.XPATH, "//Text[@Name='Specify time for additional needle washing between injections']/following::Spinner/following::Text")

    _favorite_icon_locator = (By.XPATH, "//Text[contains(@Name, 'Wash Time')]/following::Button")

    def get_wash_time_title(self):
        return self.get_text(self._wash_time_title_locator)

    def get_wash_time_settings_title(self):
        return self.get_text(self._wash_time_settings_locator)

    def get_wash_time_settings_summary(self):
        return self.get_text(self._wash_time_settings_summary_locator)

    def get_wash_time_hint(self):
        return self.get_text(self._wash_time_hint_locator)

    def get_settings_group_title(self):
        return self.get_text(self._group_title_locator)

    def get_wash_time_editbox_value(self):
        return self.get_text(self._wash_time_editbox_locator)

    def set_wash_time_editbox(self, wash_time: str):
        self.set_text(self._wash_time_editbox_locator, str(wash_time))

    def set_favorite(self):
        self.click_on_element(self._favorite_icon_locator)

    def is_wash_time_displayed(self) -> bool:
        return self.is_displayed_with_timeout(5, self._group_title_locator)
