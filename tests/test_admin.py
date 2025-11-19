import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils import config
import time
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def test_admin_deleteuser(setup):
    driver = setup
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.login(config.USERNAME, config.PASSWORD)

    assert driver.title == "OrangeHRM"

    driver.find_element(By.XPATH, '//span[normalize-space() = "Admin"]').click()
    driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[2]").click()
    driver.find_element(By.XPATH,
        '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'
    ).click()
    mywait = WebDriverWait(driver, 10)
    toast = mywait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Successfully Deleted')]"))
    )
    # assert "Successfully Deleted" in toast.text
    assert "Successfully Deleted" in driver.page_source

    print("Toast text:", toast.text)
    file_name = "test_admin_deleteuser " + time.localtime()
    driver.save_screenshot(f"reports/screenshot/{file_name}.png")
    print(driver.page_source)