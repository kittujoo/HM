from enum import Enum
from typing import Callable

from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient
from web_framework.empower.pages.miltest.miltest_web_page import MiltestWebPage
from web_framework.empower.pages.run_samples.running_tab import RunningTab
from web_framework.empower.pages.run_samples.sample_sets_tab import SampleSetsTab
from web_framework.empower.pages.run_samples.samples_table import SamplesTab
from web_framework.empower.pages.run_samples.single_injection_tab import SingleInjectionTab
from web_framework.web_driver_common.constants import WIN_APP_BY


class SampleSetTabsEnum(Enum):
    SINGLE = "Single"
    SAMPLES = "Samples"
    SAMPLE_SETS = "Sample Sets"
    RUNNING = "Running"


class RunSamplesTabs(MiltestWebPage):

    def __init__(self, driver: WebDriver, miltest_rest_client_creator: Callable[[str], MiltestRestClient]):
        super().__init__(driver, miltest_rest_client_creator)

    def _get_miltest_handler(self):
        element = self._driver.find_element(WIN_APP_BY, "59905").get_attribute("NativeWindowHandle")
        return element

    @property
    def single_injection_tab(self) -> SingleInjectionTab:
        self._select_tab_by_name(SampleSetTabsEnum.SINGLE)
        page = SingleInjectionTab(self._driver)
        page.validate_opened()
        return page

    @property
    def samples_tab(self) -> SamplesTab:
        self._select_tab_by_name(SampleSetTabsEnum.SAMPLES)
        page = SamplesTab(self._driver, self._miltest_rest_client_creator)
        page.validate_opened()
        return page

    @property
    def sample_sets_tab(self) -> SampleSetsTab:
        self._select_tab_by_name(SampleSetTabsEnum.SAMPLE_SETS)
        page = SampleSetsTab(self._driver)
        page.validate_opened()
        return page

    @property
    def running_tab(self) -> RunningTab:
        self._select_tab_by_name(SampleSetTabsEnum.RUNNING)
        page = RunningTab(self._driver)
        page.validate_opened()
        return page

    def _select_tab_by_name(self, tab_name: SampleSetTabsEnum):
        self.miltest_rest.select_tab_by_name(tab_name.value)
