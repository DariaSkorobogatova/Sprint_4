from selenium.webdriver.common.by import By


class OrderSecondPageLocators:
    when_bring_scooter_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rent_duration = [By.CSS_SELECTOR, ".Dropdown-arrow"]
    choose_rent_duration = [By.CSS_SELECTOR, ".Dropdown-menu :nth-child(7)"]
    scooter_colour = [By.ID, "black"]
    message_for_carrier = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    second_page_order_bt = [By.CSS_SELECTOR, "div.Order_Buttons__1xGrp :nth-child(2)"]