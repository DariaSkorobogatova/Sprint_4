from selenium.webdriver.common.by import By
import datetime
from random import choice


class OrderPageLocators:
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    surname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    phone_number = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    metro_station = (By.XPATH, "//input[@placeholder='* Станция метро']")
    choose_metro_station = (By.CSS_SELECTOR, ".select-search__select :first-child")
    next_bt = (By.XPATH, ".//button[text()='Далее']")
    when_bring_scooter_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    day = datetime.date.today().day
    choose_when_bring_scooter_date = (By.XPATH, f'//*[@class="react-datepicker"]//*[text()="{day}"]')
    rent_duration = (By.XPATH, '//div[contains(text(),"* Срок аренды")]')
    rent_duration_options = (
        (By.XPATH, '//div[contains(text(),"сутки")]'),
        (By.XPATH, '//div[contains(text(),"двое суток")]'),
        (By.XPATH, '//div[contains(text(),"трое суток")]'),
        (By.XPATH, '//div[contains(text(),"четверо суток")]'),
        (By.XPATH, '//div[contains(text(),"пятеро суток")]'),
        (By.XPATH, '//div[contains(text(),"шестеро суток")]'),
        (By.XPATH, '//div[contains(text(),"семеро суток")]')
    )
    color = choice(['black', 'grey'])
    scooter_color = (By.XPATH, f'//div[contains(@class, "Order_Checkboxes")]//input[@id="{color}"]')
    message_for_carrier = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_bt = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp :nth-child(2)")
    see_status_bt = (By.XPATH, ".//button[text()='Посмотреть статус']")
    yes_bt = (By.XPATH, ".//button[text()='Да']")
