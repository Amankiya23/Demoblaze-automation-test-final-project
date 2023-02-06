from web.Page.cathagory_page import cathegory_page
import allure
import pytest
from web.Base.Base_test import Base_test
from web.utils.utils import Utils


class Test_cathagory(Base_test):

    @allure.description('verify if the cathagory page runs')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_cathagory(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_cathagory()

    @allure.description('verify if the phone page runs')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()

    @allure.description('verify on product details page device name is displayed ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_samsung_s6(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_samsung_s6()

    @allure.description('verify on product details page device price is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_nokia(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_nokia()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_nexus(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_nexus()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_galaxy_s7(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_galaxy_s7()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_iphone_6(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_iphone_6()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_sony_xperia(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_sony_xperia()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_phone_htc_one(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_phone()
        phone = cathegory_page(driver)
        phone.phone_htc_one()








    @allure.description('verify if the laptop page runs')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_laptop(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_laptop_sony_i5(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()
        laptop = cathegory_page(driver)
        laptop.laptop_sony_i5()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_laptop_sony_i7(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()
        laptop = cathegory_page(driver)
        laptop.laptop_sony_i7()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_macbook_air(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()
        laptop = cathegory_page(driver)
        laptop.laptop_macbook_air()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_del_i7(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()
        laptop = cathegory_page(driver)
        laptop.laptop_del_i7()

    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_del_2017(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()
        laptop = cathegory_page(driver)
        laptop.laptop_del_2017()


    @allure.description('verify on product details page device name is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_macbook_pro(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_laptop()
        laptop = cathegory_page(driver)
        laptop.laptop_macbook_pro()







    @allure.description('verify if the monitor page runs')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_monitor(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_monitor()

    @allure.description('verify on product details page product discription is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_monitor_apple_24(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_monitor()
        monitor = cathegory_page(driver)
        monitor.monitor_apple_24()

    @allure.description('verify on product details page product discription is displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_monitor_assus_full_hd(self):
        driver = self.driver
        web_pass_web = cathegory_page(driver)
        web_pass_web.web_page_monitor()
        monitor = cathegory_page(driver)
        monitor.monitor_assus_full_hd()