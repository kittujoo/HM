from typing import Callable

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.EnumBase import EnumBase
from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient
from web_framework.empower.pages.miltest.miltest_rest_models import Rectangle
from web_framework.empower.pages.miltest.miltest_web_page import MiltestWebPage

SAMPLE_SET_METHOD_NAME_HEADER_HEIGHT = 20


class MethodFunctions(EnumBase):
    INJECT_STANDARDS = "Inject Standards"
    INJECT_NARROW_STANDARDS = "Inject Narrow Standards"
    INJECT_BROAD_STANDARDS = "Inject Broad Standards"
    INJECT_SAMPLES = "Inject Samples"
    INJECT_NARROW_SAMPLES = "Inject Narrow Samples"
    INJECT_BROAD_SAMPLES = "Inject Broad Samples"
    INJECT_CONTROLS = "Inject Controls"
    INJECT_RF_INTERNAL_STANDARDS = "Inject RF Internal Standards"
    INJECT_IMMEDIATE_STANDARDS = "Inject Immediate Standards"
    INJECT_IMMEDIATE_SAMPLES = "Inject Immediate Samples"
    CLEAR_CALIBRATION = "Clear Calibration"
    EQUILIBRATE = "Equilibrate"
    REPORT = "Report"
    QUANTITATE = "Quantitate"
    CALIBRATE = "Calibrate"
    CONDITION_COLUMN = "Condition Column"
    PURGE_INJ = "Purge Inj"
    WASH_NEEDLE = "Wash Needle"
    WET_PRIME = "Wet Prime"
    SUMMARIZE_CUSTOM_FIELDS = "Summarize Custom Fields"
    PAUSE = "Pause"
    SUMMARIZE_CUSTOM_FIELDS_EXCLUDE_FAULTED = "Summarize Custom Fields (Exclude Faulted)"
    SUMMARIZE_CUSTOM_FIELDS_INCREMENTALLY = "Summarize Custom Fields Incrementally"
    SUMMARIZE_CUSTOM_FIELDS_INCREMENTALLY_EXCLUDE_FAULTED = "Summarize Custom Fields Incrementally (Exclude Faulted)"
    EXPORT = "Export"


class TableColumnNames(EnumBase):
    PLATE_WELL = "Plate/Well"
    INJ_VOL_UL = "Inj Vol\n(uL)"
    NUM_OF_INJECTIONS = "# of Injs"
    LABLE = "Label"
    SIMPLE_NAME = "SampleName"
    LEVEL = "Level"
    SAMPLE_MATRIX = "Sample Matrix"
    FUNCTION = "Function"
    METHOD_SET_OR_EXPORT = "Method Set / Report or Export Method"
    LABEL_REFERENCE = "Label Reference"
    PROCESSING = "Processing"
    RUN_TIME_MINUTES = "Run Time\n(Minutes)"
    DATA_START_MINUTES = "Data Start\n(Minutes)"
    NEXT_INJ_DELAY_MINUTES = "Next Inj. Delay\n(Minutes)"
    BATH = "Bath"
    VESSEL = "Vessel"
    TRANSFER_TIME = "Transfer Time"
    RI_SENSITIVITY = "RI Sensitivity"
    SOLVERN = "Solvent"
    PREP_TYPE = "Prep Type"
    SAMPLE_PREP = "Sample Prep"


# TODO derive from BaseTable
class SamplesTab(MiltestWebPage):

    def __init__(self, driver, miltest_rest_client_creator: Callable[[str], MiltestRestClient]):
        super().__init__(driver, miltest_rest_client_creator)

    def _get_miltest_handler(self):
        element = self._get_table_element().get_attribute("NativeWindowHandle")
        return element

    def _get_table_element(self):
        return self.find_element((By.XPATH, "//Pane[@AutomationId='59648'and @ClassName='TableView']"))

    def select_method_function(self, row: int, function: MethodFunctions):
        # Row count starts from 1
        column = self.left_click_cell_by_column_name(row, TableColumnNames.FUNCTION)
        self.click_on_element((By.XPATH, f"//ListItem[@Name='{function.value}']"))
        self.verify_cell_text(row, column, function.value)

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

    def select_method_set(self, row: int, method_set_name: str):
        column = self.left_click_cell_by_column_name(row, TableColumnNames.METHOD_SET_OR_EXPORT)
        self.click_on_element((By.XPATH, f"//ListItem[@Name='{method_set_name}']"))
        self.verify_cell_text(row, column, method_set_name)

    def get_cell_coordinates(self, row: int, col: int) -> Rectangle:
        response = self.miltest_rest.get_cell_rectangle(row, col)
        return response.rectangle

    def left_click_cell_by_column_name(self, row, column: TableColumnNames):
        column_number = self._get_column_num_by_name(column)
        self.make_column_visible_on_screen(column_number)
        self.left_click_cell(row, column_number)
        return column_number

    def left_click_cell(self, row: int, col: int):
        cell_rect = self.get_cell_coordinates(row, col)
        x = cell_rect.left + (cell_rect.right - cell_rect.left) // 2
        y = cell_rect.top + (cell_rect.bottom - cell_rect.top) // 2 + SAMPLE_SET_METHOD_NAME_HEADER_HEIGHT
        ActionChains(self._driver).move_to_element_with_offset(self._get_table_element(), x, y).click().perform()

    def right_click_cell_by_column_name(self, row, column: TableColumnNames):
        column_number = self._get_column_num_by_name(column)
        self.make_column_visible_on_screen(column_number)
        self.right_click_cell(row, column_number)
        return column_number

    def right_click_cell(self, row, column_name):
        column_number = self._get_column_num_by_name(column_name)
        cell_rect = self.get_cell_coordinates(row, column_number)
        x = cell_rect.left + (cell_rect.right - cell_rect.left) // 2
        y = cell_rect.top + (cell_rect.bottom - cell_rect.top) // 2
        ActionChains(self._driver).move_to_element_with_offset(self._get_table_element(), x, y).context_click().perform()

    def _get_column_num_by_name(self, column: TableColumnNames) -> int:
        response = self.miltest_rest.get_column_index(column.value)
        return response.columnIndex

    def add_new_sample_table_line(self):
        self._get_table_element().click()
        ActionChains(self._driver).send_keys(Keys.ESCAPE).perform()

    def make_column_visible_on_screen(self, column_id):
        self.miltest_rest.select_and_show_column(column_id)
        self.miltest_rest.deselect_column(column_id)

    def set_sample_prep(self, row: int, value: int) -> str:
        column_id = self._get_column_num_by_name(TableColumnNames.SAMPLE_PREP)
        self.make_column_visible_on_screen(column_id)
        return self.set_cell_text(row, column_id, str(value))

    def set_runtime(self, row: int, value: str) -> str:
        column_id = self._get_column_num_by_name(TableColumnNames.RUN_TIME_MINUTES)
        self.make_column_visible_on_screen(column_id)
        return self.set_cell_text(row, column_id, value)
