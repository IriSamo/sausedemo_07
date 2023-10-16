import time
from pages.start_page import StartPage
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from locators.checkout_your_info_page_locators import CheckoutYourInfoPageLocators


class TestLoginPage:

    def test_login_with_standard_user(self, open_start_page):
        catalog_page = (open_start_page
                        .login_with_standard_user())
        assert catalog_page.get_current_url() == 'https://www.saucedemo.com/inventory.html'
        assert catalog_page.get_title() == 'Swag Labs'

    def test_login_negative_path(self, open_start_page):
        start_page = (open_start_page
                      .login_negative_path())
        assert (start_page.get_current_url() == 'https://www.saucedemo.com/')
        assert (start_page.get_login_error() ==
                'Epic sadface: Username and password do not match any user in this service')


class TestCartPage:

    def test_cart_is_empty(self, open_start_page):
        cart_list = (open_start_page
                     .login_with_standard_user()
                     .go_to_cart_page()
                     .get_items_list())
        assert len(cart_list) == 0

    def test_add_to_cart_item(self, open_start_page):
        cart_list = (open_start_page
                     .login_with_standard_user()
                     .add_to_cart_backpack()
                     .go_to_cart_page()
                     .get_items_list())
        assert len(cart_list) == 1
        assert cart_list.count('Sauce Labs Backpack') == 1

    def test_add_to_cart_items(self, open_start_page):
        cart_list = (open_start_page
                     .login_with_standard_user()
                     .add_to_cart_backpack()
                     .add_to_cart_bike_light()
                     .go_to_cart_page()
                     .get_items_list())
        print()
        print('-------------------------', *cart_list)
        assert len(cart_list) == 2
        assert cart_list.count('Sauce Labs Backpack') == 1
        assert cart_list.count('Sauce Labs Bike Light') == 1

    def test_remove_to_cart_item(self, open_start_page):
        cart_list = (open_start_page
                     .login_with_standard_user()
                     .add_to_cart_backpack()
                     .go_to_cart_page()
                     .remove_to_cart_backpack()
                     .get_items_list())
        assert len(cart_list) == 0

    def test_checkout_your_info(self, open_start_page):
        checkout_your_info_page = (open_start_page
                                  .login_with_standard_user()
                                  .add_to_cart_backpack()
                                  .go_to_cart_page()
                                  .click_checkout_button())


        assert checkout_your_info_page.get_current_url() == 'https://www.saucedemo.com/checkout-step-one.html'
        assert checkout_your_info_page.get_title() == 'Swag Labs'
        assert checkout_your_info_page.get_header_secondary_container() == 'Checkout: Your Information'

    def test_checkout_overview(self, open_start_page):
        checkout_overview_page = (open_start_page
                                  .login_with_standard_user()
                                  .add_to_cart_backpack()
                                  .go_to_cart_page()
                                  .click_checkout_button()
                                  .set_your_info()
                                  .click_continue_button())

        assert checkout_overview_page.get_current_url() == 'https://www.saucedemo.com/checkout-step-two.html'
        assert checkout_overview_page.get_title() == 'Swag Labs'
        assert checkout_overview_page.get_header_secondary_container() == 'Checkout: Overview'
