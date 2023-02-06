import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.aboutus_locatores import aboutus_locators
from web.utils.utils import Utils


class aboutus_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.about_page = aboutus_locators.about_us_xp
        self.video = aboutus_locators.video_id
        self.close = aboutus_locators.close_aboutus

    @allure.step
    @allure.description('Navigate to login page')
    def aboutus_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.about_page).click()
        time.sleep(3)


    @allure.step
    @allure.description('Navigate to login page')
    def aboutus_page_video(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, self.video).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def aboutus_page_close(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)
