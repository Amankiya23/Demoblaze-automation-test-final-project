from web.Page.home_page import Home_page
import allure
import pytest
from web.Base.Base_test import Base_test


class Test_login(Base_test):


    @allure.description('home page runs')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_home(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.web_page()

    @allure.description('home logo runs')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_home_logo(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.web_page_logo()

    @allure.description('homepage next slide')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_next(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.next_page_image()

    @allure.description('home page preview slide')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_preview(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.preview_page_image()

    @allure.description('home page scroll')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_scrool(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.scrool_page_down()

    @allure.description('home page product clickable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_product_home(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.cheak_page_product()

    @allure.description('home page product clickable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_product_home_price(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.cheak_page_product_price()

    @allure.description('home page next page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_product_home_next_slide(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.next_page_slide()

    @allure.description('home page preview page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_product_home_preview_slide(self):
        driver = self.driver
        web_pass_web = Home_page(driver)
        web_pass_web.preview_page_slide()



