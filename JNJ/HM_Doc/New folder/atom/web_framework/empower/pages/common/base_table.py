import abc
from typing import Callable

from selenium.webdriver import ActionChains

from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient
from web_framework.empower.pages.miltest.miltest_rest_models import Rectangle
from web_framework.empower.pages.miltest.miltest_web_page import MiltestWebPage

SAMPLE_SET_METHOD_NAME_HEADER_HEIGHT = 20


class BaseTable(MiltestWebPage, metaclass=abc.ABCMeta):

    def __init__(self, driver, miltest_rest_client_creator: Callable[[str], MiltestRestClient]):
        super().__init__(driver, miltest_rest_client_creator)

    @abc.abstractmethod
    def _get_miltest_handler(self):
        raise NotImplementedError("Must implement this method")

    @abc.abstractmethod
    def _get_table_element(self):
        raise NotImplementedError("Must implement this method")

    def verify_cell_text(self, row: int, col: int, expected_text: str):
        actual_text = self.get_cell_text(row, col)
        assert actual_text == expected_text, f"Cell [{row};{col}] has unexpected text expected: [{expected_text}], actual: [{actual_text}]"

    def set_cell_text(self, row: int, col: int, cell_text: str):
        self.miltest_rest.set_cell_text(row, col, cell_text)
        self.verify_cell_text(row, col, cell_text)
        return cell_text

    def get_cell_text(self, row: int, col: int):
        response = self.miltest_rest.get_cell_text(row, col)
        return response.text

    def get_cell_coordinates(self, row: int, col: int) -> Rectangle:
        response = self.miltest_rest.get_cell_rectangle(row, col)
        return response.rectangle

    def left_click_cell_by_column_name(self, row, column: str):
        column_number = self._get_column_num_by_name(column)
        self.make_column_visible_on_screen(column_number)
        self.left_click_cell(row, column_number)
        return column_number

    def left_click_cell(self, row: int, col: int):
        cell_rect = self.get_cell_coordinates(row, col)
        x = cell_rect.left + (cell_rect.right - cell_rect.left) // 2
        y = cell_rect.top + (cell_rect.bottom - cell_rect.top) // 2 + SAMPLE_SET_METHOD_NAME_HEADER_HEIGHT
        ActionChains(self._driver).move_to_element_with_offset(self._get_table_element(), x, y).click().perform()

    def right_click_cell(self, row, column_name: str):
        column_number = self._get_column_num_by_name(column_name)
        cell_rect = self.get_cell_coordinates(row, column_number)
        x = cell_rect.left + (cell_rect.right - cell_rect.left) // 2
        y = cell_rect.top + (cell_rect.bottom - cell_rect.top) // 2
        ActionChains(self._driver).move_to_element_with_offset(self._get_table_element(), x, y).context_click().perform()

    def _get_column_num_by_name(self, column: str) -> int:
        response = self.miltest_rest.get_column_index(column)
        return response.columnIndex

    def make_column_visible_on_screen(self, column_id):
        self.miltest_rest.select_and_show_column(column_id)
        self.miltest_rest.deselect_column(column_id)
