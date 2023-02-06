import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.cart_locator import cart_locator
from web.Locator.Home_locatores import Homelocator
from web.Locator.cathagory_locator import category_locators


class cart_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.cart_page = cart_locator.cart_id
        self.order_button = cart_locator.order_button_xp
        self.name = cart_locator.name_ID
        self.country = cart_locator.country_ID
        self.city = cart_locator.city_ID
        self.credit_card = cart_locator.Creditcard_ID
        self.month = cart_locator.Month_ID
        self.year = cart_locator.Year_ID
        self.purchase = cart_locator.Purchase_XP
        self.close_xp = cart_locator.close_xp
        self.nokia = category_locators.phone_nokia_luma_xp
        self.samsung = category_locators.phone_samsung_galaxy6_xp
        self.add = Homelocator.add_to_cart
        self.name_send_key = cart_locator.name_send_key
        self.country_send_key = cart_locator.country_send_key
        self.city_send_key = cart_locator.city_send_key
        self.credit_send_key = cart_locator.credit_send_key
        self.month_send_key = cart_locator.month_send_key
        self.year_send_key = cart_locator.year_send_key
        self.delete = cart_locator.delete


    @allure.step
    @allure.description('Navigate to login page')
    def web_page_cart(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, self.cart_page).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_add_to_cart(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.add).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_cart_home_product(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.nokia).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_cart_home_product_samsung(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.samsung).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_cart_home_product_samsung(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.samsung).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_place_order(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.order_button).click()
        time.sleep(3)

    @allure.step
    @allure.description('cart delete product')
    def web_cart_delete(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.delete).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def place_order_valid(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys(self.name_send_key)
        time.sleep(3)
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys(self.country_send_key)
        time.sleep(3)
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys(self.city_send_key)
        time.sleep(3)
        credit = self.driver.find_element(By.ID, self.credit_card)
        credit.clear()
        credit.send_keys(self.credit_send_key)
        time.sleep(3)
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys(self.month_send_key)
        time.sleep(3)
        year = self.driver.find_element(By.ID, self.year)
        year.clear()
        year.send_keys(self.year_send_key)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(5)

    @allure.step
    @allure.description('invalid purchase')
    def place_order_invalid(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys(self.name_send_key)
        time.sleep(3)
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys(self.country_send_key)
        time.sleep(3)
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys(self.city_send_key)
        time.sleep(3)
        credit = self.driver.find_element(By.ID, self.credit_card)
        credit.clear()
        credit.send_keys(self.credit_send_key)
        time.sleep(3)
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys(self.month_send_key)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(5)

    @allure.step
    @allure.description('invalid purchase')
    def place_order_invalid_name(self):
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys(self.country_send_key)
        time.sleep(3)
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys(self.city_send_key)
        time.sleep(3)
        credit = self.driver.find_element(By.ID, self.credit_card)
        credit.clear()
        credit.send_keys(self.credit_send_key)
        time.sleep(3)
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys(self.month_send_key)
        time.sleep(3)
        year = self.driver.find_element(By.ID, self.year)
        year.clear()
        year.send_keys(self.year_send_key)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(5)

    @allure.step
    @allure.description('Navigate to login page')
    def place_order_valid_cancle(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys(self.name_send_key)
        time.sleep(3)
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys(self.country_send_key)
        time.sleep(3)
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys(self.city_send_key)
        time.sleep(3)
        credit = self.driver.find_element(By.ID, self.credit_card)
        credit.clear()
        credit.send_keys(self.credit_send_key)
        time.sleep(3)
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys(self.month_send_key)
        time.sleep(3)
        year = self.driver.find_element(By.ID, self.year)
        year.clear()
        year.send_keys(self.year_send_key)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close_xp).click()
        time.sleep(5)



