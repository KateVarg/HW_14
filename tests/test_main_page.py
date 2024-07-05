from guru_qahacking_tests.pages.main_page import MainPage
import allure


@allure.story('Переход на страницу "Подробнее ..."')
def test_open_details():
    main_page = MainPage()
    main_page.open_browser().check_open_details()

    assert main_page.check_open_details


@allure.story('Переход на страницу "Магазин"')
def test_open_shop():
    main_page = MainPage()
    main_page.open_browser().check_open_shop()

    assert main_page.check_open_shop
