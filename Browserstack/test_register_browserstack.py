import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_register_browserstack():
    desired_cap = {
        'browser': 'Firefox',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Register Test',
        'build': 'Allara BrowserStack Build'
    }
    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_KEY')}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )
    driver.get("https://allarahealth.com/register")
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "password").send_keys("Test@1234")
    driver.find_element(By.ID, "confirm-password").send_keys("Test@1234")
    driver.find_element(By.ID, "register-button").click()
    assert "Welcome" in driver.page_source
    driver.quit()