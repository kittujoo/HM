from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logger import Logger
from web_framework.web_driver_common.constants import WIN_APP_BY
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class NewSystemWizardPage(WinAppBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    def select_create_new_system_rb(self):
        new_system_rb = self._driver.find_element(WIN_APP_BY, '12234')
        new_system_rb.click()

    def click_next(self):
        next_button = self._driver.find_element(WIN_APP_BY, '12324')
        next_button.click()

    def select_node(self, node_name):
        node_name_item = self._driver.find_element_by_name(node_name)
        node_name_item.click()

    def add_instruments_to_system(self, instruments_name):
        # select the first node in the tree, so we can navigate at the end of the list
        unused_components = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.NAME, "Unused Components")), "Element 'Unused Components' not found.")
        ActionChains(self._driver).send_keys_to_element(unused_components, Keys.END).perform()

        instruments_item = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.NAME, instruments_name)), f"Element {instruments_name} not found.")
        ActionChains(self._driver).double_click(on_element=instruments_item).perform()
        instruments_sub_item = self._driver.find_element_by_xpath(f"//TreeItem[@Name='{instruments_name}']/TreeItem")
        ActionChains(self._driver).double_click(on_element=instruments_sub_item).perform()

    def set_sharing_with_world(self):
        share_with_network_checkbox = self._driver.find_element(WIN_APP_BY, '12248')
        share_with_network_checkbox.click()
        owner_group_and_worlds_rb = self._driver.find_element(WIN_APP_BY, '12252')
        owner_group_and_worlds_rb.click()

    def set_system_name(self, system_name, system_comment=None):
        system_name_edit_element = self._driver.find_element(WIN_APP_BY, '12228')
        system_name_edit_element.clear()
        system_name_edit_element.send_keys(system_name)
        if system_comment:
            system_comment_edit_element = self._driver.find_element(WIN_APP_BY, '12233')
            system_comment_edit_element.clear()
            system_comment_edit_element.send_keys(system_name)

    def click_finish(self):
        finish_button = self._driver.find_element(WIN_APP_BY, '12325')
        finish_button.click()

    def confirm_system_online(self):
        ok_button = self._driver.find_element(WIN_APP_BY, '2')
        ok_button.click()

    def is_duplicated_system_windows_exists(self):
        return self.is_displayed_with_timeout(3, (By.NAME, "There is already a system named atom_new_system configured on this node."))

    def is_new_chromatographic_type_entry_wizard_displayed(self, timeout=10):
        return self.is_displayed_with_timeout(timeout, (By.NAME, "New Chromatographic System Wizard - Type Entry"))
