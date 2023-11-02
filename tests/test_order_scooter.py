import allure
import pytest
from data import Data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


@allure.feature('Заказ самоката')
class TestOrderScooter:
    @allure.title('Проверка перехода на страницу заказа по кнопке "Заказать" в хедере')
    @allure.description('В хедере главной страницы кликнуть на кнопку "Заказать", проверить переход на страницу заказа')
    def test_header_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_page(Data.url_main)
        main_page.click_order_button_in_header()
        opened_page = order_page.get_current_url()
        assert opened_page == Data.url_order, f'Вместо {Data.url_order} отображается {opened_page}'

    @allure.title('Проверка перехода на страницу заказа по кнопке "Заказать" в блоке "Как это работает?"')
    @allure.description('В блоке "Как это работает?" главной страницы кликнуть на кнопку "Заказать", проверить '
                        'переход на страницу заказа')
    def test_middle_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_page(Data.url_main)
        main_page.click_order_button_in_middle()
        opened_page = order_page.get_current_url()
        assert opened_page == Data.url_order, f'Вместо {Data.url_order} отображается {opened_page}'

    @allure.title('Проверка оформления заказа самоката')
    @allure.description('На странице заказа заполнить форму и проверить, что появился попап с кнопкой "Посмотреть статус"')
    @pytest.mark.parametrize('name, surname, address, metro, phone, message', Data.data_for_order_test)
    def test_order_scooter(self, driver, name, surname, address, metro, phone, message):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_page(Data.url_order)
        order_page.fill_data_on_first_order_page(name, surname, address, metro, phone)
        order_page.fill_data_on_second_order_page(message)
        order_page.click_yes_button()
        assert order_page.element_is_enabled(OrderPageLocators.see_status_bt), 'Кнопка "Посмотреть статус" не найдена'



