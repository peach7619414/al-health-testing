import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_browserstack():
    desired_cap = {
        'browser': 'Chrome',
        'os': 'Windows',
        'os_version': '11',
        'name': 'Login Test',
        'build': 'Allara BrowserStack Build'
    }
    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_KEY')}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    driver.get("https://allarahealth.com/login")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "password").send_keys("SecurePass123")
    driver.find_element(By.ID, "login-button").click()
    assert "Dashboard" in driver.page_source
    driver.quit()