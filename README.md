# Al Health QA Automation Portfolio

This is a complete QA testing portfolio built for **AllaraHealth.com**, a healthcare platform focused on personalized care for women with chronic hormonal conditions.
The project demonstrates **full test coverage** across frontend (UI), backend (SQL), API, cross-browser testing, and visual reporting, using manual and automated testing strategies.

#Tools & Technologies Used

| Category            | Tools/Technologies                      |
|---------------------|-----------------------------------------|
| Test Management     | Jira + Zephyr                           |
| Manual Testing      | 30+ Test Cases (CSV format for Zephyr)  |
| Test Automation     | Selenium WebDriver (Python), Pytest     |
| API Testing         | Postman                                 |
| Database Validation | MySQL (via custom SQL queries)          |
| Reporting           | Pytest HTML Report, Allure              |
| Cross-Browser       | BrowserStack                            |
| Version Control     | Git + GitHub                            |

---

# Folder Structure
├── JIRA_Zephyr/
│ ├── Sample_Jira_Ticket/
│ │ ├── BUG-001_Login_Invalid_Credentials.md
│ │ └── allure_login_failure.png
│ └── README.md
├── Reports/
│ └── pytest_report.html
├── Allure_Reports/
│ └── index.html
├── Test_Cases/
│ └── CSV/
│ └── test_cases_allara.csv
├── Selenium_Scripts/
│ └── test_login.py, test_register.py, etc.
├── SQL_Scripts/
│ └── allara_queries.sql
├── Postman_Collections/
│ └── Allara_API_Tests.postman_collection.json
└── BrowserStack/
└── browser_config.json


---

# Highlights of Test Coverage

#  Manual Test Cases
- Written in CSV for easy Zephyr import
- Cover positive and negative flows for:
  - User Registration
  - Login & Logout
  - Forgot Password
  - Profile Management
  - Appointment Booking & Cancellation
  - Payment Flows (Success/Failure)

# UI Automation with Selenium
- Written in **Python + Pytest**
- Full interaction coverage with locators and assertions
- Covers dynamic elements, form validations, redirects

# API Testing with Postman
- Auth endpoints: Register, Login, Logout
- CRUD operations for appointments
- Payment gateway validation
- Status code + schema validation

# SQL Scripts
- Verify backend updates for user and appointment data
- Ensure payment transactions are logged
- Validate DB integrity for failed logins or null values

# BrowserStack
- Executed on Chrome, Safari, Firefox, and Edge
- Validated responsive behavior and layout across devices

---

# Jira Ticket Example

**Location:**  
`JIRA_Zephyr/Sample_Jira_Ticket/BUG-001_Login_Invalid_Credentials.md`

**Contents:**
- Title, Steps, Expected/Actual Results
- Linked Test Case: `TC002`
- Attached: `allure_login_failure.png` (report screenshot)

---
# HTML Report (Pytest):
Navigate to:

`Reports/pytest_report.html`

This report provides:
- A summary of all test executions
- Pass/Fail status for each test
- Execution time
- Detailed failure logs (if any)
- A visual overview of the test run using tables and charts

# Allure Report:
Launch in browser:
```bash
allure serve Allure_Reports/
```

**Includes:**
- Test run summary  
- Pass/Fail/Skip stats  
- Linked test cases & tags  
- Attachments for failed test steps  

---

# How to Run This Project

# Install Requirements
```bash
pip install selenium pytest pytest-html allure-pytest
```

# Run Tests & Generate Reports
```bash
pytest Selenium_Scripts/ --html=Reports/pytest_report.html --self-contained-html --alluredir=Allure_Reports/
allure serve Allure_Reports/
```

---

# Zephyr Integration Instructions
- Import test cases from `Test_Cases/CSV/test_cases_allara.csv` into your Zephyr test cycle.
- Log bugs using Jira (markdown in `/Sample_Jira_Ticket`)
- Attach test results (Allure/HTML) directly to Jira execution cycles

---

# Author

**Sonya Nelson**  
GitHub Portfolio  
QA Engineer | Manual & Automation | Selenium | Postman | SQL | Jira/Zephyr | Allure  
Based in New York City
