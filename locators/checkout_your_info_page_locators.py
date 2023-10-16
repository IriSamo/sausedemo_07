from selenium.webdriver.common.by import By

class CheckoutYourInfoPageLocators:
    HEADER_SECONDARY_CONTAINER = (By.CLASS_NAME, 'title')
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')