import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.cathagory_locator import category_locators


class cathegory_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.category_page = category_locators.catagories_id
        self.phone_page = category_locators.phone_xp
        self.galaxy6 = category_locators.phone_samsung_galaxy6_xp
        self.nokia = category_locators.phone_nokia_luma_xp
        self.nexus = category_locators.phone_nexus6_xp
        self.galaxy7 = category_locators.phone_samsung_galaxy7_xp
        self.iphone6 = category_locators.phone_iphone6_xp
        self.sony_xpria = category_locators.phone_sonyxpria_xp
        self.ht_cone = category_locators.phone_htcone_xp
        self.monitor_page = category_locators.monitor_xp
        self.apple_24 = category_locators.monitor_apple_24_xp
        self.assus_full_hd = category_locators.monitor_asus_fullhd_xp
        self.laptop_page = category_locators.laptop_xp
        self.sony_i5 = category_locators.laptop_sonyvio_i5_xp
        self.sony_i7 = category_locators.laptop_sonyvio_i7_xp
        self.macbook_air = category_locators.laptop_macbook_air_xp
        self.del_i7 = category_locators.laptop_del_i7_xp
        self.del_2017 = category_locators.laptop_del_2017_xp
        self.macbook_pro = category_locators.laptop_macbook_pro_xp

    @allure.step
    @allure.description('Navigate to cathagory page')
    def web_page_cathagory(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.ID, self.category_page).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page')
    def web_page_phone(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.phone_page).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page galaxy_s6')
    def phone_samsung_s6(self):
        self.driver.find_element(By.XPATH, self.galaxy6).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page nokia')
    def phone_nokia(self):
        self.driver.find_element(By.XPATH, self.nokia).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page nexus')
    def phone_nexus(self):
        self.driver.find_element(By.XPATH, self.nexus).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page galaxy_s7')
    def phone_galaxy_s7(self):
        self.driver.find_element(By.XPATH, self.galaxy7).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page iphone_6')
    def phone_iphone_6(self):
        self.driver.find_element(By.XPATH, self.iphone6).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page sony_xperia')
    def phone_sony_xperia(self):
        self.driver.find_element(By.XPATH, self.sony_xpria).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to phone page htc_one')
    def phone_htc_one(self):
        self.driver.find_element(By.XPATH, self.ht_cone).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page')
    def web_page_laptop(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.laptop_page).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page sony_i5')
    def laptop_sony_i5(self):
        self.driver.find_element(By.XPATH, self.sony_i5).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page sony_i7')
    def laptop_sony_i7(self):
        self.driver.find_element(By.XPATH, self.sony_i7).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page macbook_air')
    def laptop_macbook_air(self):
        self.driver.find_element(By.XPATH, self.macbook_air).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page del_i7')
    def laptop_del_i7(self):
        self.driver.find_element(By.XPATH, self.del_i7).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page del_2017')
    def laptop_del_2017(self):
        self.driver.find_element(By.XPATH, self.del_2017).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page macbook_air')
    def laptop_macbook_pro(self):
        self.driver.find_element(By.XPATH, self.macbook_pro).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_monitor(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.monitor_page).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page apple_24')
    def monitor_apple_24(self):
        self.driver.find_element(By.XPATH, self.apple_24).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to laptop page assus_full_hd')
    def monitor_assus_full_hd(self):
        self.driver.find_element(By.XPATH, self.assus_full_hd).click()
        time.sleep(3)
