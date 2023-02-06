import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.contact_locator import contact_locator

class contact_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.contact_page = contact_locator.contact_page
        self.email = contact_locator.email_xp
        self.name = contact_locator.name_xp
        self.message = contact_locator.message_xp
        self.contact_close = contact_locator.contact_close_xp
        self.contact_send = contact_locator.contact_send_xp
        self.send_key_email = contact_locator.send_key
        self.send_key_name = contact_locator.send_key_name
        self.send_key_message = contact_locator.send_key_message

    @allure.step
    @allure.description('Navigate to login page')
    def web_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.contact_page).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_email(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.contact_page).click()
        time.sleep(3)
        Email = self.driver.find_element(By.XPATH, self.email)
        Email.clear()
        Email.send_keys(self.send_key_email)
        self.driver.find_element(By.XPATH, self.contact_send).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_name(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.contact_page).click()
        time.sleep(3)
        name = self.driver.find_element(By.XPATH, self.name)
        name.clear()
        name.send_keys(self.send_key_name)
        self.driver.find_element(By.XPATH, self.contact_send).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_all(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.contact_page).click()
        time.sleep(3)
        Email = self.driver.find_element(By.XPATH, self.email)
        Email.clear()
        Email.send_keys(self.send_key_email)
        name = self.driver.find_element(By.XPATH, self.name)
        name.clear()
        name.send_keys(self.send_key_name)
        message = self.driver.find_element(By.XPATH, self.message)
        message.clear()
        message.send_keys(self.send_key_message)
        self.driver.find_element(By.XPATH, self.contact_send).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_cancle(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.contact_page).click()
        time.sleep(3)
        Email = self.driver.find_element(By.XPATH, self.email)
        Email.clear()
        Email.send_keys(self.send_key_email)
        name = self.driver.find_element(By.XPATH, self.name)
        name.clear()
        name.send_keys(self.send_key_name)
        message = self.driver.find_element(By.XPATH, self.message)
        message.clear()
        message.send_keys(self.send_key_message)
        self.driver.find_element(By.XPATH, self.contact_close).click()
        time.sleep(3)

