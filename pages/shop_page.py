from selene import browser, by
import allure


@allure.step('Открытие страницы "Магазин"')
def open_page():
    browser.open('/index.php/magazin')


@allure.step('Переход на страницу "Подробнее о товаре"')
def check_open_item_details():
    browser.element('.productitem_2').element('.oiproduct').element('.button_detail').click()
    browser.element(by.partial_text('Перекус для собачки'))
