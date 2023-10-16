from selenium.webdriver.common.by import By

class StartPageLocators:

    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    LOGIN_ERROR = (By.TAG_NAME, 'h3')