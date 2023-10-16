import time
from pages.base_page import BasePage
from pages.catalog_page import *
from pages.checkout_your_info_page import CheckoutYourInfoPage
from locators.cart_page_locators import CartPageLocators as locators


class CartPage(BasePage):

    def get_items_list(self):
        items_list = []
        try:
            for i in self.elements_are_presents(locators.ITEMS_LIST):
                items_list.append(i.text)
        except Exception:
            items_list = []
        return items_list


    def go_to_cart_page(self):
        self.element_is_visible(locators.CART_BUTTON).click()
        time.sleep(2)
        return CartPage(self.driver)


    def remove_to_cart_backpack(self):
        self.element_is_visible(locators.BACKPACK_REMOVE_BUTTON).click()
        return CartPage(self.driver)

    def click_checkout_button(self):
        self.element_is_visible(locators.CHECKOUT_BUTTON).click()
        time.sleep(2)
        return CheckoutYourInfoPage(self.driver)
