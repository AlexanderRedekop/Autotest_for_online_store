from selenium.webdriver.common.by import By

class CartPage:      # Создание класса

    def __init__(self, driver): # Инициализация класса
        self.driver = driver

    def check_page_cart(self):          #  Проверка системы, что открылась нужная страница
        cart_client = self.driver.find_element(By.XPATH, '//span[contains(text(), "Your Cart")]')
        assert cart_client.text == "Your Cart"

    def click_button_checkout(self):         #  Нажатие кнопки проверки
        self.driver.find_element(By.ID, 'checkout').click()
