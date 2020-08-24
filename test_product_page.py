import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    # link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # time.sleep(3)
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_message()
    page.should_be_add_to_basket_name()
    page.should_be_add_to_basket_price()
