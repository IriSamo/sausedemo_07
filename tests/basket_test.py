import pytest
from selenium.webdriver.common.by import By


def test_add_to_cart_backpack(driver, login):
    login
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    cart_list = []
    for i in driver.find_elements(By.XPATH, '//div[@class="cart_list"]//a/div'):
        cart_list.append(i.text)
    print()
    print('-------------------------', *cart_list)
    assert cart_list.count('Sauce Labs Backpack') == 1