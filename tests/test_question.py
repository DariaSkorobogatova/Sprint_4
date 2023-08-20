import time

import allure

from data import Data as data
import pytest
from pages.main_page import MainPage
from pages.cookie_page import CookiePage


class TestQuestions:
    @allure.title('Проверка текстов ответов в блоке Вопросы о важном')
    @allure.description('В блоке Вопросы о важном на главной странице кликнуть на каждый вопрос и проверить ответ')
    @pytest.mark.parametrize('id, text', data.data_for_question_tests)
    def test_questions(self, id, text, driver):
        main_page = MainPage(driver)
        cookie_page = CookiePage(driver)
        main_page.go_to_main_page(data.url)
        cookie_page.click_agree_cookie()
        main_page.wait_for_question_block_to_load()
        main_page.scroll_to_question_block(id)
        main_page.click_question(id)
        assert main_page.return_answer_text(id) == text

