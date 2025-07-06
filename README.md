# OrangeHRM Automation - Selenium Python POM Framework

## 📌 Project Objective

Automate the following processes for the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login):

- Login to the system
- Navigate to "My Leave"
- Perform Logout
- Validate each page loaded correctly

---

## 🧱 Project Structure

This framework follows the **Page Object Model (POM)** pattern and includes:

orangehrm_automation/
├── pages/
│ ├── login_page.py
│ ├── dashboard_page.py
│ └── leave_page.py
├── tests/
│ ├── test_login.py
│ ├── test_dashboard.py
│ ├── test_leave.py
│ └── test_logout.py
├── conftest.py
├── requirements.txt
└── README.md


---

## ⚙️ Tools & Technologies

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Git & GitHub

---

## ✅ Test Scenarios

| Test | Description | Status |
|------|-------------|--------|
| ✅ Login Test | Verifies login page and performs login | ✔️ Passed |
| ✅ Dashboard Test | Verifies Dashboard is loaded after login | ✔️ Passed |
| ✅ Leave Test | Navigates to Leave via Quick Launch | ✔️ Passed |
| ✅ Logout Test | Logs out from the application | ✔️ Passed |

---

## 🚀 How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/orangehrm-automation.git
   cd orangehrm-automation

2. Install dependencies:
pip install -r requirements.txt

3. Run tests using pytest:
pytest tests/

🔐 Credentials Used
Username: Admin
Password: admin123
(Provided by the OrangeHRM demo site)


📝 Author
Name: [Janidu Gamlath]
