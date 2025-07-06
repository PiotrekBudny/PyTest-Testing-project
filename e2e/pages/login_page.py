from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

    @property
    def username_input(self):
        return self.driver.find_element(By.ID, "username")

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    @property
    def flash_messages(self):
        return self.driver.find_element(By.ID, "flash")

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
