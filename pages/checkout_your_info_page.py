import time
from pages.base_page import BasePage
from pages.checkout_overview_page import CheckoutOverviewPage
from locators.checkout_your_info_page_locators import CheckoutYourInfoPageLocators as locators
from generator.generator import generated_person

class CheckoutYourInfoPage(BasePage):

    def set_your_info(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        postal_code = person_info.postal_code
        self.element_is_visible(locators.FIRST_NAME_FIELD).send_keys(first_name)
        self.element_is_visible(locators.LAST_NAME_FIELD).send_keys(last_name)
        self.element_is_visible(locators.POSTAL_CODE_FIELD).send_keys(postal_code)
        time.sleep(2)
        return CheckoutYourInfoPage(self.driver)

    def click_continue_button(self):
        self.element_is_visible(locators.CONTINUE_BUTTON).click()
        return CheckoutOverviewPage(self.driver)

    def get_header_secondary_container(self):
        return self.element_is_present(locators.HEADER_SECONDARY_CONTAINER).text