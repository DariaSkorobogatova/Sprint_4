import allure
import pytest
from data import Data
from pages.main_page import MainPage


@allure.feature('Блок "Вопросы о важном"')
class TestQuestions:
    @allure.title('Проверка текстов ответов в блоке "Вопросы о важном"')
    @allure.description('В блоке "Вопросы о важном" на главной странице кликнуть на каждый вопрос и проверить ответ.'
                        'Использованы динамические локаторы')
    @pytest.mark.parametrize('id, text', Data.data_for_question_tests)
    def test_questions(self, id, text, driver):
        main_page = MainPage(driver)
        main_page.go_to_page(Data.url_main)
        main_page.click_question_get_answer(id)
        received_answer_text = main_page.get_answer_text(id)
        assert received_answer_text == text, \
            f'''Ожидаемый ответ - {text}.
            Полученый ответ - {received_answer_text}'''



