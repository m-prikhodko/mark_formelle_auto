import allure
from pages.base_page import BasePage
from pages.page_elements.locators.listing_locators import ListingLocators


class Listing(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.listing_locators = ListingLocators()

    def assert_presence_of_item(self):
        with allure.step("Проверка наличия карточки в листинге"):
            self.wait_for_selector(self.listing_locators.CATALOG_ITEM)
