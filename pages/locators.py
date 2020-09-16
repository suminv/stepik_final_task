from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK_PAGE = (By.CSS_SELECTOR, 'a.btn.btn-default')
    MESSAGE_NAME_ITEM_IN_BASKET = (
        By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in > div> strong')
    MESSAGE_PRICE_ITEM_IN_BASKET = (
        By.CSS_SELECTOR, '.alert-info.fade.in div strong')
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    CONTENT_OF_THE_BASKET = (By.CSS_SELECTOR, ".basket_summary")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form input[type='email']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#register_form input[name='registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#register_form input[name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
