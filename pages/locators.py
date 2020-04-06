from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_FORM = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_PRE_BUY_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRE_BUY_TITLE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert .alert-safe .alert-noicon .alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")