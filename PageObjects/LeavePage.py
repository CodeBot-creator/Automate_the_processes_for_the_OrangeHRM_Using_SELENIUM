from selenium.webdriver.common.by import By

class Leave:
    def __init__(self, driver):
        self.driver = driver


    def clickMyLeave(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]").click()


    def is_leave_page_loaded(self):
         return "leave" in self.driver.current_url.lower()