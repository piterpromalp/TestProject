from .pages.product_page import ProductPage
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_ok()

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()

class TestUserAddToCartFromProductPage(object):

        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            email = str(time.time()) + "@gipsymail.com"
            password = 'doggywithbrilliant'
            link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
            page = LoginPage(browser, link)
            page.open()
            page.register_new_user(email, password)
            page.should_be_authorized_user()

        @pytest.mark.need_review
        def test_user_can_add_product_to_basket(self, browser):
            link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
            page = ProductPage(browser, link)
            page.open()
            page.should_be_add_to_basket_ok()

        @pytest.mark.xfail
        def test_user_cant_see_success_message(self, browser):
            link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
            page = ProductPage(browser, link)
            page.open()
            page.test_guest_cant_see_success_message()