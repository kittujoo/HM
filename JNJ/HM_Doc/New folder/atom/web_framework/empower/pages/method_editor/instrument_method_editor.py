from web_framework.web_driver_common.constants import WIN_APP_BY
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class InstrumentMethodEditorPage(WinAppBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    _edit_button = (WIN_APP_BY, '20251')
    _setup_button = (WIN_APP_BY, '20455')

    def click_edit_button(self):
        self.click_on_element(self._edit_button)

    def click_setup_button(self):
        self.click_on_element(self._setup_button)
