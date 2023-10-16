from selenium.webdriver.common.by import By


def test_login_positive_path():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    assert driver.title == 'Swag Labs'
    driver.quit()


def test_login_negative_path(driver):
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('user')
    driver.find_element(By.ID, 'password').send_keys('user')
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/'
    assert (driver.find_element(By.TAG_NAME,
                                'h3').text == 'Epic sadface: Username and password do not match any user in this service')
