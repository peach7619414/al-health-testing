import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_forgot_password_browserstack():
    desired_cap = {
        'browser': 'Edge',
        'os': 'Windows',
        'os_version': '11',
        'name': 'Forgot Password Test',
        'build': 'Allara BrowserStack Build'
    }
    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_KEY')}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    driver.get("https://allarahealth.com/forgot-password")
    driver.find_element(By.ID, "email").send_keys("user@example.com")
    driver.find_element(By.ID, "reset-button").click()
    assert "Reset link sent" in driver.page_source
    driver.quit()