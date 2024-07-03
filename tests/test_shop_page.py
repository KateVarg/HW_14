from pages.shop_page import open_page, check_open_item_details
import allure


@allure.story('Переход на страницу "Подробнее о товаре"')
def test_open_page_item_details():
    open_page()
    check_open_item_details()
