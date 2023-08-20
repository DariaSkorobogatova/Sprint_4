from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_first_page_locators import OrderFirstPageLocators as l
from selenium.webdriver.common.by import By


class OrderFirstPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name_address_phone_number(self, name, surname, address, phone):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tuple(l.name)))
        self.driver.find_element(*l.name).send_keys(name)
        self.driver.find_element(*l.surname).send_keys(surname)
        self.driver.find_element(*l.address).send_keys(address)
        self.driver.find_element(*l.phone_number).send_keys(phone)

    def choose_metro_station(self, metro_st):
        self.driver.find_element(*l.metro_station).send_keys(metro_st)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(tuple(l.choose_metro_station)))
        self.driver.find_element(*l.choose_metro_station).click()

    def click_next_bt(self):
        self.driver.find_element(*l.next_bt).click()