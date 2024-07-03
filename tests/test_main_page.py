from pages.main_page import open_browser, check_open_details, check_open_shop
import allure


@allure.story('Переход на страницу "Подробнее ..."')
def test_open_details():
    open_browser()
    check_open_details()


@allure.story('Переход на страницу "Магазин"')
def test_open_shop():
    open_browser()
    check_open_shop()
