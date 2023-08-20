from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_second_page_locators import OrderSecondPageLocators as l
from selenium.webdriver.common.by import By


class OrderSecondPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_date_duration_colour_msg(self, date, msg):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tuple(l.when_bring_scooter_date)))
        self.driver.find_element(*l.when_bring_scooter_date).send_keys(date)
        self.driver.find_element(*l.rent_duration).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tuple(l.choose_rent_duration)))
        self.driver.find_element(*l.choose_rent_duration).click()
        self.driver.find_element(*l.scooter_colour).click()
        self.driver.find_element(*l.message_for_carrier).send_keys(msg)

    def click_order_bt(self):
        self.driver.find_element(*l.second_page_order_bt).click()

