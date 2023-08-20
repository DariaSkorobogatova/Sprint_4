from selenium.webdriver.common.by import By


class OrderFirstPageLocators:
    name = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    phone_number = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    metro_station = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    choose_metro_station = [By.CSS_SELECTOR, ".select-search__select :first-child"]
    next_bt = [By.XPATH, ".//button[text()='Далее']"]
