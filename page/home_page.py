from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:              # Создание класса

    def __init__(self, driver):   # Инициализация класса
        self.driver = driver


    def sorter_choice_high_price_and_click(self):      # Выбор в выпадающем списке нужного фильтра
        sorter = self.driver.find_element(By.XPATH, '//select[starts-with(@class, "product")]')
        sel = Select(sorter)
        sel.select_by_value('hilo')

    def product_selection_and_click_button_add(self):     # Выбор товара и добавление в корзину
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    def checking_changes_in_cart(self):       #  Проверка системы, что товар появился в корзине
        cart = self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//span[@class = "shopping_cart_badge"]'),
                'class',
                'shopping_cart_badge'
            )
        )
        assert cart.text == '1'

    def click_on_cart(self):    # Переход в корзину
        self.driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
