from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.user_dropdown = (By.XPATH, "//p[@class='oxd-userdropdown-name']")

    def is_dashboard_loaded(self):
        return self.driver.find_element(*self.dashboard_header).is_displayed()

    def navigate_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def open_user_menu(self):
        self.driver.find_element(*self.user_dropdown).click()
