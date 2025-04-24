from PageObjects.LogoutPage import LogoutP
from selenium import webdriver
from PageObjects.LoginPage import Login 
import time



class Test_003_Logout:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    username = "Admin"
    password = "admin123"


    def test_logout(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Login
        login_page = Login(self.driver)
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login()

        time.sleep(5)  # wait for dashboard to load


        # Perform logout
        Logout = LogoutP(self.driver)
        Logout.clickUserDropdown()
        Logout.clickLogout()
        time.sleep(2)

        # Verify you are back on login page
        assert "login" in self.driver.current_url.lower()
        self.driver.quit()
