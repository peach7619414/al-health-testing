import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_profile_update_browserstack():
    desired_cap = {
        'browser': 'Chrome',
        'os': 'Windows',
        'os_version': '11',
        'name': 'Profile Update Test',
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
    driver.get("https://allarahealth.com/profile")
    driver.find_element(By.ID, "name").clear()
    driver.find_element(By.ID, "name").send_keys("Updated User")
    driver.find_element(By.ID, "save-button").click()
    assert "Profile updated" in driver.page_source
    driver.quit()