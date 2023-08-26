from selenium.webdriver.common.by import By


class MainPageLocators:
    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]')
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]')
    order_bt_upper = (By.XPATH, '//div[contains(@class, "Header")]//button[text()="Заказать"]')
    order_bt_lower = (By.XPATH, '//div[contains(@class, "FinishButton")]//button[text()="Заказать"]')


def question_locator(id):
    question = (By.ID, f"accordion__heading-{id}")
    return question


def answer_locator(id):
    answer = (By.XPATH, f"//*[@id='accordion__panel-{id}']/p")
    return answer

