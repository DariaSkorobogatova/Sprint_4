import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.yandex_page_locators import YaPageLocators
from random import randint


class OrderPage(BasePage):
    @allure.step('Ввести имя в поле "Имя"')
    def enter_name(self, name):
        self.input_data(OrderPageLocators.name, name)

    @allure.step('Ввести фамилию в поле "Фамилия"')
    def enter_surname(self, surname):
        self.input_data(OrderPageLocators.surname, surname)

    @allure.step('Ввести адрес в поле "Адрес"')
    def enter_address(self, address):
        self.input_data(OrderPageLocators.address, address)

    @allure.step('Заполнить поле "Станция метро"')
    def choose_metro_station(self, metro_st):
        self.input_data(OrderPageLocators.metro_station, metro_st)
        self.click_element(OrderPageLocators.choose_metro_station)

    @allure.step('Ввести номер телефона в поле "Телефон"')
    def enter_phone_number(self, phone_number):
        self.input_data(OrderPageLocators.phone_number, phone_number)

    @allure.step('Заполнить данные на первой странице заказа')
    def fill_data_on_first_order_page(self, name, surname, address, metro_st, phone_num):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.choose_metro_station(metro_st)
        self.enter_phone_number(phone_num)
        self.click_element(OrderPageLocators.next_bt)

    @allure.step('Выбрать дату в календаре в поле "Когда привезти самокат"')
    def enter_order_date(self):
        self.click_element(OrderPageLocators.when_bring_scooter_date)
        self.click_element(OrderPageLocators.choose_when_bring_scooter_date)

    @allure.step('Выбрать срок аренды в поле "Срок аренды"')
    def choose_rent_duration(self):
        self.click_element(OrderPageLocators.rent_duration)
        choosen = randint(0, 6)
        self.click_element(OrderPageLocators.rent_duration_options[choosen])

    @allure.step('Выбрать цвет самоката в поле "Цвет самоката"')
    def choose_scooter_color(self):
        self.click_element(OrderPageLocators.scooter_color)

    @allure.step('Заполнить поле "Комментарий"')
    def enter_message_for_carrier(self, msg):
        self.input_data(OrderPageLocators.message_for_carrier, msg)

    @allure.step('Заполнить данные на второй странице заказа')
    def fill_data_on_second_order_page(self, message):
        self.enter_order_date()
        self.choose_rent_duration()
        self.choose_scooter_color()
        self.enter_message_for_carrier(message)
        self.click_element(OrderPageLocators.order_bt)

    @allure.step('Кликнуть по  кнопке "Да"')
    def click_yes_button(self):
        self.click_element(OrderPageLocators.yes_bt)

    @allure.step('Кликнуть по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.scooter_logo)

    @allure.step('Кликнуть по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.yandex_logo)

    @allure.step('Переход на страницу Яндекса')
    def check_yandex_search_bt(self):
        self.switch_to_second_tab()
        return self.element_is_enabled(YaPageLocators.search_bt)