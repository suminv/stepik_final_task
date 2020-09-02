from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_content_of_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT_OF_THE_BASKET), \
            "Content of the basket is not disappeared, but should be"

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Empty message is not disappeared, but should be"

    def should_not_be_content_of_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTENT_OF_THE_BASKET), \
            "Content of the basket is presented, but should not be"

    def should_not_be_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Empty message is presented, but should not be"

