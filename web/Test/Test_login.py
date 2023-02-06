from web.Page.login_page import login_page
import allure
import pytest
from web.Base.Base_test import Base_test
from web.utils.utils import Utils


class Test_login(Base_test):


    @allure.description('login page works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_works(self):
        driver = self.driver
        web_signin = login_page(driver)
        web_signin.web_page()

    @allure.description('login with invalid email & password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_invalid(self):
        driver = self.driver
        signin_button = login_page(driver)
        signin_button.web_page()
        email = login_page(driver)
        email.login_page()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('login with valid email & password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_valid(self,):
        driver = self.driver
        signin_button = login_page(driver)
        signin_button.web_page()
        email = login_page(driver)
        email.login_page_valid()



    @allure.description('login with valid null_email & password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_email_null(self):
        driver = self.driver
        signin_button = login_page(driver)
        signin_button.web_page()
        email = login_page(driver)
        email.null_user_page()
        passs = login_page(driver)
        passs.pass_page()
        signin = login_page(driver)
        signin.button_log()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('login with valid email & null_password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_pass_null(self):
        driver = self.driver
        signin_button = login_page(driver)
        signin_button.web_page()
        passs = login_page(driver)
        passs.null_pass_page()
        signin = login_page(driver)
        signin.button_log()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('login with null email & password')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_all_null(self):
        driver = self.driver
        signin_button = login_page(driver)
        signin_button.web_page()
        login = login_page(driver)
        login.button_log()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('login with valid email & password and logout')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_valid_logout(self):
        driver = self.driver
        signin_button = login_page(driver)
        signin_button.web_page()
        email = login_page(driver)
        email.login_page_valid()
        logout = login_page(driver)
        logout.logout()

