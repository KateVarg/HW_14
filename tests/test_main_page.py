from guru_qahacking_tests.pages.main_page import main_page
import allure


@allure.story('Переход на страницу "Подробнее ..."')
def test_open_details():
    main_page.open_browser().open_details().check_open_details()


@allure.story('Переход на страницу "Магазин"')
def test_open_shop():
    main_page.open_browser().open_shop().check_open_shop()
