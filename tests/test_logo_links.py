import allure
from data import Data
from pages.order_page import OrderPage


@allure.feature('Логотипы')
class TestLogoLinks:
    @allure.title('Проверка перехода на главную страницу по клику на лого самоката')
    @allure.description('На странице заказа кликнуть на логотип самоката, проверить переход на главную страницу')
    def test_scooter_logo_link(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_page(Data.url_order)
        order_page.click_scooter_logo()
        opened_page = order_page.get_current_url()
        assert opened_page == Data.url_main, f'Вместо {Data.url_main} отображается {opened_page}'

    @allure.title('Проверка перехода на главную страницу Яндекса по клику на лого Яндекса')
    @allure.description('Проверка перехода на главную страницу Яндекса по нажатию на логотип Яндекса '
        'в хэдере страницы оформления заказа в приложении')
    def test_yandex_logo_link(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_page(Data.url_order)
        order_page.click_yandex_logo()
        assert order_page.check_yandex_search_bt(), f'Не осуществлен переход на главную страницу Яндекса'


