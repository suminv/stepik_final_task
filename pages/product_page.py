from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not displayed"

    # def return_to_basket_message(self):
    #     """поиск сообщения, что товар добавлен в корзину """
    #     return self.browser.find_element(*ProductPageLocators.MESSAGE).text

    def return_basket_name_item(self):
        """поиск имени добавленного товара в корзину"""
        return self.browser.find_element(*BasketPageLocators.MESSAGE_NAME_ITEM_IN_BASKET).text

    def return_basket_price(self):
        """поиск цены товара из корзины для сравнения с ценой товара"""
        return self.browser.find_element(*BasketPageLocators.MESSAGE_PRICE_ITEM_IN_BASKET).text

    def return_name_product(self):
        """ находим имя книги для последующего стравнения с именем в корзине"""
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    def return_price_product(self):
        """находим цену книги для послежующего сравнения с ценой в корзине"""
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text

    def should_be_add_to_basket_name(self):
        """сравниваем название товара с корзины  с карточкой товара"""
        # self.return_name_product()
        # self.return_basket_name_item()
        assert self.return_name_product() == self.return_basket_name_item(), f'Товар {self.return_name_product()} не ' \
                                                                             f'в корзине '

    def should_be_add_to_basket_price(self):
        """сравниваем цену товара с корзины  с ценой с карточки"""
        # self.return_basket_price()
        # self.return_price_product()
        assert self.return_price_product() == self.return_basket_price(), f'Цена {self.return_price_product()} не в ' \
                                                                          f'корзине. '
