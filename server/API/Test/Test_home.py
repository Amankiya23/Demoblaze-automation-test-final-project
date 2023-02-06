from server.API.Constants.home_constant import homeConstants
import requests
import allure


class Test_Search:
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("lala")
    @allure.description('Search correctly in the website')
    def test_search_correctly(self):
        value = homeConstants.value_valid
        url = homeConstants.url_search_phone + value
        res = requests.post(url)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5

    @allure.severity(allure.severity_level.MINOR)
    @allure.description('Search incorrectly - in the website ')
    def test_search_incorrectly_when_city_not_exist(self):
        value = homeConstants.value_invalid
        url = homeConstants.url_search_phone + value
        res = requests.post(url)
        assert res.status_code == 404
        assert res.elapsed.total_seconds() < 10

