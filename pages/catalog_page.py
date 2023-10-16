from pages.base_page import BasePage
from pages.cart_page import CartPage
from locators.catalog_page_locators import CatalogPageLocators as locators


class CatalogPage(BasePage):

    def add_to_cart_backpack(self):
        self.element_is_visible(locators.BACKPACK).click()
        return CatalogPage(self.driver)

    def add_to_cart_bike_light(self):
        self.element_is_visible(locators.BIKE_LIGHT).click()
        return CatalogPage(self.driver)

    def go_to_cart_page(self):
        self.element_is_present(locators.CART_LINK).click()
        return CartPage(self.driver)
