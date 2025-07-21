from selenium.webdriver.common.by import By

class MainPageLocators:
    # Главная страница
    SCOOTER_LOGO = (By.CSS_SELECTOR, "[class*='Header_LogoScooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "[class*='Header_LogoYandex']")
    ORDER_BUTTON_IN_HEADER = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(text(), "Заказать")]')
    ORDER_BUTTON_IN_MAIN = (By.XPATH, '//button[contains(@class,"Button_Middle")]')
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
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

