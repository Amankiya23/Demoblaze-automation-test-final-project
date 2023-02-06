import time
from web.utils.utils import Utils
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from web.Locator.Home_locatores import Homelocator

class Home_page():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.logo = Homelocator.demoblaze_logo_id
        self.homepage = Homelocator.home_page_xp
        self.preview = Homelocator.preview_icon_name
        self.next = Homelocator.next_icon_name
        self.next_page = Homelocator.next_page_id
        self.preview_page = Homelocator.priview_page_id
        self.add_to_cart = Homelocator.add_to_cart
        self.delete_product = Homelocator.delete_product
        self.product_home = Homelocator.phone_home
        self.product_home2 = Homelocator.phone_home2


    @allure.step
    @allure.description('Navigate to login page')
    def web_page(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.homepage).click()

    @allure.step
    @allure.description('Navigate to login page')
    def web_page_logo(self):
        self.driver.find_element(By.ID, self.logo).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def next_page_image(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.next).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.next).click()
        time.sleep(2)

    @allure.step
    @allure.description('Navigate to login page')
    def preview_page_image(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.preview).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.preview).click()
        time.sleep(2)

    @allure.step
    @allure.description('Navigate to login page')
    def scrool_page_down(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def cheak_page_product(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.product_home).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def cheak_page_product_price(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.product_home2).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def next_page_slide(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        self.driver.find_element(By.ID, self.next_page).click()
        time.sleep(3)

    @allure.step
    @allure.description('Navigate to login page')
    def preview_page_slide(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.preview_page).click()
        time.sleep(3)









        
