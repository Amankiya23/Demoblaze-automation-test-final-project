from web.Page.cart_page import cart_page
import allure
import pytest
from web.Base.Base_test import Base_test


class Test_signin(Base_test):

    @allure.description('verify cart page opens')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_cart_page(self):
        driver = self.driver
        web_signin = cart_page(driver)
        web_signin.web_page_cart()

    @allure.description('verify add_to_Cart_visibility')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_add_to_Cart_visibility(self):
        driver = self.driver
        web_signin = cart_page(driver)
        web_signin.web_page_cart_home_product()

    @allure.description('verify add to cart runs ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_add_to_cart(self):
        driver = self.driver
        samsung = cart_page(driver)
        samsung.web_page_cart_home_product_samsung()
        add = cart_page(driver)
        add.web_page_add_to_cart()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('on cart product remove')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_place_order_delete(self):
        driver = self.driver
        samsung = cart_page(driver)
        samsung.web_page_cart_home_product_samsung()
        add = cart_page(driver)
        add.web_page_add_to_cart()
        alert = driver.switch_to.alert
        alert.accept()
        web_signin = cart_page(driver)
        web_signin.web_page_cart()
        delete = cart_page(driver)
        delete.web_cart_delete()


    @allure.description('place order runs valid')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_place_order(self):
        driver = self.driver
        samsung = cart_page(driver)
        samsung.web_page_cart_home_product_samsung()
        add = cart_page(driver)
        add.web_page_add_to_cart()
        alert = driver.switch_to.alert
        alert.accept()
        web_signin = cart_page(driver)
        web_signin.web_page_cart()
        place_order = cart_page(driver)
        place_order.web_place_order()
        purchase = cart_page(driver)
        purchase.place_order_valid()

    @allure.description('place order runs invalid')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_place_order_invalid(self):
        driver = self.driver
        samsung = cart_page(driver)
        samsung.web_page_cart_home_product_samsung()
        add = cart_page(driver)
        add.web_page_add_to_cart()
        alert = driver.switch_to.alert
        alert.accept()
        web_signin = cart_page(driver)
        web_signin.web_page_cart()
        place_order = cart_page(driver)
        place_order.web_place_order()
        purchase = cart_page(driver)
        purchase.place_order_invalid()

    @allure.description('place order runs invalid name')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_place_order_invalid_name(self):
        driver = self.driver
        samsung = cart_page(driver)
        samsung.web_page_cart_home_product_samsung()
        add = cart_page(driver)
        add.web_page_add_to_cart()
        alert = driver.switch_to.alert
        alert.accept()
        web_signin = cart_page(driver)
        web_signin.web_page_cart()
        place_order = cart_page(driver)
        place_order.web_place_order()
        purchase = cart_page(driver)
        purchase.place_order_invalid_name()
        alert = driver.switch_to.alert
        alert.accept()

    @allure.description('place order runs valid and cancle ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_place_order_cancle(self):
        driver = self.driver
        samsung = cart_page(driver)
        samsung.web_page_cart_home_product_samsung()
        add = cart_page(driver)
        add.web_page_add_to_cart()
        alert = driver.switch_to.alert
        alert.accept()
        web_signin = cart_page(driver)
        web_signin.web_page_cart()
        place_order = cart_page(driver)
        place_order.web_place_order()
        purchase = cart_page(driver)
        purchase.place_order_valid_cancle()

