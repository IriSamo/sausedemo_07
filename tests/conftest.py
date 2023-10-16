import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.start_page import StartPage

BASE_URL = 'https://www.saucedemo.com/'


@pytest.fixture(scope='function', autouse=True, )
def driver():
    # print('\nopen browser')
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # print('\nquit driver')
    driver.quit()


@pytest.fixture(scope='function')
def open_start_page(driver):
    driver.get(BASE_URL)
    # print('\nopen start page')
    return StartPage(driver)


@pytest.fixture(scope='function')
def login(driver):
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

# @pytest.fixture(scope='function')
# def cart_list(driver):
#     cart_list = []
#     for i in driver.find_elements(By.XPATH, '//div[@class="cart_list"]//a/div'):
#         cart_list.append(i.text)
#
#     yield cart_list
