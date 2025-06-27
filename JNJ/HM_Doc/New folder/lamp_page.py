from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.logger import Logger
from utilities.string_utility import str_to_float
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class LampPage(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    _lamp_menu_title_locator = (By.XPATH, "//Text[contains(@Name, 'Lamp')]")
    _lamp_sub_menu_title_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/Text[@Name='Lamp']")
    # _lamp_sub_menu_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/List/ListItem[Text[@Name='SLamp']]")
    _lamp_sub_menu_state_title_locator = (By.XPATH, "//Text[contains(@Name, 'Lamp State')]")
    _lamp_sub_menu_state_description_title_locator = (
        By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/Text[@Name='Caution: Turn off lamp if this is shut down method only']")

    def get_lamp_menu_tile(self):
        return self.get_text(self._lamp_menu_title_locator)

    def get_lamp_setting_group_title(self):
        return self.get_text(self._lamp_sub_menu_state_title_locator)

    def get_lamp_state_setting_title(self):
        return self.get_text(self._lamp_sub_menu_state_title_locator)

    def get_lamp_state_setting_summary_title(self):
        return self.get_text(self._lamp_sub_menu_state_description_title_locator)
