from pages.base_page import BasePage
from locators.checkout_overview_page_locators import CheckoutOverviewPageLocators as locators

class CheckoutOverviewPage(BasePage):

    def get_header_secondary_container(self):
        return self.element_is_present(locators.HEADER_SECONDARY_CONTAINER).text
