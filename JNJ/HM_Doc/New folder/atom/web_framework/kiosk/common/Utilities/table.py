from typing import Dict, List, Optional, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.kiosk.common.Utilities.element import wait_for_element_visibility, wait_for_element_invisibility

NESTED_ROW_LOCATOR = (By.XPATH, ".//ul[contains(@class, 'table-row')]")
NESTED_CELL_LOCATOR = (By.XPATH, ".//li[contains(@class, 'table-column')]")


def wait_table_loaded(driver: WebDriver, locator: Tuple[By, str], timeout=10):
    wait_for_element_visibility(driver, (By.XPATH, "//ics-spinner"), timeout=2, proceed_on_absence=True)
    wait_for_element_invisibility(driver, (By.XPATH, "//ics-spinner"))
    table = wait_for_element_visibility(driver, locator=locator, timeout=timeout)
    return table


def get_table_data(driver: WebDriver, table_locator=(By.XPATH, "//ics-table"), table_load_timeout=10, **kwargs) -> Optional[List[Dict[str, str]]]:
    nested_row_locator = kwargs.get("nested_row_locator", NESTED_ROW_LOCATOR)
    nested_cell_locator = kwargs.get("nested_cell_locator", NESTED_CELL_LOCATOR)
    table_element = wait_table_loaded(driver, locator=table_locator, timeout=table_load_timeout)

    rows = []
    for row in table_element.find_elements(*nested_row_locator):
        calls_text = [str(cell.text).strip() for cell in row.find_elements(*nested_cell_locator)]
        rows.append(calls_text)

    if not rows:
        return None

    result = []
    headers = rows[0]
    for row in rows[1:]:
        if len(headers) != len(row):
            raise ValueError(f"Unexpected len of row values. Headers: [{headers}], row: [{row}]")
        result.append(dict(zip(headers, row)))

    return result
