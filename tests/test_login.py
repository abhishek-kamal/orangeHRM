import pytest
from pages.login_page import LoginPage
from utils import config
from selenium.webdriver.common.by import By
from pages.Admin_dashboard import Admin_dashboard

def test_valid_login(setup):
    driver = setup
    driver.get(config.BASE_URL)

    # Login Page
    driver.find_element(By.NAME, "username").send_keys(config.USERNAME)
    driver.find_element(By.NAME, "password").send_keys(config.PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Assertion
    assert driver.title == "OrangeHRM"

def test_valid_login2(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.USERNAME, config.PASSWORD)
    assert driver.title == "OrangeHRM"


def test_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login(config.USERNAME, config.PASSWORD)
    login_page.logout()
    assert driver.title == "OrangeHRM"
