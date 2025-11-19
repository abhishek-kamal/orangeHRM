from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def logout(self):
        self.driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

    def test_invalid_login(setup):
        driver = setup
        login = LoginPage(driver)

        login.open(config.BASE_URL)
        login.login("wrongUser", "wrongPass")
        assert "Invalid credentials" in login.get_error_text(), "Error message not displayed for invalid login"