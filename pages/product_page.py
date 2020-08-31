from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        """ добавление элемента в корзину"""
        self.should_be_add_to_basket_btn()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not displayed"

    def should_be_add_to_basket_message(self):
        """проверка, что есть сообщение про добавление товара в корзину: has been added to your basket."""
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_TO_BASKET
        ), "No alert that a product has been added to cart"

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
        """сравниваем название товара в карточке с названием с корзины"""
        assert self.return_name_product() == self.return_basket_name_item(), f'Товар {self.return_name_product()} не ' \
                                                                             f'в корзине '

    def should_be_add_to_basket_price(self):
        """сравниваем цену товара карточки с ценой товара в корзине"""
        assert self.return_price_product() == self.return_basket_price(), f'Цена {self.return_price_product()} не в ' \
                                                                          f'корзине. '

    def should_not_be_success_message(self):
        """Проверка на отсутствие появления SUCCESS_MESSAGE"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message should be disappeared, but still present"
