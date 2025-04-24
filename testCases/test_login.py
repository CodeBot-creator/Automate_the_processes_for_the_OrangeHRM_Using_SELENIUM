from selenium import webdriver
from PageObjects.LoginPage import Login 
import time


class Test_001_Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # Create an instance of the Login class
        login_page = Login(self.driver)

        # Enter username and password
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)

        # Click the login button
        login_page.click_login()

        # Add assertions to verify successful login

        time.sleep(5)  # Wait for a few seconds to observe the result
        self.driver.quit()  # Close the browser after the test is done


    def test_home_page_title(self):
        driver = webdriver.Chrome()
        driver.get(self.baseURL)
        assert "OrangeHRM" in driver.title
        driver.quit()


    


    



    







        


