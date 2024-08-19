import allure
import pytest
from selenium import webdriver


@allure.title("To Verify Browser URL")
@allure.description("Enter url using chrome")
@pytest.mark.smoke
def test_sample():
    url = 'https://www.google.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    assert driver.current_url == url


@allure.title("To Verify Negative Browser URL")
@allure.description("Enter url using chrome")
@pytest.mark.smoke
def test_sample2():
    url = 'https://google.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    assert url == driver.current_url
