import pytest
import allure

from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import *

class TestOrder:

    #  Весь флоу позитивного сценария с двумя наборами данных через параметризацию.
    @allure.title('Позитивный сценарий заказа самоката')
    @allure.description('Заполняем все обязательные поля во вкладке "Для кого самокат", нажимаем "Далее", заполняем все обязательные поля во вкладке "Про аренду", нажимаем "Заказать", подтверждаем заказ. Проверяем, что появилось сообщение "Заказ оформлен".')
    @pytest.mark.parametrize('button, test_data', [(MainPageLocators.ORDER_BUTTON_IN_HEADER, TestData.test_user_1),
                                                   (MainPageLocators.ORDER_BUTTON_IN_MAIN, TestData.test_user_2)])

    def test_order_scooter(self, driver, button, test_data):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_cookie_button()
        order_page.scroll_to_element(button)
        order_page.wait_for_clickable(button)
        order_page.click_element(button)
        order_page.create_order(test_data)

        assert order_page.check_success_message()