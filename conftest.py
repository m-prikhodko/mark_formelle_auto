import pytest
from enums.browser import BROWSERS
from utils.browser_setup import BrowserSetup


@pytest.fixture(params=BROWSERS)
def browser(request):
    playwright, browser, context, page = BrowserSetup.setup(browser_type=request.param)
    yield page
    BrowserSetup.teardown(context, browser, playwright)

# @pytest.fixture
# def simple():
#     return "simple value"

