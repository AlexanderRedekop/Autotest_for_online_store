from selenium.webdriver.common.by import By


class OverviewPage:          # Создание класса

    def __init__(self, driver):        # Инициализация класса
        self.driver = driver

    def check_overview_page(self):      #  Проверка системы, что открылась нужная страница
        checkout_overview = self.driver.find_element(By.XPATH, '//span[contains(text(), "Checkout: Overview")]')
        assert checkout_overview.text == "Checkout: Overview"

    def click_button_finish(self):        #  Нажатие кнопки завершения оформления
        self.driver.find_element(By.ID, 'finish').click()

