from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    

    def is_dashboard_page_loaded(self):
         return "dashboard" in self.driver.current_url.lower()
    

    def click_my_leave(self):
        my_leave_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/leave')]")))
        my_leave_button.click()

