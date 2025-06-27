from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class FileType(Enum):
    pdf = "pdf"


@dataclass
class FileSavePageLocators:
    file_path: Tuple[str, str]
    file_path_dropdown: Tuple[str, str]
    save_button: Tuple[str, str]
    cancel_button: Tuple[str, str]


class FileSavePage(WinAppBasePage):

    def __init__(self, driver, file_page_locator: FileSavePageLocators):
        super().__init__(driver)
        self._file_page_locator: FileSavePageLocators = file_page_locator
        # self._logger = logging.getLogger(self.__class__.__name__)

    def set_file_path(self, file_path, file_type: FileType = None):
        self.wait_for_element_visibility(self._file_page_locator.file_path, 10)
        self.clear_and_set_text(self._file_page_locator.file_path, file_path)

    def click_save(self):
        self.click_on_element(self._file_page_locator.save_button)

    def click_cancel(self):
        self.click_on_element(self._file_page_locator.cancel_button)
