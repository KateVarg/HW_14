from selene import browser, have
import allure


class ShopPage:

    @allure.step('Открытие страницы "Магазин"')
    def open_page(self):
        browser.open('/index.php/magazin')
        return self

    @allure.step('Переход на страницу "Подробнее о товаре"')
    def check_open_item_details(self):
        browser.element('.productitem_2').element('.oiproduct').element('.button_detail').click()
        browser.element('#comjshop').should(have.text('Перекус для собачки'))
        return self
