from pages.base_page import BasePage
from locators.start_page_locators import StartPageLocators as locators
from pages.catalog_page import CatalogPage


class StartPage(BasePage):

    def login_with_standard_user(self):
        self.element_is_visible(locators.USERNAME_FIELD).send_keys('standard_user')
        self.element_is_visible(locators.PASSWORD_FIELD).send_keys('secret_sauce')
        self.element_is_visible(locators.LOGIN_BUTTON).click()
        return CatalogPage(self.driver)

    def login_negative_path(self):
        self.element_is_visible(locators.USERNAME_FIELD).send_keys('user')
        self.element_is_visible(locators.PASSWORD_FIELD).send_keys('user')
        self.element_is_visible(locators.LOGIN_BUTTON).click()
        return StartPage(self.driver)

    def get_login_error(self):
        return self.element_is_present(locators.LOGIN_ERROR).text
