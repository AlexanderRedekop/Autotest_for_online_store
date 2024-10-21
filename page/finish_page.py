from selenium.webdriver.common.by import By


class FinishPage:     # Создание класса

    def __init__(self, driver):    # Инициализация класса
        self.driver = driver

    def check_finish_page(self):       #  Проверка системы, что открылась нужная страница
        checkout_complete = self.driver.find_element(By.XPATH, '//h2[@class="complete-header"]')
        assert checkout_complete.text == "Thank you for your order!"

    def click_button_back_home(self):        #  Нажатие кнопки вернуться на home page
        self.driver.find_element(By.ID, 'back-to-products').click()