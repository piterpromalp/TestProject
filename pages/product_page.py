from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_add_to_basket_ok(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()
        self.should_be_correct_result_of_deal()

    def should_be_product_url(self):
        assert self.url.find("catalogue") > 0, "Incorrect url (product page)"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_FORM), "Add to basket button is not presented"
        self.browser.find_element(*ProductPageLocators.ADD_FORM).click()

    def should_be_correct_result_of_deal(self):
        Prod_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        Pre_buy_title = self.browser.find_element(*ProductPageLocators.PRODUCT_PRE_BUY_TITLE).text
        Prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        Pre_buy_price =self.browser.find_element(*ProductPageLocators.PRODUCT_PRE_BUY_PRICE).text
        assert Prod_title == Pre_buy_title, "Нам подсунули другой товар, чёртовы цыгане"
        assert Prod_price == Pre_buy_price, "Цена не совпадает Изя, совсем никак"
        print (f"{Pre_buy_title}, {Pre_buy_price}")

    def test_guest_cant_see_success_message(self):
        self.browser.find_element(*ProductPageLocators.ADD_FORM).click()
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_PRE_BUY_PRICE), \
        "Success message is not presented, but should not be"

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_PRE_BUY_PRICE), \
        "Success message is not presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_FORM).click()
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_PRE_BUY_PRICE), \
        "Success message is not presented, but should not be"

