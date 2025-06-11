# 🧪 Allara Health QA Testing Portfolio

This is a complete software testing portfolio for the **Allara Health** web platform, showcasing full coverage using manual and automated QA tools.

---

## 🔧 Tools Used

- **Selenium WebDriver (Python)** – UI test automation
- **Cucumber (Gherkin)** – BDD test scenarios
- **BrowserStack** – Cross-browser cloud execution
- **Postman** – API testing
- **SQL** – Backend validation
- **Jenkins** – CI/CD test pipeline
- **Allure** – Test reporting

---

## 📁 Folder Structure

```
Allara_Health_QA_Portfolio/
│
├── Jenkins_Pipeline/           # Jenkinsfile for CI/CD automation
├── Reports/                    # HTML Pytest reports
├── Allure_Reports/             # Allure report directory
├── Test_Cases/
│   ├── CSV/                    # Test cases in Excel-friendly format
│   └── Gherkin/                # Gherkin .feature files
├── Selenium_Scripts/           # Python-based UI tests
├── SQL_Scripts/                # Backend SQL validation
├── Postman_Collections/        # Postman API tests
└── BrowserStack/               # Selenium tests for BrowserStack
```

---

## 🚀 How to Run

1. **Clone the repository**
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests locally:
   ```
   pytest Selenium_Scripts/ --html=Reports/pytest_report.html --self-contained-html
   ```
4. Generate Allure Report:
   ```
   pytest --alluredir=allure-results
   allure generate allure-results --clean -o Allure_Reports
   ```

---

## 🔐 GitHub Secrets (CI/CD Integration)

If integrating into GitHub Actions:

- Add the following under **Settings > Secrets and Variables > Actions**
  - `BROWSERSTACK_USERNAME`
  - `BROWSERSTACK_KEY`

---

## 📊 View Reports

- HTML: Open `Reports/pytest_report.html`
- Allure: Open index.html inside `Allure_Reports/`

---

## ✅ Test Coverage

Includes **30+ test cases**, covering:
- Authentication (login, logout, register, forgot password)
- Booking & payments
- Security (SQLi, XSS)
- UI & Mobile responsiveness
- Profile validations (ZIP, phone)
- API endpoints
- CI/CD reporting with Jenkins + Allure

---

**Author:** QA Analyst Portfolio (Sonya)  
**Website under Test:** [https://allarahealth.com](https://allarahealth.com)
