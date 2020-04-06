from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import BasketPageLocators





class BasketPage(BasePage):
    def should_be_basket_empty(self):
            is_empty = False
            try:
                empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
                is_empty = empty_basket_text == "Your basket is empty. Continue shopping"
            except NoSuchElementException:
                pass
            assert is_empty, "No basket empty text"
            assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "The basket form shouldn't be here"