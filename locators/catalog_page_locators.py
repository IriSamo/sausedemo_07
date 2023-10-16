from selenium.webdriver.common.by import By

class CatalogPageLocators:

    BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BIKE_LIGHT = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    CART_LIST = (By.XPATH, '//div[@class="cart_list"]//a/div')
