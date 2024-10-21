from selenium.webdriver.common.by import By

class AuthPage:      # Создание класса

    def __init__(self, driver):    # Инициализация класса
        self.driver = driver

    def click_login(self):     # Клик по кнопке авторизации
        self.driver.find_element(By.CSS_SELECTOR, 'input.submit-button.btn_action').click()
