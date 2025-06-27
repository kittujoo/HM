from enum import Enum

from utilities.logger import Logger
from web_framework.empower.pages.miltest.miltest_web_page import MiltestWebPage
from web_framework.web_driver_common.constants import WIN_APP_BY


class ProjectTabsHeaders(Enum):
    SAMPLE_SETS = "Sample Sets"
    INJECTIONS = "Injections"
    CHANNELS = "Channels"
    METHODS = "Methods"
    RESULT_SETS = "Result Sets"
    RESULTS = "Results"
    PEAKS = "Peaks"
    FRACTIONS = "Fractions"
    SIGN_OFFS = "Sign Offs"
    CURVES = "Curves"
    VIEW_FILTERS = "View Filters"
    CUSTOM_FIELDS = "Custom Fields"
    AUDIT_TRAILS = "Audit Trails"


class TabSelectorItem(MiltestWebPage):
    TAB_SELECTOR_LOCATOR = (WIN_APP_BY, "59905")

    def __init__(self, driver, miltest_rest_client_creator):
        super().__init__(driver, miltest_rest_client_creator)
        self._logger = Logger(self.__class__.__name__)

    def _get_miltest_handler(self):
        handle = self.get_element_attribute(self.TAB_SELECTOR_LOCATOR, "NativeWindowHandle")
        return handle

    def select_tab(self, tab: ProjectTabsHeaders):
        self.miltest_rest.select_tab_by_name(tab.value)
