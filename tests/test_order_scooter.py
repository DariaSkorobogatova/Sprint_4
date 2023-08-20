from data import Data as data
import allure
from pages.main_page import MainPage
from pages.cookie_page import CookiePage
from pages.order_first_page import OrderFirstPage
from pages.order_second_page import OrderSecondPage
from pages.want_to_confirm_order_popup_page import ConfirmOrderPage
from pages.confirmation_order_page import ConfirmationOrderPage
from pages.general_page import GeneralPage
from pages.yandex_page import YaPage


class TestOrderScooter:
    @allure.title('Проверка заказа самоката и перехода по лого')
    @allure.description('На главной странице нажимаем Заказать, заполняет форму, подтверждаем заказ, '
                        'убеждаемся, что подтверждающая заказ форма открылась,'
                        'убеждаемся, что по клику на лого самоката переходим на главную страницу сервиса'
                        'убеждаемся, что по клику на лого яндекса переходим на главную страницу яндекса')
    def test_order_scooter(self, driver):
        main_page = MainPage(driver)
        cookie_page = CookiePage(driver)
        order_page_1 = OrderFirstPage(driver)
        order_page_2 = OrderSecondPage(driver)
        confirm_order = ConfirmOrderPage(driver)
        order_confirmation = ConfirmationOrderPage(driver)
        general_page = GeneralPage(driver)
        yandex_page = YaPage(driver)
        main_page.go_to_main_page(data.url)
        main_page.wait_for_main_page_to_load()
        cookie_page.click_agree_cookie()
        main_page.click_order_bt()
        order_page_1.enter_name_address_phone_number(data.name, data.surname, data.address, data.phone)
        order_page_1.choose_metro_station(data.metro_station)
        order_page_1.click_next_bt()
        order_page_2.enter_date_duration_colour_msg(data.date, data.msg)
        order_page_2.click_order_bt()
        confirm_order.wait_for_popup()
        confirm_order.click_yes_bt()
        assert order_confirmation.order_is_confirmed_popup()
        order_confirmation.see_status_bt()
        general_page.click_scooter_logo()
        main_page.wait_for_main_page_to_load()
        assert main_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'
        general_page.click_yandex_logo()
        general_page.windows_switch()
        yandex_page.wait_for_search_bt()
        assert main_page.get_current_url() == 'https://dzen.ru/?yredirect=true'




