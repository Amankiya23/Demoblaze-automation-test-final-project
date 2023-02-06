from web.Page.signup_page import signin_page
import allure
import pytest
from web.Base.Base_test import Base_test
from web.utils.utils import Utils


class Test_signin(Base_test):


    @allure.description('signin page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_signin_works(self):
        driver = self.driver
        web_signin = signin_page(driver)
        web_signin.web_page()

    @allure.description('existing user')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_signin_valid(self):
        driver = self.driver
        signin_button = signin_page(driver)
        signin_button.web_page()
        email = signin_page(driver)
        email.sign_page()
        alert = driver.switch_to.alert
        alert.accept()



    @allure.description('signin with valid null_email & password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_signin_email_null(self):
        driver = self.driver
        signin_button = signin_page(driver)
        signin_button.web_page()
        email = signin_page(driver)
        email.null_user_page()
        passs = signin_page(driver)
        passs.pass_page()
        signin = signin_page(driver)
        signin.button_signin()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('signin with valid email & null_password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_signin_pass_null(self):
        driver = self.driver
        signin_button = signin_page(driver)
        signin_button.web_page()
        passs = signin_page(driver)
        passs.null_pass_page()
        signin = signin_page(driver)
        signin.button_signin()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('signin with null email & password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_signin_all_null(self):
        driver = self.driver
        signin_button = signin_page(driver)
        signin_button.web_page()
        signin = signin_page(driver)
        signin.button_signin()
        alert = driver.switch_to.alert
        alert.accept()





