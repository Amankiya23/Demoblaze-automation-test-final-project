from web.Page.contact_page import contact_page
import allure
import pytest
from web.Base.Base_test import Base_test


class Test_signin(Base_test):

    @allure.description('valid contactus_works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_contactus_works(self):
        driver = self.driver
        web_signin = contact_page(driver)
        web_signin.web_page()

    @allure.description('valid contactus_works_email')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_contactus_works_email(self):
        driver = self.driver
        web_signin = contact_page(driver)
        web_signin.web_page_email()

    @allure.description('valid contactus_works_name')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_contactus_works_name(self):
        driver = self.driver
        web_signin = contact_page(driver)
        web_signin.web_page_name()

    @allure.description('valid test_contactus_works_all')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_contactus_works_all(self):
        driver = self.driver
        web_signin = contact_page(driver)
        web_signin.web_page_all()

    @allure.description('contactus_cancle')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_contactus_cancle(self):
        driver = self.driver
        web_signin = contact_page(driver)
        web_signin.web_page_cancle()

