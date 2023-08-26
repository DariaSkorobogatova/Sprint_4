import allure
from locators.main_page_locators import MainPageLocators, question_locator, answer_locator
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть по вопросу, дождаться появления ответа')
    def click_question_get_answer(self, id):
        self.wait_for_loading(question_locator(id))
        self.scroll_to_element(question_locator(id))
        self.click_element(question_locator(id))
        self.wait_for_loading(answer_locator(id))

    @allure.step('Получить текст ответа')
    def get_answer_text(self, id):
        return self.get_element_text(answer_locator(id))

    @allure.step('Кликнуть кнопку "Заказать" в хедере страницы')
    def click_order_button_in_header(self):
        self.click_element(MainPageLocators.order_bt_upper)

    @allure.step('Кликнуть кнопку "Заказать" в блоке "Как это работает?"')
    def click_order_button_in_middle(self):
        self.scroll_to_element(MainPageLocators.order_bt_lower)
        self.click_element(MainPageLocators.order_bt_lower)
