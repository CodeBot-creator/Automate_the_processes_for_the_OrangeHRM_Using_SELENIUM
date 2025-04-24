from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        
    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
        login_button.click()






    

    







