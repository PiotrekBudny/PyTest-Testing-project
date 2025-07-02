from selenium.webdriver.common.by import By

class SecurePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def flash_messages(self):
        return self.driver.find_element(By.ID, "flash")
    
    @property
    def secure_area_header(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h2/i")
    
    @property
    def secure_area_welcome_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h4")
    
    @property
    def logout_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/logout']")
    
    def logout(self):
        self.logout_button.click()
   