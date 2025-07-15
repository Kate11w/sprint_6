import allure

from locators.order_page_locators import OrderPageLocators
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class OrderPage(BasePage):

    # Заполнение формы "Для кого самокат"
    @allure.step('Заполнение поля "Имя"')
    def filling_field_of_name(self, test_data):
        self.wait_for_clickable(OrderPageLocators.NAME)
        self.click_element(OrderPageLocators.NAME)
        self.send_keys(OrderPageLocators.NAME, test_data["name"])

    @allure.step('Заполнение поля "Фамилия')
    def filling_field_of_lastname(self, test_data):
        self.click_element(OrderPageLocators.LASTNAME)
        self.send_keys(OrderPageLocators.LASTNAME, test_data["lastname"])

    @allure.step('Заполнение поля адреса доставки')
    def filling_field_of_address(self, test_data):
        self.click_element(OrderPageLocators.ADDRESS)
        self.send_keys(OrderPageLocators.ADDRESS, test_data["address"])

    @allure.step('Выбор станции метро')
    def choose_metro_station(self, test_data):
        self.click_element(OrderPageLocators.METRO)
        self.send_keys(OrderPageLocators.METRO, test_data["metro"])
        self.click_element(OrderPageLocators.METRO_DROPDOWN_OPTION)

    @allure.step('Заполнение номера телефона')
    def filling_field_of_phone(self, test_data):
        self.click_element(OrderPageLocators.PHONE)
        self.send_keys(OrderPageLocators.PHONE, test_data["phone"])

    @allure.step('Клик по кнопке "Далее"')
    def submit_order(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    # Заполнение формы "Про аренду"
    @allure.step('Заполнение даты доставки')
    def filling_field_of_date_delivery(self, test_data):
        self.wait_for_clickable(OrderPageLocators.DATE)
        self.click_element(OrderPageLocators.DATE)
        self.send_keys(OrderPageLocators.DATE, test_data["date"])
        self.click_escape()



    @allure.step('Выбор срока аренды на сутки')
    def choice_of_rental_term(self):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)

    @allure.step('Выбор цвета самоката')
    def choice_of_scooter_color(self):
        self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)

    @allure.step('Ввод комментария для курьера')
    def input_comment(self, test_data):
        self.click_element(OrderPageLocators.COMMENT_INPUT)
        self.send_keys(OrderPageLocators.COMMENT_INPUT, test_data["comment"])

    @allure.step('Клик по кнопке "Заказать"')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Подтверждаем заказ. Кнопка "Да"')
    def confirm_yes_in_popup(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step('Проверка, что появилось сообщение "Заказ оформлен"')
    def check_success_message(self):
        try:
            success_message = self.wait_for_text(OrderPageLocators.SUCCESS_ORDER_MESSAGE)
            return "Заказ оформлен" in success_message
        except TimeoutException:
            return False

    @allure.step('Создание заказа аренды самоката')
    def create_order(self, test_data):
        self.filling_field_of_name(test_data)
        self.filling_field_of_lastname(test_data)
        self.filling_field_of_address(test_data)
        self.choose_metro_station(test_data)
        self.filling_field_of_phone(test_data)
        self.submit_order()
        self.filling_field_of_date_delivery(test_data)
        self.choice_of_rental_term()
        self.choice_of_scooter_color()
        self.input_comment(test_data)
        self.confirm_order()
        self.confirm_yes_in_popup()
