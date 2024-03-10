import time
from playwright.sync_api import sync_playwright

from conftest import browser
from enums.urls import BASE_URL
from pages.page_elements.header_element import Header
from pages.page_elements.listing_element import Listing
from pages.search_page import SearchPage


def test_search(browser):
    header = Header(browser)
    listing = Listing(browser)
    # search_page = SearchPage(browser)
    header.navigate(BASE_URL)
    header.send_search_request("платье")
    listing.assert_presence_of_item()
    # search_page.assert_search_request_is_in_field("платье")

# class TestSearch:
#     def test_search(self, simple):
#         playwright = sync_playwright().start()
#         browser = getattr(playwright, "chromium").launch(headless=False)
#         context = browser.new_context()
#         context.tracing.start(screenshots=True, snapshots=True, sources=True)
#         page = context.new_page()
#         page.set_viewport_size({"width": 1500, "height": 800})
#         search_browser = Header(page)
#         listing_browser = Listing(page)
#         search_browser.navigate(BASE_URL)
#         search_browser.send_search_request("платье")
#         listing_browser.assert_presence_of_item()

# class Test:
# def test_test():
#     playwright = sync_playwright().start()
#     br = getattr(playwright, "chromium").launch(headless=False)
#     context = br.new_context()
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#     page.set_viewport_size({"width": 1500, "height": 900})
#     context.tracing.stop(path='trace.zip')
#     time.sleep(5)
#     br.close()
#     playwright.stop()


