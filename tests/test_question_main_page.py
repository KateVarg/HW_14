from pages.main_page import open_browser, QuestionMainPage
import allure
from data.user import User


@allure.story('Заполнение и отправка формы для отправки вопроса')
def test_fill_form_question():
    question = QuestionMainPage()
    user = User(
        'Катя Варганова',
        'test@test.com',
        '812345678990',
        'Очень важный вопрос про собачек.'
    )
    open_browser()
    question.fill_name(user).fill_mail(user).fill_phone(user).fill_question(user).send_form_question()


@allure.story('Отправка пустой формы')
def test_send_empty_form_question():
    question = QuestionMainPage()

    open_browser()
    question.send_form_question().show_error()
