from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ открываем нужную страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """будем перехватывать исключение.
        how - как искать (css, id, xpath и тд)
        what - что искать (строку-селектор). """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:  # имя исключения
            return False
        return True
