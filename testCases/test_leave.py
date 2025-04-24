from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.LeavePage import Leave
from PageObjects.dashboard_page import DashboardPage
import time

class Test_002_Leave:

    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"
    username = "Admin"
    password = "admin123"

    def test_leave(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        driver.maximize_window()

        # Login
        login_page = Login(driver)
        login_page.enter_username(self.username)
        login_page.enter_password(self.password)
        login_page.click_login()

        time.sleep(5)  # wait for dashboard to load

        # Dashboard - click My Leave
        dashboard = DashboardPage(driver)
        dashboard.click_my_leave()

        time.sleep(3)  # wait for leave page to load

        # Leave Page - verify leave page loaded
        leave_page = Leave(driver)
        assert leave_page.is_leave_page_loaded()

        driver.quit()
