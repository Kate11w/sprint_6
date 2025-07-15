from selenium.webdriver.common.by import By

class MainPageLocators:
    # Главная страница
    SCOOTER_LOGO = (By.XPATH, '//img[@alt="Scooter"]')
    YANDEX_LOGO = (By.XPATH, '//img[@alt="Yandex"]')
    ORDER_BUTTON_IN_HEADER = (By.XPATH, '//button[contains(text(), "Заказать")][1]')
    ORDER_BUTTON_IN_MAIN = (By.XPATH, '//button[contains(@class,"Button_Middle")]')
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    QUESTIONS_TITLE = (By.XPATH, "//div[text() = 'Вопросы о важном']")

    # Вопросы о важном
    QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    # Ответы
    ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]

