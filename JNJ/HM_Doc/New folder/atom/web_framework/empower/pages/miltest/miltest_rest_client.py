from isym_test_api.rest_api.rest_client.rest import RestClient
from web_framework.empower.pages.miltest.miltest_rest_models import GetCellTextRequest, GetCellTextResponse, SetCellTextRequest, GetCellRectangleRequest, \
    GetCellRectangleResponse, GetColumnIndexRequest, GetColumnIndexResponse, SelectAndShowColumnRequest, SelectColumnRequest, ShowColumnRequest, \
    DeselectColumnRequest, GetTabNumberRequest, GetTabNumberResponse, SelectTabByIndexRequest, SelectTabByTitleRequest, GetTabTestRequest, GetTabTextResponse, \
    GetTabCountResponse, GetCurrentTabResponse


class MiltestRestClient:
    def __init__(self, rest_client: RestClient):
        self._rest_client: RestClient = rest_client

    def get_cell_text(self, row: int, col: int) -> GetCellTextResponse:
        payload = GetCellTextRequest(row=row, column=col)
        response = self._rest_client.post("getCellText", payload=payload, response_type=GetCellTextResponse).data
        return response

    def set_cell_text(self, row: int, col: int, text: str) -> None:
        payload = SetCellTextRequest(row=row, column=col, text=text)
        self._rest_client.post("setCellText", payload=payload).validate_status_code()

    def get_cell_rectangle(self, row: int, col: int) -> GetCellRectangleResponse:
        payload = GetCellRectangleRequest(row=row, column=col)
        response = self._rest_client.post("getCellRectangle", payload=payload, response_type=GetCellRectangleResponse).data
        return response

    def get_column_index(self, column_name: str) -> GetColumnIndexResponse:
        payload = GetColumnIndexRequest(columnName=column_name)
        response = self._rest_client.post("getColumnIndex", payload=payload, response_type=GetColumnIndexResponse).data
        return response

    def select_and_show_column(self, column_index: int) -> None:
        payload = SelectAndShowColumnRequest(columnIndex=column_index)
        self._rest_client.post("selectAndShowColumn", payload=payload).validate_status_code()

    def select_column(self, column_index: int):
        payload = SelectColumnRequest(columnIndex=column_index)
        self._rest_client.post("selectColumn", payload=payload).validate_status_code()

    def shown_column(self, column_index: int):
        payload = ShowColumnRequest(columnIndex=column_index)
        self._rest_client.post("showColumn", payload=payload).validate_status_code()

    def deselect_column(self, column_index) -> None:
        payload = DeselectColumnRequest(columnIndex=column_index)
        self._rest_client.post("deselectColumn", payload=payload).validate_status_code()

    def get_tab_index(self, tab_name: str) -> GetTabNumberResponse:
        payload = GetTabNumberRequest(tabName=tab_name)
        response = self._rest_client.post("getTabNumber", payload=payload, response_type=GetTabNumberResponse).data
        return response

    def select_tab_by_index(self, tab_index: int) -> None:
        payload = SelectTabByIndexRequest(tabIndex=tab_index)
        self._rest_client.post("selectTabByIndex", payload=payload).validate_status_code()

    def select_tab_by_name(self, tab_name) -> None:
        payload = SelectTabByTitleRequest(tabTitle=tab_name)
        self._rest_client.post("selectTabByTitle", payload=payload).validate_status_code()

    def get_tab_title(self, tab_index: int) -> GetTabTextResponse:
        payload = GetTabTestRequest(tabIndex=tab_index)
        response = self._rest_client.post("getTabText", payload=payload, response_type=GetTabTextResponse).data
        return response

    def get_tabs_count(self) -> GetTabCountResponse:
        response = self._rest_client.post("getTabsCount", payload=None, response_type=GetTabCountResponse).data
        return response

    def get_current_tab_index(self) -> GetCurrentTabResponse:
        response = self._rest_client.post("getCurrentTab", payload=None, response_type=GetCurrentTabResponse).data
        return response
