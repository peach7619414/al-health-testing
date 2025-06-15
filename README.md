# Allara Health QA Automation Portfolio

This is a complete QA testing portfolio built for **AllaraHealth.com**, a healthcare platform focused on personalized care for women with chronic hormonal conditions.

The project demonstrates **full test coverage** across frontend (UI), backend (SQL), API, cross-browser testing, and visual reporting, using manual and automated testing strategies.

# Allara Health QA Automation Portfolio

This portfolio showcases full-spectrum QA testing for AllaraHealth.com, a digital platform for women's hormonal care. The project simulates a real-world test environment with manual and automated test coverage across UI, API, backend, and cross-browser layers.

---

## Tools Used

| Category        | Tools                          |
|----------------|--------------------------------|
| Test Management| Jira + Zephyr                  |
| UI Automation  | Selenium WebDriver (Python), Pytest |
| API Testing    | Postman                        |
| Backend Testing| MySQL + SQL Scripts            |
| Reporting      | Pytest HTML Report, Allure     |
| Cross-Browser  | BrowserStack                   |
| Source Control | Git + GitHub                   |

---

## Folder Structure
Allara_Health_QA_Portfolio_COMPLETE_FINAL/
├── JIRA_Zephyr/
│ ├── Sample_Jira_Ticket/ → Simulated Jira ticket with Allure screenshot
│ └── README.md → Zephyr import guide
├── Reports/ → HTML report from Pytest
├── Allure_Reports/ → Allure results (open via CLI)
├── Test_Cases/
│ └── CSV/ → 30+ Jira/Zephyr-ready test cases
├── Selenium_Scripts/ → Functional UI automation scripts
├── SQL_Scripts/ → DB validations
├── Postman_Collections/ → REST API testing
└── BrowserStack/ → Multi-browser configuration

## Sample Jira Ticket
See `JIRA_Zephyr/Sample_Jira_Ticket/BUG-001_Login_Invalid_Credentials.md` for a realistic Jira bug.  
This ticket includes a linked test case and an Allure report **screenshot** as attachment.

## Reporting
- **Pytest HTML Report:** `Reports/pytest_report.html`
- **Allure Report:** Open with:
```bash
allure serve Allure_Reports/

pytest Selenium_Scripts/ --html=Reports/pytest_report.html --alluredir=Allure_Reports/

Zephyr Integration
Test cases imported from Test_Cases/CSV/

Defects logged in Jira using structured markdown

Allure reports attached or linked per test case

Author
Sonya Nelson
QA Portfolio | Automation | API | Jira | SQL | Selenium | Allure

