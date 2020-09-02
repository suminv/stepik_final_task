import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """перейти на ссылку с логином"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        """переход на страницу корзины"""
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_login_link(self):
        """проверить ссылку на login"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        """ открываем нужную страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """ Проверка на наличие элемента на странице.
        будем перехватывать исключение.
        how - как искать (css, id, xpath и тд)
        what - что искать (строку-селектор). """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:  # имя исключения
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """проверяет, что элемент не появляется на странице в течение заданного времени. упадет, как только увидит
        искомый элемент. Не появился: успех, тест зеленый. """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """проверить, что какой-то элемент исчезает. будет ждать до тех пор, пока элемент не исчезнет """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert presented")
