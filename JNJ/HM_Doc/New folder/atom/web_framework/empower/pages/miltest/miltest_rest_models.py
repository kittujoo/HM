from dataclasses import dataclass


@dataclass
class GetCellTextRequest:
    row: int
    column: int


@dataclass
class GetCellTextResponse:
    text: str


@dataclass
class SetCellTextRequest:
    row: int
    column: int
    text: str


@dataclass
class GetCellRectangleRequest:
    row: int
    column: int


@dataclass
class Rectangle:
    left: int
    top: int
    right: int
    bottom: int


@dataclass
class GetCellRectangleResponse:
    rectangle: Rectangle


@dataclass
class GetColumnIndexRequest:
    columnName: str


@dataclass
class GetColumnIndexResponse:
    columnIndex: int


@dataclass
class SelectAndShowColumnRequest:
    columnIndex: int


@dataclass
class SelectColumnRequest:
    columnIndex: int


@dataclass
class ShowColumnRequest:
    columnIndex: int


@dataclass
class DeselectColumnRequest:
    columnIndex: int


@dataclass
class GetTabNumberRequest:
    tabName: str


@dataclass
class SelectTabByTitleRequest:
    tabTitle: str


@dataclass
class GetTabNumberRequest:
    tabName: str


@dataclass
class SelectTabByIndexRequest:
    tabIndex: int


@dataclass
class GetTabNumberResponse:
    tabIndex: int


@dataclass
class SelectTabByIndexRequest:
    tabIndex: int


@dataclass
class SelectTabByTitleRequest:
    tabTitle: str


@dataclass
class GetTabTextResponse:
    text: str


@dataclass
class GetTabTestRequest:
    tabIndex: int


@dataclass
class GetTabCountResponse:
    count: int


@dataclass
class GetCurrentTabResponse:
    tabIndex: int
