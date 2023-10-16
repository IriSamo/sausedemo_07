from selenium.webdriver.common.by import By

class CartPageLocators:

    ITEMS_LIST = (By.XPATH, '//div[@class="cart_list"]//a/div')
    BACKPACK_REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
    BIKE_LIGHT_REMOVE_BUTTON = (By.XPATH, '//button[@data-test="remove-sauce-labs-bike-light"]')
    CHECKOUT_BUTTON = (By.ID, 'checkout')