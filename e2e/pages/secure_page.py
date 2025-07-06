from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/h2")
                                           ))

    @property
    def flash_messages(self):
        return self.driver.find_element(By.ID, "flash")

    @property
    def secure_area_header(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h2")

    @property
    def secure_area_welcome_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h4")

    @property
    def logout_button(self):
        return self.driver.find_element(By.LINK_TEXT, "Logout")

    def logout(self):
        self.logout_button.click()
