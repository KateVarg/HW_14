from guru_qahacking_tests.pages.shop_page import shop_page
import allure


@allure.story('Переход на страницу "Подробнее о товаре"')
def test_open_page_item_details():
    shop_page.open_page().check_open_item_details()
