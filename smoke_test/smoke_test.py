from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.auth_page import AuthPage
from page.cart_page import CartPage
from page.filling_in_form_page import InformPage
from page.finish_page import FinishPage
from page.home_page import HomePage
from page.overview_page import OverviewPage


@pytest.mark.parametrize('creds', [('standard_user', 'secret_sauce')])  # Декоратор для параметризации. [логин и пароль пользователя.]
def test_full_smoke_order(creds):    # функция для smoke test
    login, password = creds        # Создание переменных из заданных данных
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys(login)         # Ввод логина
    driver.find_element(By.ID, 'password').send_keys(password)      # Ввод пароля
    auth_page = AuthPage(driver)            #   Сессия работы со страницей
    auth_page.click_login()             #  Клик по кнопке авторизации
    home_page = HomePage(driver)            #   Сессия работы со страницей
    home_page.sorter_choice_high_price_and_click()          #  Выбор в выпадающем списке нужного фильтра
    home_page.product_selection_and_click_button_add()          #  Выбор товара и добавление в корзину
    home_page.checking_changes_in_cart()                #   Проверка системы, что товар появился в корзине
    home_page.click_on_cart()               #    Переход в корзину
    cart_page = CartPage(driver)                #   Сессия работы со страницей
    cart_page.check_page_cart()               #  Проверка системы, что открылась нужная страница
    cart_page.click_button_checkout()                  #  Нажатие кнопки проверки
    filling_in_form_page = InformPage(driver)                   #   Сессия работы со страницей
    filling_in_form_page.check_inform_page()                #  Проверка системы, что открылась нужная страница
    filling_in_form_page.enter_data_about_user()                    #  Ввод данных пользователя для оформления
    filling_in_form_page.click_button_continue()                    #  Нажатие кнопки для продолжения
    overview_page = OverviewPage(driver)                    #  Сессия работы со страницей
    overview_page.check_overview_page()                     #  Проверка системы, что открылась нужная страница
    overview_page.click_button_finish()                     #  Нажатие кнопки завершения оформления
    finish_page = FinishPage(driver)                    #   Сессия работы со страницей
    finish_page.check_finish_page()                 #  Проверка системы, что открылась нужная страница
    finish_page.click_button_back_home()                            #  Нажатие кнопки вернуться на home page
    print('Order done an user back to home page')               #   Вывод, что заказ оформлен и открылась home page




