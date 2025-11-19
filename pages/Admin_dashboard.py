from selenium.webdriver.common.by import By


class Admin_dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.admin_page = (By.XPATH, '//span[normalize-space() = "Admin"]').click()


    # def delete_user(self):

