from guru_qahacking_tests.pages.main_page import main_page, question
import allure
from guru_qahacking_tests.data.user import User
import pytest


@pytest.mark.xfail
@allure.story('Проверка успешной отправки формы с вопросом')
def test_fill_form_question():
    user = User(
        'Катя Варганова',
        'test@test.com',
        '812345678990',
        'Очень важный вопрос про собачек.'
    )
    main_page.open_browser()
    question.fill_name(user).fill_mail(user).fill_phone(user).fill_question(user).send_form_question().success_form_question()


@allure.story('Отправка пустой формы')
def test_send_empty_form_question():

    main_page.open_browser()
    question.send_form_question().show_error()
