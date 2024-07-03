from pages.main_page import open_browser, SubscriptionMainPage
import allure
from data.emails import Email


@allure.story('Оформление подписки с корректным email')
def test_right_subscription():
    subscription = SubscriptionMainPage()
    email = Email(
        'test@test.com'
    )
    open_browser()
    subscription.fill_email(email).send_email()


@allure.story('Оформление подписки с некорректным email')
def test_wrong_subscription():
    subscription = SubscriptionMainPage()
    email = Email(
        'testtest.com'
    )
    open_browser()
    subscription.fill_email(email).send_email()


@allure.story('Оформление подписки без email')
def test_subscription():
    subscription = SubscriptionMainPage()
    email = Email(
        ' '
    )
    open_browser()
    subscription.fill_email(email).send_email()


