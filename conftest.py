import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from utils import config
import allure, os
import time

@pytest.fixture()
def setup():
    """Fixture to launch Chrome browser only"""
    options = ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(config.TIMEOUT)
    yield driver
    driver.quit()

time.localtime()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            os.makedirs("reports/screenshot", exist_ok=True)

            file_name = f"reports/screenshot/{item.name}.png"
            driver.save_screenshot(file_name)
            allure.attach.file(file_name, name=item.name, attachment_type=allure.attachment_type.PNG)
