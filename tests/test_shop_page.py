from guru_qahacking_tests.pages.shop_page import shop_page
import allure


@allure.story('Проверка перехода на страницу "Подробнее о товаре"')
def test_open_page_item_details():
    shop_page.open_page().open_item_details().check_open_item_details()
