from selenium.webdriver.common.by import By


class InformPage:       # Создание класса

    def __init__(self, driver):      # Инициализация класса
        self.driver = driver

    def check_inform_page(self):      #  Проверка системы, что открылась нужная страница
        checkout = self.driver.find_element(By.XPATH, '//span[contains(text(), "Checkout: Your Information")]')
        assert checkout.text == "Checkout: Your Information"

    def enter_data_about_user(self):       #  Ввод данных пользователя для оформления
        self.driver.find_element(By.ID, 'first-name').send_keys('TestName')
        self.driver.find_element(By.ID, 'last-name').send_keys('TestLastName')
        self.driver.find_element(By.ID, 'postal-code').send_keys('666666')

    def click_button_continue(self):     #  Нажатие кнопки для продолжения
        self.driver.find_element(By.ID, 'continue').click()



