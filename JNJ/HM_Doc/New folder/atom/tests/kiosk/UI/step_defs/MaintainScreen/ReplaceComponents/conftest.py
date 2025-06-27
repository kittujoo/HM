import pytest

from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen


@pytest.fixture
def maintain_screen(page_builder):
    page = page_builder(MaintainScreen)
    return page
