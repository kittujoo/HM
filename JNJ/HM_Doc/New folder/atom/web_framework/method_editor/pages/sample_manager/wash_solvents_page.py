from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class WashSolventsPage(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    _favorite_icon_locator = (By.XPATH, "//Text[contains(@Name, 'Wash Solvents')]/following::Button")

    def set_favorite(self):
        self.click_on_element(self._favorite_icon_locator)

