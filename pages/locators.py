from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN = (By.CSS_SELECTOR, '#login_form')
    REGISTER = (By.CSS_SELECTOR, '#register_form')
