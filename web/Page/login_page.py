import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.login_locator import login_locator
from web.utils.utils import Utils


class login_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.login = login_locator.login_id
        self.username = login_locator.lo_Username2_ID
        self.user_send_key = login_locator.user_send_key1
        self.user_send_key2 = login_locator.user_send_key2
        self.password = login_locator.lo_Password2_ID
        self.pass_send_key = login_locator.pass_send_key1
        self.pass_send_key2 = login_locator.pass_send_key2
        self.button_login = login_locator.Login_button_XP
        self.logout_page = login_locator.logout_ID
        self.cancle_login_xp = login_locator.cancle_login

    @allure.step
    @allure.description('Navigate to login page')
    def web_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, self.login).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def login_page(self):
        Email = self.driver.find_element(By.ID, self.username)
        Email.clear()
        Email.send_keys(self.user_send_key2)
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        password.send_keys(self.pass_send_key2)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_login).click()
        time.sleep(5)

    @allure.step
    @allure.description('Navigate to login page')
    def login_page_valid(self):
        Email = self.driver.find_element(By.ID, self.username)
        Email.clear()
        Email.send_keys(self.user_send_key)
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        password.send_keys(self.pass_send_key)
        # Utils(self.driver).assertion('Emanuel123', password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_login).click()
        time.sleep(5)

    @allure.step
    @allure.description('Navigate to login page')
    def null_user_page(self):
        Email = self.driver.find_element(By.ID, self.username)
        Email.clear()
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        password.send_keys(self.pass_send_key)
        time.sleep(2)



    @allure.step
    @allure.description('Navigate to login page')
    def pass_page(self):
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        password.send_keys(self.pass_send_key)
        time.sleep(2)


    @allure.step
    @allure.description('Navigate to login page')
    def null_pass_page(self):
        Email = self.driver.find_element(By.ID, self.username)
        Email.clear()
        Email.send_keys(self.user_send_key)
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        time.sleep(2)

    @allure.step
    @allure.description('Navigate to login page')
    def button_log(self):
        self.driver.find_element(By.XPATH, self.button_login).click()
        time.sleep(5)


    @allure.step
    @allure.description('Navigate to login page')
    def cancle_login(self):
        self.driver.find_element(By.CLASS_NAME, self.cancle_login_xp).click()
        time.sleep(5)

    @allure.step
    @allure.description('Navigate to login page')
    def logout(self):
        self.driver.find_element(By.ID, self.logout_page).click()
        time.sleep(5)







