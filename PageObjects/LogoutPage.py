from selenium.webdriver.common.by import By
import time

class LogoutP:
    logout_dropdown_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span"
    logout_link_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a"

    def __init__(self, driver):
        self.driver = driver

    def clickUserDropdown(self):
        self.driver.find_element(By.XPATH, self.logout_dropdown_xpath).click()

    def clickLogout(self):
        time.sleep(1)  # wait for the dropdown to load
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()
