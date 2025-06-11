# Allara Health QA Portfolio Project

This project is a **comprehensive Quality Assurance (QA) testing suite** created to test the web application of [Allara Health](https://allarahealth.com). 
---

## Project Overview

**Allara Health** is a women’s health platform that provides virtual care and treatment for hormone-related conditions. This testing suite ensures that all key user workflows — from registration and login to appointments and payments — are robust, secure, and user-friendly.

---

## Tools & Technologies Used

| Folder                 | What’s Inside                                                       |
| ---------------------- | ------------------------------------------------------------------- |
| `Test_Cases/`          | Gherkin `.feature` files for login (valid & invalid)                |
| `Test_Cases_Excel/`    | CSV test cases (manual format) with positive & negative coverage    |
| `Selenium_Scripts/`    | Full browser automation: login, appointment, and payment flows      |
| `SQL_Scripts/`         | Data checks: user exists, duplicate appointments, declined payments |
| `BrowserStack/`        | Secure config script using environment variables                    |
| `Jenkins_Pipeline/`    | Jenkinsfile to run tests + generate Allure reports                  |
| `Postman_Collections/` | API collection to register users (POST) with JSON payload           |
| `Pytest_Execution/`    | Pytest automation suite with `@fixture` and real UI test flows      |
| `Reports/`             | For HTML reports (optional if running locally)                      |
| `Allure_Reports/`      | Allure integration instructions in `README.md`                      |

## Folder Structure

 Test_Cases → Gherkin (.feature) files
📂 Test_Cases_Excel → CSV-formatted test case documentation
📂 Selenium_Scripts → Full Selenium test scripts (login, payment, etc.)
📂 Pytest_Execution → Pytest suite with HTML report command
📂 SQL_Scripts → Queries to validate database state
📂 BrowserStack → Config using GitHub Secrets for cross-browser tests
📂 Jenkins_Pipeline → Jenkinsfile for CI/CD integration
📂 Postman_Collections → API test collection (valid/invalid scenarios)
📂 Reports → Configs + generated HTML test reports

yaml



---

## Test Coverage Summary

- User Registration (valid, invalid, edge cases)
- Login & Logout flows
- Appointment Booking (with and without selections)
- Payment with valid/invalid cards
- Profile Update
- API: Registration (positive + negative)
- SQL: Data integrity, duplicate checks, declined payments
- Responsive design: BrowserStack cloud execution
- Jenkins: Secure pipeline automation
- Reporting: HTML for visual validation

---

## How to Run Locally

> Ensure Python and Chrome are installed. Recommended: Python 3.9+

```bash
# 1. Clone the project
git clone https://github.com/YOUR-USERNAME/allara-health-qa-portfolio.git
cd allara-health-qa-portfolio

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install selenium pytest pytest-html

# 4. Run Pytest test suite with HTML report
pytest Pytest_Execution/test_allara_health.py --html=Reports/pytest_report.html

View Report
Open the file Reports/pytest_report.html in your browser.

GitHub Secrets (for BrowserStack or Jenkins)
If integrating into CI/CD:

Add BROWSERSTACK_USERNAME and BROWSERSTACK_KEY under:
GitHub > Settings > Secrets and Variables > Actions

About This Portfolio
This project was created by Sunny Nelson a QA Software Tester with professional experience in:

Manual and Automated Testing

Web UI, API, and Database Validation

Test Strategy & Execution

Agile SDLC & QA Reporting
