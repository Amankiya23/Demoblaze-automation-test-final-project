import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.signin_locator import signin_locator
from web.utils.utils import Utils


class signin_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.signin_page = signin_locator.signin_id
        self.username_signin = signin_locator.si_Username_ID
        self.user_send_key = signin_locator.user_send_key1
        self.password_signin = signin_locator.si_Password_ID
        self.pass_send_key = signin_locator.pass_send_key1
        self.signup_button = signin_locator.Sign_up_XP
        self.close_signup = signin_locator.Close_XP

    @allure.step
    @allure.description('Navigate to login page')
    def web_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, self.signin_page).click()
        time.sleep(3)
        title = self.driver.title
        assert title == "STORE"

    @allure.step
    @allure.description('Navigate to login page')
    def sign_page(self):
        Email = self.driver.find_element(By.ID, self.username_signin)
        Email.clear()
        Email.send_keys(self.user_send_key)
        password = self.driver.find_element(By.ID, self.password_signin)
        password.clear()
        password.send_keys(self.pass_send_key)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.signup_button).click()
        time.sleep(5)

    @allure.step
    @allure.description('Navigate to login page')
    def null_user_page(self):
        Email = self.driver.find_element(By.ID, self.username_signin)
        Email.clear()
        password = self.driver.find_element(By.ID, self.password_signin)
        password.clear()
        password.send_keys(self.pass_send_key)
        time.sleep(2)


    @allure.step
    @allure.description('Navigate to login page')
    def pass_page(self):
        password = self.driver.find_element(By.ID, self.password_signin)
        password.clear()
        password.send_keys(self.pass_send_key)
        time.sleep(2)


    @allure.step
    @allure.description('Navigate to login page')
    def null_pass_page(self):
        Email = self.driver.find_element(By.ID, self.username_signin)
        Email.clear()
        Email.send_keys(self.user_send_key)
        password = self.driver.find_element(By.ID, self.password_signin)
        password.clear()
        time.sleep(2)

    @allure.step
    @allure.description('Navigate to login page')
    def button_signin(self):
        self.driver.find_element(By.XPATH, self.signup_button).click()
        time.sleep(5)



    @allure.step
    @allure.description('Navigate to login page')
    def cancle_signin(self):
        self.driver.find_element(By.XPATH, self.close_signup).click()
        time.sleep(5)


