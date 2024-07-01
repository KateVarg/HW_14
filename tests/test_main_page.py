from selene import browser, by
import allure


@allure.step('Открытие сайта')
def open(self):
    browser.open('')
    return self


@allure.step('Переход на страницу "Подробнее о питомнике"')
def check_open_details():
    browser.element('.uk-button-primary').click()
    browser.element(by.partial_text('Наши питомцы обладают хорошей и'))

