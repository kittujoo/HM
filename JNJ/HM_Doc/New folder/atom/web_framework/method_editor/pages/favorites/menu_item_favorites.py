from collections import Counter
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage
from utilities.logger import Logger


class FavoritesMenu(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    _favorite_list_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']//List[2]//ListItem/Text[1]")
    _null_favorite_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']//List[2]/ListItem[3]")


    def validate_expected_favorites(self, expected_favorite_settings: list):
        elements = self.find_elements(self._favorite_list_locator)
        actual_favorite_settings = [element.get_attribute("Name") for element in elements]

        assert Counter(expected_favorite_settings) == Counter(actual_favorite_settings), \
            f"The number of favorites is incorrect. Expected: [{expected_favorite_settings}], Actual: [{actual_favorite_settings}]"
