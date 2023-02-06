from web.Page.aboutus_page import aboutus_page
import allure
import pytest
from web.Base.Base_test import Base_test


class Test_signin(Base_test):


    @allure.description('valid aboutus page works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_aboutus_works(self):
        driver = self.driver
        web_signin = aboutus_page(driver)
        web_signin.aboutus_page()

    @allure.description('valid aboutus video works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_aboutus_video(self):
        driver = self.driver
        web_signin = aboutus_page(driver)
        web_signin.aboutus_page()
        video = aboutus_page(driver)
        video.aboutus_page_video()

    @allure.description('cancel the page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_aboutus_cancle(self):
        driver = self.driver
        web_signin = aboutus_page(driver)
        web_signin.aboutus_page()
        cancle = aboutus_page(driver)
        cancle.aboutus_page_close()
