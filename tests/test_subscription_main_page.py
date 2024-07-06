from guru_qahacking_tests.pages.main_page import main_page, subscription
import allure
from guru_qahacking_tests.data.emails import Email


@allure.story('Оформление подписки с корректным email')
def test_right_subscription():
    email = Email(
        'test@test.com'
    )
    main_page.open_browser()
    subscription.fill_email(email).send_email().success_email()


@allure.story('Оформление подписки с некорректным email')
def test_wrong_subscription():
    email = Email(
        'testtest.com'
    )
    main_page.open_browser()
    subscription.fill_email(email).send_email().error_email()
